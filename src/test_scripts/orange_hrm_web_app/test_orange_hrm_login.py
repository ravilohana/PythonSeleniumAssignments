import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.test_scripts.logging_core import logger



@pytest.fixture
def chrom_options():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("start-maximized")
    return options


# # Let us Create an object
# logging.getLogger().addHandler(logging.StreamHandler())
# logger = logging.getLogger('__name__')
# # Now we are going to Set the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)


def test_orange_hrm_login_valid_credentials(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    logger.info("Browser Launched")
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys("admin")
    logger.info("Username entered")
    driver.find_element(By.NAME, "password").send_keys("Hacker@4321")
    logger.info("Password entered")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    logger.info("Login button clicked")
    assert driver.title in "OrangeHRM"
    logger.info("Assertion Successfully Done!!")
    driver.quit()



