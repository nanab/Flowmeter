# Flowmeter plugin for CraftbeerPi

This plugin is for a flowmeter of magnetic hall type. Like this https://www.adafruit.com/product/828.

Use a 10k ohm resistor on sensors signal pin to protect your Pi.

Wire the sensor to the pi:
<br>
Red -> 5v.
<br>
Black -> GND.
<br>
Red -> 10k ohm resistor -> GPIO pin.

Add the sensor under System -> Hardware settings -> Sensors -> Flowmeter.

You can choose between following units in System -> Parameter -> flowunit. (Conversion is builtin)
<br>
Liters.
<br>
Gallons US.
<br>
Gallons UK.
<br>
Quarts.
<br>

There is some http api commands avaliable.
<br>
To get the id of your sensor: http://"ip of pi":5000/api/flowmeter/list_all_sensors 
<br>
For getting the value of sensor: http://"ip of pi:5000api/flowmeter/"sensor id"
<br>
For reseting the sensors value: http://"ip of pi":5000/api/flowmeter/"sensor id"/reset

As it is for now there is no way of adding a reset function direct on the flowmeter in gui. So i have implented an Actor for reseting the value as a workaround.

Add this under System -> Hardware settings -> Actors -> FlowmeterReset.
<br>
You have to enter the id of the flowmeter which you can find by using the api command http://"ip of pi":5000/api/flowmeter/list_all_sensors 


