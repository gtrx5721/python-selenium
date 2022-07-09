import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    
    # time.sleep(20000)
    page.should_be_equal_product_name_and_product_added_to_basket()
    page.should_be_equal_product_price_and_basket_value()