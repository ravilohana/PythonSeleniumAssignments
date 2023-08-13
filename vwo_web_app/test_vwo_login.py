import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


# $Indkabang$@2023
# ravilohana09@gmail.com
@pytest.fixture
def chrom_options():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("start-maximized")
    return options


# Let us Create an object
logging.getLogger().addHandler(logging.StreamHandler())
logger = logging.getLogger(__name__)
# Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


def test_login_vwo_valid_credentials(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    logger.info("Browser Launched")
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(By.ID, "login-username").send_keys("ravilohana09@gmail.com")
    logger.info("Username entered")
    driver.find_element(By.ID, "login-password").send_keys("$Indkabang$@2023")
    logger.info("Password entered")
    driver.find_element(By.ID, "js-login-btn").click()
    logger.info("Login button clicked")
    time.sleep(3)
    print(driver.title)
    assert driver.title in "Dashboard"
    logger.info("Assertion Successfully Done!!")
    time.sleep(3)
    driver.quit()


def test_login_vwo_invalid_credentials(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(By.ID, "login-username").send_keys("ravilohana109@gmail.com")
    driver.find_element(By.ID, "login-password").send_keys("$Indkabang$@2023")
    driver.find_element(By.ID, "js-login-btn").click()
    expected_error_notification = "Your email, password, IP address or location did not match"
    time.sleep(3)
    actual_error_notification = driver.find_element(By.ID, "js-notification-box-msg").text
    print("Actual: ", actual_error_notification)
    time.sleep(3)
    assert actual_error_notification == expected_error_notification
    logger.info("Assertion of error notification Successfully Done!!")
    time.sleep(3)
    driver.quit()
