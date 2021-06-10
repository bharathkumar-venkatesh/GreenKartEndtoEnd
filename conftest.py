import pytest
from selenium import webdriver


@pytest.fixture()
def browser_init(request):
    driver = webdriver.Chrome(executable_path="/Users/bharathkumarv/Desktop/Drivers for Selenium/chromedriver")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
