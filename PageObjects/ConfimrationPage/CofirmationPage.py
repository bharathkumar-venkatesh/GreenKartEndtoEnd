from selenium.webdriver.common.by import By


class ConfirmationPage():
    def __init__(self, driver):
        self.driver= driver

    # self.driver.find_elements_by_xpath("//div[@class='wrapperTwo']/div/select")
    countries= (By.XPATH, "//div[@class='wrapperTwo']/div/select")

    # self.driver.find_element_by_css_selector("input.chkAgree").click()
    checkbox= (By.CSS_SELECTOR, "input.chkAgree")

    # self.driver.find_element_by_xpath("//button[contains(text(),'Proceed')]").click()
    proceed_btn= (By.XPATH, "//button[contains(text(),'Proceed')]")

    def country_dropdown(self):
        return self.driver.find_elements(*ConfirmationPage.countries)

    def check_box(self):
        return self.driver.find_element(*ConfirmationPage.checkbox)

    def proceed_button(self):
        return self.driver.find_element(*ConfirmationPage.proceed_btn)