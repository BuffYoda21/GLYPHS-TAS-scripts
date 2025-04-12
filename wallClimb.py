import keyboard
import time
import sys

# === Config ===
hold_space_duration = 0.2
hold_d_duration = 0.38
direction_hold_before_space = 0.05
hold_combo_duration = 0.1
dash_settle_time = 0.05
space_spam_duration = 0.2

print("Press '1' to start/resume, '2' to pause, '3' to kill, '4' to climb out at top of wall.")

# Wait for '1' to start
keyboard.wait('1')
print("Starting...")

while True:
    # Stop the script if '3' is pressed
    if keyboard.is_pressed('3'):
        print("Stopping.")
        sys.exit()

    # Emergency climb-out with '4'
    if keyboard.is_pressed('4'):
        print("Exiting.")

        # W + SPACE for upward dash
        keyboard.press('w')
        time.sleep(direction_hold_before_space)
        keyboard.press('space')
        time.sleep(hold_combo_duration)
        keyboard.release('w')
        keyboard.release('space')

        # Hold A to get on top of wall
        keyboard.press('a')
        time.sleep(1)
        keyboard.release('a')

        print("Stopping script.")
        sys.exit()

    # Pause if '2' is pressed
    if keyboard.is_pressed('2'):
        print("Paused. Press '1' to resume.")
        keyboard.wait('1')
        print("Resuming...")

    # Wall Jump
    start_time = time.time()
    while time.time() - start_time < space_spam_duration:
        keyboard.press('space')
        time.sleep(0.02)
        keyboard.release('space')

    # Create space between player and wall
    keyboard.press('d')
    time.sleep(hold_d_duration)
    keyboard.release('d')

    # Dash into wall (W + A then SPACE)
    keyboard.press('w')
    keyboard.press('a')
    time.sleep(direction_hold_before_space)
    keyboard.press('space')

    time.sleep(hold_combo_duration)

    keyboard.release('w')
    keyboard.release('a')
    keyboard.release('space')

    # Let dash settle (animation delay)
    time.sleep(dash_settle_time)
