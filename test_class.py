# -*- coding: utf-8 -*-
import time

from pages.practice_form import PracticeForm
from common import Common
from pages.practice_form_modal_window import PracticeFormModalWindow
from utils import generate_random_string, generate_random_number


class TestClass(Common):
    def test_filling_out_the_registration_form(self):
        practice_form_page = PracticeForm(self.driver)
        practice_form_page.go_to_automation_practice_form_page()
        first_name = generate_random_string(8)
        last_name = generate_random_string(10)
        email = generate_random_string(12) + "@yandex.ru"
        mobile_phone = generate_random_number(10)
        gender = "Male"
        practice_form_page.fill_form(first_name=first_name, last_name=last_name, email=email, gender=gender,
                                     mobile_phone=mobile_phone)
        practice_form_page.select_date_in_calendar(day="22", month="May", year="1991")
        subjects = generate_random_string(15)
        practice_form_page.fill_subjects_field(subjects)
        practice_form_page.upload_beer()
        current_address = "Ulei, street " + generate_random_string(10) + " flat " + generate_random_number(2)
        practice_form_page.fill_current_address_field(current_address)
        state = 'NCR'
        city = 'Noida'
        practice_form_page.select_state_and_city(state=state, city=city)
        practice_form_page.click_submit_button()

        practice_form_page_modal_window = PracticeFormModalWindow(self.driver)
        practice_form_page_modal_window.wait_download_page()
        title_text_for_check = 'Thanks for submitting the form'
        date_of_birth_for_check = '22 May,1991'
        picture_text_for_check = 'beer.jpg'
        practice_form_page_modal_window. \
            checking_form_completion(text_title=title_text_for_check, first_name=first_name, last_name=last_name,
                                     email=email, gender=gender, phone=mobile_phone, subjects=subjects,
                                     date_of_birth=date_of_birth_for_check, picture_text=picture_text_for_check,
                                     address=current_address, state=state, city=city)
