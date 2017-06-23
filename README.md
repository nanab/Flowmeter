# Flowmeter plugin for CraftbeerPi

This plugin is for a flowmeter of magnetic hall type. Like this https://www.adafruit.com/product/828.

Use a 10k ohm resistor on sensors signal pin to protect your Pi.

Wire the sensor to the pi:
Red -> 5v
Black -> GND
Red -> 10k ohm resistor -> GPIO pin

Add the sensor under System -> Hardware settings -> Sensors -> Flowmeter.

There is some http api commands avaliable.
To get the id of your sensor: http://<ip of pi>/api/flowmeter/list_all_sensors 
For getting the value of sensor: http://<ip of pi>/api/flowmeter/<sensor id>
For reseting the sensors value: http://<ip of pi>/api/flowmeter/<sensor id>/reset

As it is for now there is no way of adding a reset function direct on the flowmeter in gui. So i have implented an Actor for reseting the value as a workaround.

Add this under System -> Hardware settings -> Actors -> FlowmeterReset.
You have to enter the id of the flowmeter which you can find by using the api command http://<ip of pi>/api/flowmeter/list_all_sensors 


