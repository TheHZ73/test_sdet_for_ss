# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PracticeFormModalWindow:
    _title_modal_size_id = 'example-modal-sizes-title-lg'
    _student_name_value_xpath = '//td[text()="Student Name"]/following::td[1]'
    _student_email_value_xpath = '//td[text()="Student Email"]/following::td[1]'
    _gender_value_xpath = '//td[text()="Gender"]/following::td[1]'
    _mobile_phone_value = '//td[text()="Mobile"]/following::td[1]'
    _date_of_birth_value_xpath = '//td[text()="Date of Birth"]/following::td[1]'
    _subjects_value_xpath = '//td[text()="Subjects"]/following::td[1]'
    _picture_value_text_xpath = '//td[text()="Picture"]/following::td[1]'
    _address_value_xpath = '//td[text()="Address"]/following::td[1]'
    _state_and_city_value_xpath = '//td[text()="State and City"]/following::td[1]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_download_page(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self._title_modal_size_id)))
        time.sleep(1)

    def checking_form_completion(self, text_title, first_name, last_name, email, gender, phone, date_of_birth, subjects,
                                 picture_text, address, state, city):
        check_text_title = self.driver.find_element_by_id(self._title_modal_size_id).text
        assert (check_text_title == text_title), "не ожидаемый заголовок"
        assert (self.driver.find_element_by_xpath(self._student_name_value_xpath).text == (first_name + " " + last_name))
        assert (self.driver.find_element_by_xpath(self._student_email_value_xpath).text == email)
        assert (self.driver.find_element_by_xpath(self._gender_value_xpath).text == gender)
        assert (self.driver.find_element_by_xpath(self._mobile_phone_value).text == phone)
        assert (self.driver.find_element_by_xpath(self._date_of_birth_value_xpath).text == date_of_birth)
        subject_text_page = self.driver.find_element_by_xpath(self._subjects_value_xpath).text
        assert (subject_text_page == subjects), \
            f"поле Subjects заполнено не ожидаемой строкой - {subject_text_page}, ожидаемая строка - {subjects}"
        assert (self.driver.find_element_by_xpath(self._picture_value_text_xpath).text == picture_text)
        assert (self.driver.find_element_by_xpath(self._address_value_xpath).text == address)
        assert (self.driver.find_element_by_xpath(self._state_and_city_value_xpath).text == (state + " " + city))


