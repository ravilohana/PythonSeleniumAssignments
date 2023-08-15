import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.test_scripts.logging_core import logger


@pytest.fixture
def chrom_options():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("start-maximized")
    return options


def test_ebay_items_list(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    driver.get("https://www.ebay.com/b/PC-Desktops-All-In-One-Computers/179/bn_661752")
    driver.find_element(By.XPATH
                        , "//section[contains(@class,'b-guidance b-display--landscape')]//span[contains(text(),"
                          "'See All')]").click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='ABS Computer Technologies']")))
    driver.find_element(By.XPATH, "//span[text()='ABS Computer Technologies']").click()
    driver.find_element(By.XPATH, "//button[@aria-label='Apply']").click()

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='srp-controls']//button)[2]")))

    button_view = driver.find_element(By.XPATH, "(//div[@class='srp-controls']//button)[2]").get_attribute("aria-label")
    print(button_view)
    if button_view == "View: Gallery View":
        WebDriverWait(driver, 15).until(EC.staleness_of(driver.find_element
                                                        (By.XPATH, "(//div[@class='srp-controls']//button)[2]")))
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable
                                        (driver.find_element(By.XPATH, "(//div[@class='srp-controls']//button)[2]")))
        driver.find_element(By.XPATH, "(//div[@class='srp-controls']//button)[2]").click()
        driver.find_element(By.XPATH, "//ul[@class='fake-menu__items']//li//a//span[text()='List View']").click()

    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='b-list__items_nofooter"
                                                                                "']//li//h3")))

    ebay_items_list = driver.find_elements(By.XPATH, "//ul[@class='b-list__items_nofooter']//li//h3")
    items_list = []
    for item_list in ebay_items_list:
        items_list.append(item_list.text)

    print(items_list)
    print(len(items_list))

    driver.quit()
