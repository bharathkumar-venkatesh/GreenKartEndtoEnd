from selenium.webdriver.common.by import By

from GreenKartEndtoEnd.PageObjects.CheckoutPage.CheckoutPage import CheckoutPage


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
    search = (By.CSS_SELECTOR, "input.search-keyword")

    # self.driver.find_element_by_css_selector("button.search-button").click()
    searchicon = (By.CSS_SELECTOR, "button.search-button")

    # self.driver.find_elements_by_xpath("//div[@class='product-action']/button")
    add_to_cart = (By.XPATH, "//div[@class='product-action']/button")

    # self.driver.find_element_by_xpath("//img[@alt='Cart']").click()
    cart = (By.XPATH, "//img[@alt='Cart']")

    # self.driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
    Proceed = (By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")

    def search_bar(self):
        return self.driver.find_element(*HomePage.search)

    def search_icon(self):
        return self.driver.find_element(*HomePage.searchicon)

    def add_to_cart_button(self):
        return self.driver.find_elements(*HomePage.add_to_cart)

    def cart_button(self):
        return self.driver.find_element(*HomePage.cart)

    def proceed_to_checkout(self):
        self.driver.find_element(*HomePage.Proceed).click()
        Checkout_Page = CheckoutPage(self.driver)
        return Checkout_Page
