from novation import LaunchpadController
from actions import *
import time

# Create and connect to the launchpad
launchpad = LaunchpadController()
launchpad.connect()


buttons = {
    "0:0": up
}

active_buttons = {}

# Light up all action buttons
launchpad.flush()
for button in buttons:
    # Parse the XY
    x, y = button.split(":")
    x = int(x)
    y = int(y)

    # Write LED
    launchpad.setLED(x, y, 0, 5)


try:
    while True:

        # Read current button
        state = launchpad.currentButton()

        # Ensure button is valid
        if state:
            
            # Determine unique code for button
            code = f"{state[0]}:{state[1]}"

            # Ensure this is a "button down" event
            if active_buttons.get(code, False) == False:
                active_buttons[code] = True

                # Call back if possible
                if code in buttons:
                    buttons[code]()

            else:
                active_buttons[code] = False
        
        # Wait a bit
        time.sleep(0.3)



except KeyboardInterrupt as e:
    launchpad.disconnect()
    exit(0)
