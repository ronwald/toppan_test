from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Dialogs import execute_manual_step as manual
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from pywinauto import Application
from pywinauto.keyboard import send_keys
from resources.config.accessorylib import accessorylib
import resources.pageobjects.accessory as accessory
from resources.config.common import common
import resources.pageobjects.common_ele as common_ele
import random
import ctypes
import json
import os, pandas
from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class kw_accessory:
    def __init__(self):
        self.seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')

    def javascript_click(self, locator):
        element = locator.replace('css:', '')
        self.seleniumlib.execute_javascript('document.querySelector("{}").click()'.format(element))
    
    def check_accessory_nav_content(self):
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.nav_arrow_back)
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.nav_arrow_forward)
        #self.seleniumlib.wait_until_element_is_visible(accessory.objects.nav_customize)
        #self.seleniumlib.wait_until_element_is_visible(accessory.objects.nav_performance)
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.nav_lighting)
        #self.seleniumlib.wait_until_element_is_visible(accessory.objects.nav_calibration)
        # self.seleniumlib.wait_until_element_is_visible(accessory.objects.nav_power)

    def click_lighting_tab(self):
        self.seleniumlib.click_element(accessory.objects.nav_lighting)

    def lighting_page_should_load(self):
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_brightness_slider)
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_so_display_checkbox)
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_so_idle_checkbox)
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_modes_quick_tab)
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_modes_advanced_tab)

    def drag_brightness_slider_to(self, value):
        driver = self.seleniumlib.driver
        action = ActionChains(driver)
        slider = driver.find_element_by_css_selector(accessory.objects.lighting_brightness_slider.replace('css:',''))
        pixels_to_move = common.compute_pixel_offset(self, slider, value)
        action.click_and_hold(slider)
        action.move_by_offset(-float(slider.size['width'])/2, 0)
        action.move_by_offset(pixels_to_move, 0)
        action.release().perform()

    def compute_pixel_offset(self, slider, value):
        slider_width = int(slider.size['width'])
        print('slider_width = ', slider_width)
        slider_min = int(slider.get_attribute('min'))
        slider_max = int(slider.get_attribute('max'))
        multiplier = slider_width / (slider_max-slider_min)
        slider_center_position = slider_width / 2
        value = int(value) - slider_min
        percentage_distance_from_center = (multiplier*value - slider_center_position) / slider_center_position
        offset = percentage_distance_from_center * (16 / 2) #16 be the thumbtack width. prolly should use the find_by_css function to get the width
        return multiplier*value - offset


    def brightness_slider_value_should_be(self, expected_value):
        brightness_value = self.seleniumlib.get_value(accessory.objects.lighting_brightness_slider)
        BuiltIn().should_be_equal(brightness_value, expected_value)

    def check_display_turned_off_checkbox(self):
        is_checked = self.seleniumlib.execute_javascript('return document.querySelector("#checkDisplay:checked")')
        if is_checked is None:
            self.seleniumlib.click_element(accessory.objects.sol_check_display)
            self.seleniumlib.checkbox_should_be_selected(accessory.objects.sol_checkbox_display)
        else:
            self.seleniumlib.click_element(accessory.objects.sol_check_display)
            self.seleniumlib.checkbox_should_not_be_selected(accessory.objects.sol_checkbox_display)


    def click_lighting_effect_dropdown(self):
        self.seleniumlib.click_element(accessory.objects.lighting_effect_dropdown)

    def set_lighting_to_quick_effects(self):
        is_qe = self.seleniumlib.execute_javascript('return document.querySelector("div.modes-tab:nth-child(1).active");')
        if not is_qe:
            self.seleniumlib.click_element(accessory.objects.lighting_modes_quick_tab)

    def click_color_dropdown(self):
        self.seleniumlib.click_element(accessory.objects.lighting_color_dropdown)

    def click_random_color_preset(self):
        random_color = accessory.objects.lighting_random_color_preset.format(random.randint(1, 40))
        self.seleniumlib.wait_until_element_is_visible(random_color)
        self.seleniumlib.click_element(random_color)

    # Cloned Method - TungH
    def check_toolbar_title(self, device_name):
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.toolbar_title, 5)
        name = self.seleniumlib.get_text(accessory.objects.toolbar_title)
        BuiltIn().should_be_equal(name.upper(), device_name.upper())

    def check_if_element_exists_by_css(self, css):
        driver = self.seleniumlib.driver
        try:
            driver.find_element_by_css_selector(css)
        except NoSuchElementException:
            return False
        return True

    def switch_brightness_button_to(self, status):
        is_on = self.check_if_element_exists_by_css(accessory.objects.lighting_brightness_switch_on.replace('css:', ''))
        if status.lower() == 'on' and not is_on:
            self.seleniumlib.click_element(accessory.objects.lighting_brightness_switch)
            self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_brightness_slider_on, 5)
            self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_brightness_switch_on, 5)
            self.seleniumlib.wait_until_element_is_not_visible(accessory.objects.lighting_brightness_slider_off, 5)
            self.seleniumlib.wait_until_element_is_not_visible(accessory.objects.sol_display_checkbox_off, 5)
        elif status.lower() == 'off' and is_on:
            self.seleniumlib.click_element(accessory.objects.lighting_brightness_switch)
            self.seleniumlib.wait_until_element_is_not_visible(accessory.objects.lighting_brightness_slider_on, 5)
            self.seleniumlib.wait_until_element_is_not_visible(accessory.objects.lighting_brightness_switch_on, 5)
            self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_brightness_slider_off, 5)
            self.seleniumlib.wait_until_element_is_visible(accessory.objects.sol_display_checkbox_off, 5)

    def switch_display_turned_off_checkbox(self, status):
        is_checked = self.seleniumlib.execute_javascript('return document.querySelector("#checkDisplay:checked")')
        if status == "On" and is_checked is None:
            self.seleniumlib.click_element(accessory.objects.sol_check_display)
            self.seleniumlib.checkbox_should_be_selected(accessory.objects.sol_checkbox_display)
        elif status == "Off" and is_checked is not None:
            self.seleniumlib.click_element(accessory.objects.sol_check_display)
            self.seleniumlib.checkbox_should_not_be_selected(accessory.objects.sol_checkbox_display)  

    def check_brightness_is_switched_on(self):
        brightness_status = self.check_if_element_exists_by_css(accessory.objects.lighting_brightness_switch_on.replace('css:', ''))
        BuiltIn().should_be_equal(brightness_status, True)
    
    def check_switchoff_display_option_is_disabled(self):
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_so_display_checkbox)
        is_checked = self.seleniumlib.execute_javascript('return document.querySelector("#checkDisplay:checked");')
        BuiltIn().should_be_equal(is_checked, None)

    def check_quick_effects_is_enabled(self):
        selected_mode = self.seleniumlib.get_webelement(accessory.objects.lighting_effectmode_active).text
        BuiltIn().should_be_equal(selected_mode.upper(), 'QUICK EFFECTS')
        common.validate_backgroundcolor_element(self, accessory.objects.lighting_quick_effects_tab, '#44d62c')
        common.validate_backgroundcolor_element(self, accessory.objects.lighting_advanced_effects_tab, '#111111')

    def check_default_quick_effect_is_spectrum(self):
        selected_effect = self.seleniumlib.get_webelement(accessory.objects.lighting_quick_effects_selected).text
        BuiltIn().should_be_equal(selected_effect, 'Spectrum Cycling')

    def default_brightness_button_should_be_on(self):
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_brightness_switch_on, 5)

    def hover_and_check_help_tooltip_for_lighting(self):
            # Verify the tip_text of lighting_brightness_help
        common.check_tooltip_when_hover(self, accessory.objects.lighting_brightness_help_icon, 
                accessory.objects.lighting_brightness_help_tip,
                accessory.objects.lighting_brightness_help_tip_text)
        # Verify the tip_text of lighting_swlight_help
        common.check_tooltip_when_hover(self, accessory.objects.lighting_swlight_help_icon, 
                accessory.objects.lighting_swlight_help_tip,
                accessory.objects.lighting_swlight_help_tip_text)
        # Verify the tip_text of lighting_effects_help
        common.check_tooltip_when_hover(self, accessory.objects.lighting_effects_help_icon, 
                accessory.objects.lighting_effects_help_tip,
                accessory.objects.lighting_effects_help_tip_text)

    def default_brightness_slider_attributes_are_expected(self):
        self.seleniumlib.element_attribute_value_should_be(accessory.objects.lighting_brightness_slider, 'min', '0')
        self.seleniumlib.element_attribute_value_should_be(accessory.objects.lighting_brightness_slider, 'max', '100')
        self.seleniumlib.element_attribute_value_should_be(accessory.objects.lighting_brightness_slider, 'step', '1')
        # self.seleniumlib.element_attribute_value_should_be(mouse.objects.lighting_brightness_slider, 'value', '100')

    def quick_effects_mode_is_default_active(self):
        self.seleniumlib.wait_until_element_is_visible(accessory.objects.lighting_modes_quick_tab + '.active', 5)

    def default_switch_off_lighting_config_is_expected(self):
        self.seleniumlib.wait_until_element_is_not_visible('css:#checkDisplay:checked', 5)
        # self.seleniumlib.wait_until_element_is_not_visible('css:#checkIdle:checked', 5)
        # self.seleniumlib.wait_until_element_is_not_visible(accessory.objects.sol_idle_duration_slider_on, 5)
        # self.seleniumlib.element_attribute_value_should_be(accessory.objects.sol_idle_duration_slider, 'min', '1')
        # self.seleniumlib.element_attribute_value_should_be(accessory.objects.sol_idle_duration_slider, 'max', '15')
        # self.seleniumlib.element_attribute_value_should_be(accessory.objects.sol_idle_duration_slider, 'step', '1')
        # self.seleniumlib.element_attribute_value_should_be(accessory.objects.sol_idle_duration_slider, 'value', '1')        

    def select_backward_button(self):
        self.seleniumlib.click_element(accessory.objects.nav_arrow_back)

    def select_forward_button(self):
        self.seleniumlib.click_element(accessory.objects.nav_arrow_forward)