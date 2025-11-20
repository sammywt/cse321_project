

# openMV libraries (built into openMV firmware running on nicla vision) for...
# sensor - controlling camera sensor (start / stop, resolution, format, gain, exposure, etc..)
# image - image processing  - defines image class and methods to call on images
# micropython libraries
# time - similar to python time (sleep, measure, etc...)

# machine - micropython hardware abstraction
# LED -  controls onboard LED of openMV boards
# Pin - GPIO pins

import sensor, image, time
from machine import LED, Pin

# ---------- camera setup ----------
# reboots camera sensor , loads default settings
sensor.reset()
# sets how image data is stored per pixel (565 = 5 bits red, 6 bits green, 5 bitds blue)
# grayscale potentially faster? but cannot have color boxes w/ grayscale
sensor.set_pixformat(sensor.RGB565)
# sets output resolution - QVGA = 320x240
# (fast enough for face detection, large enough for full face, doesnt slow down Haar Cascade too much
sensor.set_framesize(sensor.QVGA)        # 320x240
# adjust image contrast slightly above normal (range -3 to 3)
sensor.set_contrast(1)
# default brightness level (range -3 to 3)
sensor.set_brightness(0)
# wait 1.5 seconsd while throwing away first frames
# lets auto exposure, auto white balance, gain control to settle
# ensures first frame used is stable / illuminated
sensor.skip_frames(time=1500)

# If image looks flipped:
# sensor.set_vflip(True)
# sensor.set_hmirror(True)

# ---------- face cascade (built-in ROM) ----------


face_cascade = image.HaarCascade("/rom/haarcascade_frontalface.cascade", stages=25)

# how strong feature match must be to count as detection
THRESH = 0.35

# lower scale = more sizes, more accurate, slower
# higher scale = faster, fewer window sizes checked, may miss faces
SCALE  = 1.25
# color of box drawn (not working)
BOX_COLOR = (0, 255, 0)
# how thick to draw face detection box (not working)
THICKNESS = 2

# ---------- leds ----------
led_red   = LED("LED_RED")
led_green = LED("LED_GREEN")
led_blue  = LED("LED_BLUE")

def leds_off():
    led_red.off()
    led_green.off()
    led_blue.off()

leds_off()

# ---------- pump GPIO ----------
PUMP_PIN_NAME = "PG12"     # botton left pin (D0)
pump = Pin(PUMP_PIN_NAME, Pin.OUT)
pump.value(0)  # pump off

# ---------- pump sequence ----------
def run_pump_sequence():
    # 1- red for 3s, pump off
    print("Sequence: RED (pre-pump)")
    led_red.on()
    led_green.off()
    led_blue.off()
    pump.value(0)
    time.sleep_ms(3000)

    # 2- green for 5s, pump ON
    print("Sequence: GREEN (pump ON)")
    led_red.off()
    led_green.on()
    led_blue.off()
    pump.value(1)   # HIGH -> tell driver to run pump
    time.sleep_ms(5000)

    # 3- blue for 3s, pump OFF
    print("Sequence: BLUE (cooldown, pump OFF)")
    led_red.off()
    led_green.off()
    led_blue.on()
    pump.value(0)
    time.sleep_ms(3000)

    # 4- all off, return to detection
    leds_off()
    print("Sequence done, resuming face detection")

# ---------- main loop ----------
clock = time.clock()
print("Frontal face detection running...")

while True:
    # update clock (start timing frame)
    clock.tick()
    # capture one image frame from camera sensor
    img = sensor.snapshot()
    # histogram equalization (improves contrast, makes detection work better)
    img.histeq()

# actually run face detection algo
    faces = img.find_features(face_cascade, threshold=THRESH, scale_factor=SCALE)

    if faces:
        # boxes for visual feedback (not working, likely because image freezes on recognition)
        for r in faces:
            print("rect:", r)
            img.draw_rectangle(r, color=BOX_COLOR, thickness=THICKNESS)

        print("FACE DETECTED ", len(faces))
        # pump/led sequence (detection pauses while this runs)
        run_pump_sequence()
        # after this returns, loop continues and face detection resumes




# DOCS
# https://docs.arduino.cc/resources/datasheets/ABX00051-datasheet.pdf
# https://docs.arduino.cc/resources/pinouts/ABX00051-full-pinout.pdf
# https://docs.arduino.cc/hardware/nicla-vision/#features
# https://docs.arduino.cc/tutorials/nicla-vision/getting-started/
# https://docs.openmv.io/library/omv.sensor.html
# https://docs.openmv.io/openmvcam/tutorial/script_structure.html
# https://docs.openmv.io/library/omv.image.html
# https://www.digikey.bg/en/maker/projects/how-to-build-a-face-tracking-
# pan-tilt-camera-with-openmv/91ef4610324847d38f33e3e9ded7e747
# https://www.cardinalpeak.com/blog/building-edge-ml-ai-applications-using-the-openmv-cam
# https://www.kendryte.com/k230_canmv/en/main/example/omv/image_process.html
# https://docs.openmv.io/library/omv.sensor.html
# https://docs.openmv.io/library/omv.image.html
# https://docs.openmv.io/library/time.html
# https://docs.openmv.io/openmvcam/quickref.html

# also prewritten code that comes loaded onto NICLA (opens when connecting to openMV IDE)

# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!

# import sensor
# import time

# sensor.reset()  # Reset and initialize the sensor.
# sensor.set_pixformat(sensor.RGB565)  # Set pixel format to RGB565 (or GRAYSCALE)
# sensor.set_framesize(sensor.QVGA)  # Set frame size to QVGA (320x240)
# sensor.skip_frames(time=2000)  # Wait for settings take effect.
# clock = time.clock()  # Create a clock object to track the FPS.

# while True:
#     clock.tick()  # Update the FPS clock.
#    img = sensor.snapshot()  # Take a picture and return the image.
#    print(clock.fps())  # Note: OpenMV Cam runs about half as fast when connected
    # to the IDE. The FPS should increase once disconnected.
