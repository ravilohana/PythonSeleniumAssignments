import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



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
    driver.find_element(By.ID, "login-username").send_keys("93npu2yyb0@esiix.com")
    logger.info("Username entered")
    driver.find_element(By.ID, "login-password").send_keys("Wingify@123")
    logger.info("Password entered")
    driver.find_element(By.ID, "js-login-btn").click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-heading']")))
    logger.info("Login button clicked")
    assert driver.title in "Dashboard"
    logger.info("Assertion Successfully Done!!")
    driver.quit()


def test_login_vwo_invalid_credentials(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(By.ID, "login-username").send_keys("93npu2yyb0@esiix.com")
    driver.find_element(By.ID, "login-password").send_keys("Wingify@12345")
    driver.find_element(By.ID, "js-login-btn").click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                     ".login-wrap #js-notification-box-msg")))
    expected_error_notification = "Your email, password, IP address or location did not match"
    actual_error_notification = driver.find_element(By.CSS_SELECTOR, ".login-wrap #js-notification-box-msg").text
    print("Actual: ", actual_error_notification)
    assert actual_error_notification == expected_error_notification
    logger.info("Assertion of error notification Successfully Done!!")
    driver.quit()
