import keyboard
import time
from pynput.mouse import Button, Controller
from settings import mappings


mouse = Controller()
pressed_keys = []


def handle_press(keyboard_event):
  key_name = keyboard_event.name
  button_type = mappings[key_name]

  if keyboard_event.event_type == "up":
    pressed_keys.remove(key_name)
    mouse.release(button_type)

  elif key_name not in pressed_keys:
    pressed_keys.append(key_name)
    mouse.press(button_type)


def start():
  keyboard.unhook_all()
  for key_name in mappings:
    keyboard.on_press_key(key_name, handle_press, True)
    keyboard.on_release_key(key_name, handle_press, True)


if __name__ == "__main__":
  start()
  while True:
    time.sleep(1000000)
