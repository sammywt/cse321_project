Setup:
The Nicla Vision Arduino board runs software on openMV,


for more information or troubleshooting, see docs on openMV IDE and docs on Nicla board
Once openMV is downloaded and in usable condition and the Nicla Vision is connected to the computer via USB:

Follow instructions to open the Nicla file system in openMV (usually file -> Open File...). Save the project code (projCode.py) as main.py in openMV and load it onto the Nicla (drag drop into the file system, make sure it is the ONLY main.py in the Nicla file system). 

Unplug the Nicla from the computer. Make sure that the board is connected to power via battery pack and micro USB, and ground via GND pin and breadboard wire. 
The data wire should go from port D0 (the bottom left corner of the board) to the motor driver data port. If using a kill switch / dry run switch, this switch should be placed between the port D0 and the motor driver. The kill switch enables the board to run and function without the pump ever activating.
The external battery is connected to the motor drivers ground and Vin port, the Vout should be connected to the pump itself. After all the connections are 
setup the camera is ready to detect faces and then activate the pump accordingly.

Once the board is powered and all wiring is complete, the board will blink red for one second indicating initialization, before flashing blue blinking to indicate scanning for faces. When a face is captured and detected in a frame, the RGB LED will transition to red as pre fire warning, green, during which the pump is also activated, and solid blue, indicating a cooldown.

To run with logging, run the code in openMV (in the IDE, connect the plug icon in the bottom left, then the green play button below the plug button) while the board is connected. This will allow for serial output logs to print in the terminal during operation.
