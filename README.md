//There will be no more updates from me on this repo as i dont have a CPB system anymore.


# Flowmeter plugin for CraftbeerPi

This plugin is for a flowmeter of magnetic hall type. Like this https://www.adafruit.com/product/828.
<br>

Update: 
<br>
There is now a reset function on the sensor in GUI so i have removed the custom actor. To use this click on arrow on sensor an choose reset to zero.
<br>
Please make sure that you have the latest avaliable version of Craftbeerpi from github installed.

<br>
<br>
This plugin includes sensor, actor(for reseting the sensor) and a custom step.

Use a 10k ohm resistor on sensors signal pin to protect your Pi.

Wire the sensor to the pi:
<br>
Red -> 5v.
<br>
Black -> GND.
<br>
Yellow -> 10k ohm resistor -> GPIO pin.

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
<br>
You have to enter the id of the flowmeter which you can find by using the api command http://"ip of pi":5000/api/flowmeter/list_all_sensors 
<br>
<br>
There is a custom step added for the flowmeter.
<br>
When the step is started it powers on an actor and when it reaches the given volume it powers off the actor and finnishes the step.
<br>
Configurable values for the step is:
<br>
Actor 1: Actor 1 thats going to be turned On and Off.
<br>
Actor 2: Actor 2 thats going to be turned On and Off. ( This is optional you dont have to use it)
<br>
Sensor: Flowmeter thats going to be used to measure the volume.
<br>
Volume: How much liquid that should pass before turning off actor. 
<br>
Reset flowmeter when done: Here you can choose if you want the flowmeters value to be set to zero when step is finnished. 1 for yes and 0 for no.
