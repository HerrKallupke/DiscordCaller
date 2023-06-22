import pyautogui as pag
import time


print('Move the cursor to the call deny button in discord. (5s)')
time.sleep(5)
call_deny_button = pag.position()

print('Position saved!')
while True:
    pag.moveTo(call_deny_button)
    pag.click()
    time.sleep(1)
