Setup:
The Nicla Vision Arduino board runs software on openMV,
https://docs.openmv.io/openmvcam/tutorial/openmvide_overview.html
https://docs.arduino.cc/hardware/nicla-vision/

for more information or troubleshooting, see docs on openMV IDE and docs on Nicla board
Once openMV is downloaded and in usable condition and the Nicla Vision is connected to the computer via USB:

Follow instructions to open the Nicla file system in openMV (usually file -> Open File...). Save the project code (projCode.py) as main.py in openMV and load it onto the Nicla (drag drop into the file system, make sure it is the ONLY main.py in the Nicla file system). 

Unplug the Nicla from the computer.  Plug the board in to power source via battery pack and micro USB, and ground via GND pin and breadboard wire into the breadboard. 
The data wire should go from port D0 (the bottom left corner of the board) to the motor driver data port. If using a kill switch / dry run switch, this switch should be placed between the port D0 and the motor driver on the breadboard. The kill switch enables the board to run and function without the pump ever activating.
The external battery is connected to the motor drivers ground and Vin port, the Vout should be connected to the pump itself. The motor driver ground should also be connected to the breadboard ground, as well as the water pump ground (see circuit diagrams in related documentation). After all the connections are setup the camera is ready to detect faces and activate the pump accordingly.

Take the end of the water pump tubing that does NOT have the brass nozzle and stick it into your water reservoir. Mount the powered board at approximate face height. Mount the water pump tubing end with brass nozzle at desired spray height. Fill water reservoir with water. The device is now set up and should proceed to run the water spray function on facial recognition in a frame.

Once the board is powered and all wiring is complete, the board will blink red for one second indicating initialization, before flashing blue blinking to indicate scanning for faces. When a face is and detected in a camera frame, the RGB LED will transition to red as pre fire warning for three seconds. The LED will then transition to green, during which the pump is also activated and water will be sprayed from the nozzle. Following the water spray protocol, the light will turn a solid blue, indicating a cooldown, and the port connected to the pump is deactivated, turning off the pump.

To run with logging, run the code in openMV (in the IDE, connect the plug icon in the bottom left, then the green play button below the plug button) while the board is connected. This will allow for serial output logs to print in the terminal during operation.
