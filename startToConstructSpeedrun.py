import keyboard
import time
import sys

# Instructions
print("Press '1' to start")

# Wait for '1' to start
keyboard.wait('1')
print("Starting...")

# room 1
keyboard.press('shift')
keyboard.press('d')
time.sleep(.02)
keyboard.release('shift')
time.sleep(2)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')
time.sleep(1)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')

# room 2
time.sleep(2.8)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')
time.sleep(1.2)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')

# room 3
time.sleep(3.5)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')

# rooms 4-6
time.sleep(4.825)
keyboard.release('d')
keyboard.press('a')

# room 7
time.sleep(3.75)
keyboard.release('a')
time.sleep(.8)
keyboard.press('d')
time.sleep(1.9)
keyboard.release('d')
keyboard.press('a')
time.sleep(.25)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')
time.sleep(.9)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')
time.sleep(.9)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')
time.sleep(.9)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')

# room 8
time.sleep(1.525)
keyboard.release('a')
time.sleep(2)
keyboard.press('a')
time.sleep(.8)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')
keyboard.release('a')
time.sleep(.8)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')
keyboard.press('a')
time.sleep(.4)
keyboard.release('a')
time.sleep(1.55)
keyboard.press('a')
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')

# room 9
time.sleep(1.5)
keyboard.release('a')
time.sleep(.95)
keyboard.press('d')

# room 10
time.sleep(5.5)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')
time.sleep(1.1)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')

# room 11-13
time.sleep(6.65)
keyboard.release('d')
keyboard.press('a')
time.sleep(1.5)
keyboard.press('space')
time.sleep(.02)
keyboard.release('space')
time.sleep(3)
keyboard.release('a')

# End 
keyboard.press('esc')
keyboard.press('p')
time.sleep(.02)
keyboard.release('p')
print("Finished Executing. Fight Construct manually and position agaist the right boss door" \
"right after the final blow and run the next script")
