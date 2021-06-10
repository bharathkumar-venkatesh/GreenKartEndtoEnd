import time

import pytest

from GreenKartEndtoEnd.BaseClass.BaseClass import BaseClass
from GreenKartEndtoEnd.PageObjects.HomePage.HomePage import HomePage
from GreenKartEndtoEnd.TestData.HomePageData import HomePageData


class Test_End_to_End(BaseClass):
    def test_End_to_End(self, data_load):
        log = self.getLogger()
        # self.driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
        Home_Page = HomePage(self.driver)
        log.info("Homepage loaded")
        Home_Page.search_bar().send_keys(data_load["vegetable_name"])
        log.info("Searching veggies" + " " + data_load["vegetable_name"])
        # self.driver.find_element_by_css_selector("button.search-button").click()
        Home_Page.search_icon().click()
        time.sleep(3)
        # self.driver.find_elements_by_xpath("//div[@class='product-action']/button")
        listed_veggies = Home_Page.add_to_cart_button()

        for veggie in listed_veggies:
            veggie.click()

        # self.driver.find_element_by_xpath("//img[@alt='Cart']").click()
        Home_Page.cart_button().click()
        # self.driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
        Checkout_Page = Home_Page.proceed_to_checkout()
        log.info("Moving to checkout page")

        # CheckoutPage
        time.sleep(3)
        # self.driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
        Checkout_Page.promo_code().send_keys(data_load["promocode"])
        log.info("entered promocode")

        # self.driver.find_element_by_css_selector("button.promoBtn").click()
        Checkout_Page.promo_button().click()
        self.driver.implicitly_wait(5)

        # self.driver.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()
        Confirmation_page = Checkout_Page.place_order_button()

        # ConfirmationPage
        self.driver.implicitly_wait(5)
        # self.driver.find_elements_by_xpath("//div[@class='wrapperTwo']/div/select")
        countries = Confirmation_page.country_dropdown()
        for country in countries:
            if country.text == data_load["country_name"]:
                country.click()
        log.info("Country selected")
        # self.driver.find_element_by_css_selector("input.chkAgree").click()
        Confirmation_page.check_box().click()
        # self.driver.find_element_by_xpath("//button[contains(text(),'Proceed')]").click()
        Confirmation_page.proceed_button().click()

    @pytest.fixture(params=HomePageData.test_Data_Homepage)
    def data_load(self, request):
        return request.param
