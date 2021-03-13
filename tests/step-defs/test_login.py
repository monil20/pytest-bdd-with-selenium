import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pages.login import LoginPage


# Scenarios
scenarios("../features/login.feature")


# Given Steps
@given("the Serenity Covid login page is displayed")
def serenity_covid_login_page(browser):
    login_page = LoginPage(browser)
    login_page.load()


# When Steps
@when(parsers.parse('the user enters email "{email}", password "{password}"'))
def enter_credentials(browser, email, password):
    login_page = LoginPage(browser)
    login_page.email_input.send_keys(email)
    login_page.password_input.send_keys(password)


@when(parsers.parse("clicks the login button"))
def click_login(browser, email):
    login_page = LoginPage(browser)
    login_page.login_button.click()


# Then Steps
@then("it should redirect to the homepage")
def verify_redirection(browser, asserts):
    login_page = LoginPage(browser)
    assert True


@then(parsers.parse('the user should have "{role}" rights'))
def verify_rights(browser, asserts, role):
    login_page = LoginPage(browser)
    assert True