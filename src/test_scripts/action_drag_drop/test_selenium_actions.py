import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrom_options():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("start-maximized")
    return options


def test_drag_and_drop(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    driver.get("https://automationtesting.co.uk/")
    driver.find_element(By.XPATH, "//nav[@id='menu']//ul/li/a[text()='Actions']").click()
    # Wait for draggable element to be visible
    draggable = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "dragtarget")))

    # Wait for droppable element to be visible
    droppable = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'col-6 col-12-medium')]//div[2]")))
    # draggable = driver.find_element(By.ID, "dragtarget")
    # droppable = driver.find_element(By.XPATH, "//div[contains(@class,'col-6 col-12-medium')]//div[2]")
    time.sleep(5)
    ActionChains(driver).click_and_hold(draggable).move_to_element(droppable).release().perform()


def test_drag_and_drop_1(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    driver.get("https://demo.guru99.com/test/drag_drop.html")
    draggable = driver.find_element(By.XPATH, "//a[normalize-space()='BANK']")
    droppable = driver.find_element(By.XPATH, "//ol[@id='bank']//li[@class='placeholder']")
    ActionChains(driver).drag_and_drop(draggable, droppable).perform()
    draggable_1 = driver.find_element(By.XPATH, "//a[normalize-space()='SALES']")
    droppable_1 = driver.find_element(By.XPATH, "//ol[@id='loan']//li[@class='placeholder']")
    ActionChains(driver).drag_and_drop(draggable_1, droppable_1).perform()
    time.sleep(5)
    driver.quit()


def test_drag_and_drop_3(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    driver.get("https://automationtesting.co.uk/")
    driver.find_element(By.XPATH, "//nav[@id='menu']//ul/li/a[text()='Actions']").click()
    time.sleep(4)
    draggable = driver.find_element(By.ID, "dragtarget")
    start = draggable.location
    finish = driver.find_element(By.XPATH, "//div[contains(@class,'col-6 col-12-medium')]//div[2]").location
    print(finish)
    ActionChains(driver) \
        .drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y']) \
        .perform()


def test_drag_drop_lambda_test(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    driver.get("https://www.lambdatest.com/selenium-playground/drag-and-drop-demo")
    draggable_1 = driver.find_element(By.XPATH, "//div[@id='todrag']//span[text()='Draggable 1']")
    draggable_2 = driver.find_element(By.XPATH, "//div[@id='todrag']//span[text()='Draggable 2']")
    droppable = driver.find_element(By.ID, "mydropzone")

    # ActionChains(driver).drag_and_drop(draggable_1, droppable).perform()
    ActionChains(driver).click_and_hold(draggable_1).move_to_element(droppable).release().perform()
    time.sleep(4)
    # ActionChains(driver).drag_and_drop(draggable_2, droppable).perform()
    ActionChains(driver).click_and_hold(draggable_2).move_to_element(droppable).release().perform()

    draggable_p = driver.find_element(By.CSS_SELECTOR, "#draggable > p")
    droppable_p = driver.find_element(By.CSS_SELECTOR, "#droppable > p")

    time.sleep(3)
    # ActionChains(driver).drag_and_drop(draggable_p, droppable_p).perform()
    ActionChains(driver).click_and_hold(draggable_p).move_to_element(droppable_p).release().perform()


def test_drag_drop_lambda_test_mouse(chrom_options):
    driver = webdriver.Chrome(options=chrom_options)
    driver.get("https://www.lambdatest.com/selenium-playground/drag-and-drop-demo")
    draggable_1 = driver.find_element(By.XPATH, "//div[@id='todrag']//span[text()='Draggable 1']")
    draggable_2 = driver.find_element(By.XPATH, "//div[@id='todrag']//span[text()='Draggable 2']")
    droppable = driver.find_element(By.ID, "mydropzone")

    actions = ActionChains(driver)
    actions.click_and_hold(draggable_1).move_to_element(droppable).release().perform()

    # ActionChains(driver) \
    #     .click_and_hold(draggable_1) \
    #     .click_and_hold(draggable_1) \
    #     .move_to_element(droppable) \
    #     .perform()

    # actions = ActionBuilder(driver)
    # actions.pointer_action.move_to(draggable_1)
    # actions.pointer_action.pointer_down(MouseButton.LEFT)
    # actions.pointer_action.move_to(droppable)
    # actions.pointer_action.pointer_up(MouseButton.LEFT).release()
    # actions.perform()

    time.sleep(4)


    draggable_p = driver.find_element(By.CSS_SELECTOR, "#draggable > p")
    droppable_p = driver.find_element(By.CSS_SELECTOR, "#droppable > p")

    time.sleep(3)

