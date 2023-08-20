# Automation Challenge: Finding and Deleting Terminated Employees in Web Tables
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


def test_emp_terminate_job_status(chrom_options):
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
    time.sleep(5)
    emp_rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/child::div")
    emp_rows_len = len(emp_rows)
    print(emp_rows_len)
    emp_cols = driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div[1]/div/div")
    emp_cols_len = len(emp_cols)
    print(emp_cols_len)
    first_part = "//div[@role='table']/div[2]/div["
    second_part = "]/div/div["
    third_part = "]"
    employee_status = None
    employee_name = 'Aman'
    for i in range(1, emp_rows_len + 1):  # range(1,10) -> 1, 9+1)
        for j in range(1, emp_cols_len + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if employee_name in data:
                employee_status_path = f"{dynamic_path}/following-sibling::div[3]"
                employee_status = driver.find_element(By.XPATH, employee_status_path).text
                print(f"{employee_name} employee status is  {employee_status}")
                if employee_status == "Terminated":
                    edit_employee_status_path = f"{dynamic_path}//following-sibling::div/div/button[1]"
                    driver.find_element(By.XPATH, edit_employee_status_path).click()
                break
