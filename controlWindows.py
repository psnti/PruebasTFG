import pyautogui,time
import  pywinauto

pyautogui.size()
(1920, 1080)
width, height = pyautogui.size()

pyautogui.moveTo(180, 1080, duration=0.25)
time.sleep(1);
pyautogui.click(180, 1080)
# pyautogui.moveTo(1300, 75, duration=0.25)
pyautogui.click(1300, 75)
pyautogui.click(1000, 430)



