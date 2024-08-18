# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os


class PracticeForm:
    _first_name_input_xpath = '//input[@id="firstName"]'
    _last_name_input_xpath = '//input[@id="lastName"]'
    _email_input_xpath = '//input[@id="userEmail"]'
    _male_radio_button_xpath = '//label[@for="gender-radio-1"]'
    _mobile_phone_input_xpath = '//input[@id="userNumber"]'
    _calendar_button_css = '#dateOfBirthInput'
    _calendar_month_combobox_xpath = '//select[@class="react-datepicker__month-select"]'
    _calendar_year_combobox_xpath = '//select[@class="react-datepicker__year-select"]'
    _subject_input_id = 'subjectsInput'
    _upload_picture_id = 'uploadPicture'
    _current_address_input_xpath = '//textarea[@placeholder="Current Address"]'
    _state_select_state_button_xpath = '//div[text()="Select State"]'
    _state_select_id = 'react-select-3-input'
    _state_select_city_button_xpath = '//div[text()="Select City"]'
    _city_select_id = 'react-select-4-input'
    _submit_button_id = 'submit'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait( self.driver, 10)

    def fill_form(self, first_name, last_name, email, gender, mobile_phone):
        self.driver.find_element_by_xpath(self._first_name_input_xpath).send_keys(first_name)
        self.driver.find_element_by_xpath(self._last_name_input_xpath).send_keys(last_name)
        self.driver.find_element_by_xpath(self._email_input_xpath).send_keys(email)
        if gender == "Male":
            self.driver.find_element_by_xpath(self._male_radio_button_xpath).click()
        self.driver.find_element_by_xpath(self._mobile_phone_input_xpath).send_keys(mobile_phone)

    def select_date_in_calendar(self, day, month, year):
        self.driver.find_element_by_css_selector(self._calendar_button_css).click()
        self.driver.find_element_by_xpath(self._calendar_month_combobox_xpath).click()
        select_month = Select(self.driver.find_element_by_xpath(self._calendar_month_combobox_xpath))
        select_month.select_by_visible_text(month)
        select_year = Select(self.driver.find_element_by_xpath(self._calendar_year_combobox_xpath))
        select_year.select_by_visible_text(year)
        xpath_day = '//div[@class="react-datepicker__day react-datepicker__day--0' + day + '"]'
        self.driver.find_element_by_xpath(xpath_day).click()
        time.sleep(1)

    def fill_subjects_field(self, text):
        subject_element = self.wait.until(EC.element_to_be_clickable((By.ID, self._subject_input_id)))
        subject_element.click()
        time.sleep(1)
        subject_element.send_keys(text)
        time.sleep(1)

    def go_to_automation_practice_form_page(self):
        self.driver.get("https://demoqa.com/automation-practice-form")

    def upload_beer(self):
        self.driver.find_element_by_id(self._upload_picture_id).send_keys(os.path.abspath("images/beer.jpg"))

    def fill_current_address_field(self, text):
        self.driver.find_element_by_xpath(self._current_address_input_xpath).send_keys(text)

    def select_state_and_city(self, state, city):
        self.driver.find_element_by_xpath(self._state_select_state_button_xpath).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, self._state_select_id))).send_keys(state)
        self.wait.until(EC.element_to_be_clickable((By.ID, self._state_select_id))).send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_xpath(self._state_select_city_button_xpath).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, self._city_select_id))).send_keys(city)
        self.wait.until(EC.element_to_be_clickable((By.ID, self._city_select_id))).send_keys(Keys.ENTER)

    def click_submit_button(self):
        self.driver.find_element_by_id(self._submit_button_id).click()

