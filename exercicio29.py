import time
import pyautogui
altura, largura = pyautogui.size()
print(pyautogui.position())
print(f'a altura é {largura} e a largura é {altura}')
time.sleep(5)
pyautogui.moveTo(x=529, y=17,duration=(5))
pyautogui.click()
