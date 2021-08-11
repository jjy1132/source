import pyautogui

position = pyautogui.position()

print(pyautogui.size())

print(position.x)
print(position.y)

pyautogui.moveTo(500,500)

pyautogui.moveTo(100,100,2)

pyautogui.moveRel(200,300,2)

pyautogui.click()

pyautogui.click(clicks=2,interval=2)

pyautogui.doubleClick()

pyautogui.click(button='right')

pyautogui.scroll(10)

pyautogui.drag(0,300,1, button='left')
