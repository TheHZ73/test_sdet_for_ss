import pytest
from selenium import webdriver


class Common:
    driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        if self.driver is not None:
            self.driver.close()
