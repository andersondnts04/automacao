import pyautogui as pa
import time
import pyperclip
pa.PAUSE = 1


pa.press('win')
pa.write("chrome")
pa.press('ENTER')
pa.write('youtube.com')
pa.press('ENTER')
time.sleep(5)
pa.click(x=611, y=134)
pyperclip.copy("legiao urbana")
pa.hotkey('ctrl', 'v')
pa.press('ENTER')
