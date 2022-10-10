from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Collections import Collections
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pywinauto import Application
from pywinauto.keyboard import send_keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException, NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json, uuid, os, pyotp, time, ast, requests
import urllib.parse as urlparse
from tkinter.messagebox import *
from pywinauto import taskbar
import subprocess
#from pywinauto.application import Application
class common:
    def __init__(self):
        self.seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        self.app = Application(backend="uia").connect(path="explorer.exe")
        self.sys_tray = self.app.window(class_name="Shell_TrayWnd")
        self.dirname = os.path.dirname(__file__)


    def launch_app_toppan(self):
        subprocess.call(['java', '-jar', 'OppenheimerProjectDev.jar'])