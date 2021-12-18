import cv2
import pyautogui
import numpy as np
import time

class Full():
    def tabsClicked():
        x = pyautogui.locateOnScreen("PrivacyScreenshot\_utility1.png", grayscale=True, confidence = 0.4)
        a,b,c,d = x
        width, height= pyautogui.size()
        tabimage = pyautogui.screenshot(time.sleep(float(1.0)) ,region = (0, d-10, width, height-d))
        tabimage = cv2.cvtColor(np.array(tabimage), cv2.COLOR_RGB2BGR)
        cv2.imwrite("HiddenTabs.png", tabimage)
    def normalClicked():
        normalimg = pyautogui.screenshot()
        normalimg = cv2.cvtColor(np.array(normalimg), cv2.COLOR_RGB2BGR)
        cv2.imwrite("Normal.png", normalimg)
    def taskbarClicked():
        x = pyautogui.locateOnScreen("PrivacyScreenshot\_utility2.png", grayscale=True, confidence = 0.9)
        a,b,c,d = x
        width, height= pyautogui.size()
        tabimage = pyautogui.screenshot(time.sleep(float(1.0)) ,region = (0, 0, width, height-d-10))
        tabimage = cv2.cvtColor(np.array(tabimage), cv2.COLOR_RGB2BGR)
        cv2.imwrite("HiddenTaskbar.png", tabimage)
    def privacyClicked():
        x = pyautogui.locateOnScreen("PrivacyScreenshot\_utility2.png", grayscale=True, confidence = 0.9)
        a,b,c,d = x
        y = pyautogui.locateOnScreen("PrivacyScreenshot\_utility1.png", grayscale=True, confidence = 0.4)
        p,q,r,s = y
        width, height= pyautogui.size()
        image = pyautogui.screenshot(time.sleep(float(1.0)) ,region = (0, d-10, width, height-d-s))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imwrite("Both.png", image)




