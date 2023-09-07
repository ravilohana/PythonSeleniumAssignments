import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver
    time.sleep(4)
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_emp_field_edit(driver):
    faker = Faker()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("Hacker@4321")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert driver.title in "OrangeHRM"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']")))
    driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
    time.sleep(4)
    emp_first_name = f"{faker.first_name()}"
    emp_middle_name = f"mid name {faker.random_digit()}"
    emp_last_name = f"{faker.last_name()}"

    driver.find_element(By.NAME, "firstName").send_keys(emp_first_name)
    driver.find_element(By.NAME, "middleName").send_keys(emp_middle_name)
    driver.find_element(By.NAME, "lastName").send_keys(emp_last_name)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-form-actions']//button["
                                                                          "@type='submit']")))
    driver.find_element(By.XPATH, "//div[@class='oxd-form-actions']//button[""@type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//nav[@role='navigation']/ul/li/a[text()='Employee List']")))

    driver.find_element(By.XPATH, "//nav[@role='navigation']/ul/li/a[text()='Employee List']").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")))

    driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]").send_keys(emp_last_name)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='listbox']/div/span")))
    emp_name_search_list = driver.find_elements(By.XPATH, "//div[@role='listbox']/div/span")

    # print(emp_name_search_list)
    print([ele_txt.text for ele_txt in emp_name_search_list])
    for emp_name in emp_name_search_list:
        # WebDriverWait(driver,10).until(EC.staleness_of(emp_name))
        print(emp_name.text)
        if emp_name.text == emp_first_name + " " + emp_middle_name + " " + emp_last_name:
            emp_name.click()
            break

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-form-actions']/button[@type='submit']")))

    driver.find_element(By.XPATH, "//div[@class='oxd-form-actions']/button[@type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']")))
    driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//form[@class='oxd-form']/div[2]/div/div/div/div[2]/input)[2]")))
    order_id_field = driver.find_element(By.XPATH, "(//form[@class='oxd-form']/div[2]/div/div/div/div[2]/input)[2]")
    order_id_field.click()
    order_id_field.send_keys("YES")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-form-actions']/button[@type='submit']")))

    driver.find_element(By.XPATH, "//div[@class='oxd-form-actions']/button[@type='submit']").click()

    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'oxd-text--toast-title')]")))
    success_title = driver.find_element(By.XPATH, "//p[contains(@class,'oxd-text--toast-title')]")
    assert success_title.text == "Success"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'oxd-text--toast-message')]")))
    success_msg = driver.find_element(By.XPATH, "//p[contains(@class,'oxd-text--toast-message')]")
    assert success_msg.text == "Successfully Updated"

