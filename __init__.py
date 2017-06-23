# -*- coding: utf-8 -*-
import os
from subprocess import Popen, PIPE, call
import time
from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
import json
from flask import Blueprint, render_template, jsonify, request
from modules.core.props import Property

blueprint = Blueprint('flowmeter', __name__)
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except Exception as e:
    print e
    pass

class FlowMeterData():
    SECONDS_IN_A_MINUTE = 60
    MS_IN_A_SECOND = 1000.0
    enabled = True
    clicks = 0
    lastClick = 0
    clickDelta = 0
    hertz = 0.0
    flow = 0 # in Liters per second
    pour = 0.0 # in Liters

    def __init__(self):
        self.clicks = 0
        self.lastClick = int(time.time() * FlowMeterData.MS_IN_A_SECOND)
        self.clickDelta = 0
        self.hertz = 0.0
        self.flow = 0.0
        self.pour = 0.0
        self.enabled = True

    def update(self, currentTime):
        self.clicks += 1
        # get the time delta
        self.clickDelta = max((currentTime - self.lastClick), 1)
        # calculate the instantaneous speed
        if (self.enabled == True and self.clickDelta < 1000):
            self.hertz = FlowMeterData.MS_IN_A_SECOND / self.clickDelta
            self.flow = self.hertz / (FlowMeterData.SECONDS_IN_A_MINUTE * 7.5)  # In Liters per second
            instPour = self.flow * (self.clickDelta / FlowMeterData.MS_IN_A_SECOND)  
            self.pour += instPour
        # Update the last click
        self.lastClick = currentTime

    def clear(self):
        self.pour = 0;
        return str(self.pour)

@cbpi.sensor
class Flowmeter(SensorPassive):
    fms = dict()
    gpio = Property.Select("GPIO", options=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])
    def init(self):
        try:
            GPIO.setup(int(self.gpio),GPIO.IN, pull_up_down = GPIO.PUD_UP)
            GPIO.add_event_detect(int(self.gpio), GPIO.RISING, callback=self.doAClick, bouncetime=20)
            self.fms[int(self.gpio)] = FlowMeterData()
        except Exception as e:
            print e
    def get_unit(self):
        unit = cbpi.get_config_parameter("flowunit", None)
        if unit is None:
             print "INIT FLOW DB"
             try:
                 cbpi.add_config_parameter("flowunit", "L", "select", "Flowmeter unit", options=["L","gal(us)","gal(uk)","qt"])
             except:
                 cbpi.notify("Flowmeter Error", "Unable to update database.", type="danger", timeout=None)
        return unit
    def doAClick(self, channel):
        currentTime = int(time.time() * FlowMeterData.MS_IN_A_SECOND)
        self.fms[self.gpio].update(currentTime)
    def convert(self, inputFlow):
        unit = cbpi.get_config_parameter("flowunit", None)
        if (unit == "gal(us)"): 
            inputFlow = inputFlow * 0.264172052
        elif (unit == "gal(uk)"): 
            inputFlow = inputFlow * 0.219969157
        elif (unit == "qt"): 
            inputFlow = inputFlow * 1.056688
        else:
            pass
        inputFlow = "{0:.2f}".format(inputFlow)
        return inputFlow
    def read(self):
        flow = self.fms[int(self.gpio)].pour
        flowConverted = self.convert(flow)
        self.data_received(flowConverted)
    def getValue(self,ett,tva):
        print ett
        print tva
        flow = self.fms[int(self.gpio)].pour
        flowConverted = self.convert(flow)
        return flowConverted
    def reset(self):
        self.fms[self.gpio].clear()
        Return 
@blueprint.route('/<int:t>/reset', methods=['GET'])
def reset_sensor_value(t):
    Flowmeter(t).reset
    return "OK"
@blueprint.route('/<int:t>', methods=['GET'])
def get_sensor_value(t):
    print t
    sensValue = Flowmeter().getValue

    return sensValue
@cbpi.initalizer()
def init(cbpi):
    print "INITIALIZE FlOWMETER SENSOR MODULE"
    cbpi.app.register_blueprint(blueprint, url_prefix='/api/flowmeter')
    print "READY"
