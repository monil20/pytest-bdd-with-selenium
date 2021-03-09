import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


# Scenarios
scenarios("../features/web.feature")


# Given Steps
@given("the DuckDuckGo home page is displayed")
def ddg_home(browser):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()


# When Steps
@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.search(phrase)


# Then Steps
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, asserts, phrase):
    result_page = DuckDuckGoResultPage(browser)
    asserts.assertGreater(result_page.link_div_count(), 0)
    asserts.assertGreater(result_page.phrase_result_count(phrase), 0)
    asserts.assertEqual(result_page.search_input_value(), phrase)
