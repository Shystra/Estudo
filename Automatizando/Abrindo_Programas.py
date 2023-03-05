import pyautogui
import time

pyautogui.PAUSE = 5

pyautogui.press ("win")
pyautogui.write ("Spotify")
# pyautogui.press ("backspace") # Apaga uma letra

pyautogui.press ("enter")
pyautogui.click (x = 96, y = 102)
pyautogui.write ("The Weeknd")
pyautogui.press ("enter")

pyautogui.click (x = 672, y = 364)


time.sleep(3)
pyautogui.position()
print(pyautogui.position())
