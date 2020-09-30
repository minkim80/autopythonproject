import pyautogui


print(pyautogui.position())

val = input ("Please enter the number of pages to screenshot: ")

for i in range(int(val)):
    pyautogui.click(3547, 589, 1)
    pyautogui.keyDown('win')
    pyautogui.press('prtscr')
    pyautogui.keyUp('win')
    


print('All Done!')



#Opens File Explorer
#pyautogui.click(521, 1060, 2)
#pyautogui.click(2407, 452, 2)