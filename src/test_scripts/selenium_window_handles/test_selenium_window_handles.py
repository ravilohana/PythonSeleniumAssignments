import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver
    time.sleep(4)
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_selenium_window_handle_wikipedia_txt_box(driver):
    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    driver.get("https://testautomationpractice.blogspot.com/")
    wikipedia_txt_box = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
    wikipedia_txt_box.send_keys("selenium")

    # Store the ID of the original window
    original_window = driver.current_window_handle
    print("Original window ID: ", original_window)

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    wikipedia_search_icon = driver.find_element(By.CSS_SELECTOR, ".wikipedia-search-button")
    wikipedia_search_icon.click()

    wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']//div//a")))

    wikipedia_search_results = driver.find_elements(By.XPATH,
                                                    "//div[@id='Wikipedia1_wikipedia-search-results']//div//a")
    print([x.text for x in wikipedia_search_results])
    for search_results in wikipedia_search_results:
        print(search_results.text)
        search_results.click()

    window_ids = driver.window_handles
    print(window_ids)

    for window_id in window_ids:
        driver.switch_to.window(window_id)
        print(f"window id: {window_id} | current url:  {driver.current_url} | title of page: {driver.title}")
