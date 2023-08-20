
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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


def test_actions_dropdown(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    logger.info("Browser Launched")
    driver.get("https://awesomeqa.com/selenium/action_dropdown.html")
    dropdown = driver.find_element(By.ID,"dropdownMenuButton1")
    actions = ActionChains(driver)
    actions.move_to_element(dropdown).click().send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()


