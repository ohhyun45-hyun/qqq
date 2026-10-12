import pyautogui
import time

# 1. 화면 크기 출력
# print(pyautogui.size)

# 2. 마우스 위치 출력
# time.sleep(2)
# print(pyautogui.position())

# 3. 마우스 이동
# pyautogui.moveTo(830, 404, 2)

# 4. 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleclick()
# pyautogui.click(clicks=3, interval=1)

# 3099,58 -> 2930,59

pyautogui.moveTo(3099,58, 2)
pyautogui.dragTo(2930,59, 2)


