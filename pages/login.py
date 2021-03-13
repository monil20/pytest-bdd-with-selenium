"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "file:///Users/monilandharia/Downloads/Serenity%20COVID.html"

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[primary='true']")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot password?")

    def __init__(self, browser):
        self.browser = browser

    @property
    def email_input(self):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.EMAIL_INPUT)
        )

    @property
    def password_input(self):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        )

    @property
    def login_button(self):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.LOGIN_BUTTON)
        )

    @property
    def forgot_password_link(self):
        return WebDriverWait(self.browser, 10).until(self.FORGOT_PASSWORD_LINK)

    def load(self):
        self.browser.get(self.URL)
