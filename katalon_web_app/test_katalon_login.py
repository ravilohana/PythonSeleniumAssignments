

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.select import Select



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


def test_login_katalon_demo_make_appointment(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    logger.info("Browser Launched")
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.find_element(By.ID, "btn-make-appointment").click()
    driver.find_element(By.NAME, "username").send_keys("John Doe")
    logger.info("Username entered")
    driver.find_element(By.NAME, "password").send_keys("ThisIsNotAPassword")
    logger.info("Password entered")
    driver.find_element(By.ID, "btn-login").click()
    logger.info("Login Successfully Done")
    select_facility = driver.find_element(By.XPATH, "//select[@name='facility']")
    select = Select(select_facility)
    select.select_by_visible_text("Seoul CURA Healthcare Center")
    driver.find_element(By.ID, "radio_program_medicaid").click()
    driver.find_element(By.ID, "txt_visit_date").send_keys("15/08/2023")
    driver.find_element(By.ID, "txt_comment").send_keys("This is dummy comment for make appointment for health care")
    logger.info("All Queries for appointment Done")
    driver.find_element(By.ID, "btn-book-appointment").click()
    actual_appointment_cnf_heading = driver.find_element(By.TAG_NAME,"h2").text
    expected_appointment_cnf_heading = "Appointment Confirmation"
    assert actual_appointment_cnf_heading == expected_appointment_cnf_heading
    logger.info("Asserted heading Appointment Confirmation")
    driver.quit()



