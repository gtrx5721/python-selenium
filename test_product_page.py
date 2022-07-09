import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
# def test_guest_cant_see_success_message_after_adding_product_to_basket(
#         browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/" \
#            "coders-at-work_207"
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.add_to_basket()
#     page.should_not_be_success_message()


# def test_user_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/" \
#            "coders-at-work_207"
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.should_not_be_success_message()
    
    
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/" \
#            "coders-at-work_207"
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.add_to_basket()
#     page.should_be_success_message_disappeared()