from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Collections import Collections
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pywinauto import Application
import resources.pageobjects.home as home
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
import requests
import win32gui, win32con

class common:
    def __init__(self):
        self.seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        self.app = Application(backend="uia").connect(path="explorer.exe")
        self.sys_tray = self.app.window(class_name="Shell_TrayWnd")
        self.dirname = os.path.dirname(__file__)


    def launch_app_toppan(self):
        print('Launching application.....')
        subprocess.Popen(['java', '-jar', 'OppenheimerProjectDev.jar'])
    
    def close_app_toppan(self):
        print('Launching application.....')
        subprocess.terminate()
    
    def insert_single_record_test(self):
        url = 'http://localhost:8080/calculator/insert'
        headers = {
            'Content-Type': 'application/json'                      
        }
        myobj = {
                    "birthday": "20041985",
                    "gender": "M",
                    "name": "Ronwald",
                    "natid": "abc123",
                    "salary": "10000",
                    "tax": "2000"
        }
        x = requests.post(url, headers=headers, json = myobj, verify = False)
        x.raise_for_status()
        print(x.text)
    
    def retrieve_taxrelief_natid_name(self):
        url = 'http://localhost:8080/calculator/taxRelief'
        headers = {
            'Content-Type': 'application/json'                      
        }
        x = requests.get(url, headers=headers, verify = False)
        x.raise_for_status()
        result = x.json()
        print(result)
    
    def verify_5th_character_dollar_sign(self):
        url = 'http://localhost:8080/calculator/taxRelief'
        headers = {
            'Content-Type': 'application/json'                      
        }
        x = requests.get(url, headers=headers, verify = False)
        x.raise_for_status()
        result = x.json()
        print(result)
        for item in x.json():
            natid = item['natid']
            print('natid------------', natid)
            if natid[4]=='$':
                print('5th character of the natid field is a $ sign')
                break
        #return str(item['natid'])
    
    def verify_taxrelief_has_two_decimal_places(self):
        url = 'http://localhost:8080/calculator/taxRelief'
        headers = {
            'Content-Type': 'application/json'                      
        }
        x = requests.get(url, headers=headers, verify = False)
        x.raise_for_status()
        result = x.json()
        print(result)
        for item in x.json():
            relief = item['relief']
            print('relief------------', relief)
            if len(relief.rsplit('.')[-1]) == 2:
                print('Tax relief has 2 decimal places')
                break
        #return str(item['natid'])
    
    def insert_multiple_record_test(self):
        url = 'http://localhost:8080/calculator/insertMultiple'
        headers = {
            'Content-Type': 'application/json'                      
        }
        myobj = [
                    {
                        "birthday": "20041985",
                        "gender": "M",
                        "name": "Ronwald",
                        "natid": "abc123",
                        "salary": "10000",
                        "tax": "2000"
                    },
                    {
                        "birthday": "14071998",
                        "gender": "F",
                        "name": "Anne",
                        "natid": "bxs123",
                        "salary": "20000",
                        "tax": "4000"
                    }
        ]
        x = requests.post(url, headers=headers, json = myobj, verify = False)
        x.raise_for_status()
        print(x.text)
    
    def click_upload_csv_file_button(self):
        #self.seleniumlib.wait_until_element_is_visible(home.objects.upload_csv_file_button)
        self.seleniumlib.click_element(home.objects.upload_csv_file_button)
    
    def enter_csv_file_location(self, filename):
        print(filename)
        BuiltIn().sleep('2s')
        handle = win32gui.FindWindow(None, 'Open')
        win32gui.SetForegroundWindow(handle)
        send_keys(filename, 0.05, True)
        send_keys('{ENTER}')
    
    def check_tax_compute(self, salary, taxpaid, age, gender):
        actual_tax_relief = self.seleniumlib.get_webelement(home.objects.tax_relief_field).text
        if gender=='Male':
            gender_bonus = 0
        else:
            gender_bonus = 500

        #convert the paramaters to integer
        converted_age = int(age)
        converted_salary= int(salary)
        converted_taxpaid= int(taxpaid)

        if converted_age<= 18:
            variable=1
        elif converted_age<= 35:
            variable=0.8
        elif converted_age<= 50:
            variable=0.5
        elif converted_age<= 75:
            variable=0.367
        elif converted_age>= 76:
            variable=0.05
        #print values for easy viewing
        print('salary---->', converted_salary)
        print('taxpaid---->', converted_taxpaid)
        print('gender bonus---->', gender_bonus)
        print('variable---->', variable)
        print('actual tax relief---->', actual_tax_relief)

        expected_tax_relief = ((converted_salary - converted_taxpaid) * variable) + gender_bonus
        print('expected tax_relief---->', str(expected_tax_relief))
        BuiltIn().should_be_equal(float(actual_tax_relief), float(expected_tax_relief))
    
    def verify_button_is_red(self):
        #this is the expected color in hexadecimal. NOTE : red is #FF0000
        expected_hex_color = '#dc3545'
        x = 'css:.btn-danger.btn-block'
        locator = x.replace('css:', '')
        driver = self.seleniumlib.driver
        element = driver.find_element_by_css_selector(locator)
        for _ in range(3):
            rgba = element.value_of_css_property('background-color')
            print('rgba color----', rgba)
            if rgba.startswith("rgba"):
                r, g, b, alpha = ast.literal_eval(rgba.strip("rgba"))
            elif rgba.startswith("rgb"):
                r, g, b = ast.literal_eval(rgba.strip("rgb"))
            hex_value = '#%02x%02x%02x' % (r, g, b)
            print('Actual color of the button in hex value ------', hex_value)
        #check that expected and actual are same   
        BuiltIn().should_be_equal(hex_value, expected_hex_color)
    
    def verify_text_is_dispense_now(self):
        expected_text = 'Dispense Now'
        actual_text = self.seleniumlib.get_webelement(home.objects.dispense_button).text
        print('The text of button is -----:', actual_text)
        BuiltIn().should_be_equal(expected_text, actual_text)
    
    def verify_cash_dispensed_text_displayed(self):
        expected_text = 'Cash dispensed'
        self.seleniumlib.click_element(home.objects.dispense_button)
        BuiltIn().sleep('2s')
        actual_text = self.seleniumlib.get_webelement(home.objects.cash_dispensed_text).text
        print('After click button, displayed text is -----:', actual_text)
        BuiltIn().should_be_equal(expected_text, expected_text)
