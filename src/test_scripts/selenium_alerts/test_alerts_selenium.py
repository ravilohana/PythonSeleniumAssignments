import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
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
def test_selenium_js_alerts(driver):
    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    driver.get("https://testautomationpractice.blogspot.com/")
    js_alert_ele = driver.find_element(By.XPATH,
                                       "//div[@id='HTML9']//div[@class='widget-content']/button[text()='Alert']")
    js_alert_ele.click()
    alert = wait.until(EC.alert_is_present())
    js_alert_text = alert.text
    print("\nJS alert text: ", js_alert_text)
    alert.accept()


@pytest.mark.usefixtures("driver")
def test_selenium_js_confirm_box(driver):
    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    driver.get("https://testautomationpractice.blogspot.com/")
    js_confirm_ele = driver.find_element(By.XPATH,
                                         "//div[@id='HTML9']//div[@class='widget-content']/button[text()='Confirm Box']")
    js_confirm_ele.click()
    wait.until(EC.alert_is_present())
    js_confirm = driver.switch_to.alert
    js_confirm_text = js_confirm.text
    print("\nJS Confirm alert text: ", js_confirm_text)

    # accept() if user click on OK button
    js_confirm.accept()

    after_click_js_cnf_text = driver.find_element(By.ID, "demo")
    print("After click on confirm alert response text: ", after_click_js_cnf_text.text)

    assert after_click_js_cnf_text.text == "You pressed OK!"

    # dismiss() if user click on Cancel button
    # if want to test cancel functionality then uncomment this
    # js_confirm.dismiss()
    # assert after_click_js_cnf_text.text == "You pressed Cancel!"


@pytest.mark.usefixtures("driver")
def test_selenium_js_prompt_box(driver):
    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    driver.get("https://testautomationpractice.blogspot.com/")
    js_prompt_ele = driver.find_element(By.XPATH,
                                        "//div[@id='HTML9']//div[@class='widget-content']/button[text()='Prompt']")
    js_prompt_ele.click()
    wait.until(EC.alert_is_present())
    js_prompt = Alert(driver)
    js_prompt_text = js_prompt.text
    print("\nJS Confirm alert text: ", js_prompt_text)

    prompt_box_user_text = "Selenium"
    js_prompt.send_keys(prompt_box_user_text)

    # accept() if user click on OK button
    js_prompt.accept()

    after_click_js_prompt = driver.find_element(By.ID, "demo")
    print("After click on prompt alert response text: ", after_click_js_prompt.text)

    assert after_click_js_prompt.text in f"Hello {prompt_box_user_text}! How are you today?"

    # dismiss() if user click on Cancel button
    # if want to test cancel functionality then uncomment this
    # js_prompt.dismiss()
    # after_click_js_prompt = driver.find_element(By.ID, "demo")
    # print("After click on prompt alert response text: ", after_click_js_prompt.text)
    # assert after_click_js_prompt.text == "User cancelled the prompt."
