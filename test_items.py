from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_available_button_add_basket(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "Button not available!"

