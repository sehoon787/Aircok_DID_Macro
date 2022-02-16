from webbrowser import get
from pyautogui import moveTo, click, press, hotkey
import pyautogui
from time import sleep

pyautogui.FAILSAFE = False
TERMINATE = False

def open_url(chrome_path, url):
    get(chrome_path).open(url)
    moveTo(200, 200)
    click()
    press('f11')
    moveTo(5000, 5000)  # (0, 0)이 되면 fail safe trigger

def close_url():
    moveTo(200, 200)
    click()
    press('f11')
    hotkey('ctrl', 'w')

def run(chrome_path, url_list, minute=5):
    while not TERMINATE:
        for url in url_list:
            open_url(chrome_path=chrome_path, url=url)
            for i in range(60*int(minute)):
                if TERMINATE:
                    break
                sleep(1)
            if not TERMINATE:
                close_url()
