from selenium.webdriver.common.by import By

from GreenKartEndtoEnd.PageObjects.ConfimrationPage.CofirmationPage import ConfirmationPage


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
    promocode = (By.CSS_SELECTOR, "input.promoCode")

    # self.driver.find_element_by_css_selector("button.promoBtn").click()
    promobtn = (By.CSS_SELECTOR, "button.promoBtn")

    # self.driver.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()
    place_order = (By.XPATH, "//button[contains(text(),'Place Order')]")

    def promo_code(self):
        return self.driver.find_element(*CheckoutPage.promocode)

    def promo_button(self):
        return self.driver.find_element(*CheckoutPage.promobtn)

    def place_order_button(self):
        self.driver.find_element(*CheckoutPage.place_order).click()
        Confirmation_page = ConfirmationPage(self.driver)
        return Confirmation_page
