from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest

@pytest.fixture #global function to open site
def driver():
    driver = webdriver.Chrome()  # run test on Chrome
    bank_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/"  # set bank_url
    driver.get(bank_url)  # open site on Chrome
    time.sleep(3)
    return driver

#negative test on user (Harry Potter) and target_count (=1)
#========TEST 1===================================
@pytest.mark.parametrize("user, target_count",[("Harry Potter", 1)]) #("Hermoine Granger",392)
def test_users_transactions(user, target_count, driver):    #test function
    element = driver.find_element(By.XPATH,'//button[text()="Customer Login"]') #find button Login
    element.click()                #click button Login
    time.sleep(3)
    element = driver.find_element(By.ID,"userSelect")   #find drop down
    drop=Select(element)
    drop.select_by_visible_text(user)
    element = driver.find_element(By.XPATH, '//button[text()="Login"]')
    element.click()
    time.sleep(3)
    element = driver.find_element(By.ID, "accountSelect")
    drop = Select(element)
    count = len(drop.options)
    totalRows = 0
    for i in range(count):    #loop
        drop.select_by_index(i)
        time.sleep(1)
        element = driver.find_element(By.XPATH, '//button[@ng-click="transactions()"]')   #search by ng-click
        element.click()
        time.sleep(2)
        #find transactions
        rows = driver.find_elements(By.XPATH, '//table/tbody/tr')
        cnt = len(rows)
        totalRows = totalRows + cnt
        if (totalRows > target_count):
            break
        if i<count-1:
            element = driver.find_element(By.XPATH, '//button[text()="Back"]')
            element.click()
            time.sleep(1)
            element = driver.find_element(By.ID, "accountSelect")
            drop = Select(element)
    assert totalRows == target_count

#========TEST 2===================================
@pytest.mark.parametrize("user",[("Harry Potter")]) #("Hermoine Granger")
def test_customer_deposit_numbers_only(user,driver):    #- כנס למערכת כיוזר בדוק שהשדה של הפקדת כסף אינו מקסל ערכים טקסטואלים רק מספרים
    element = driver.find_element(By.XPATH, '//button[text()="Customer Login"]')  # find button Login
    element.click()  # click button Login
    time.sleep(3)
    element = driver.find_element(By.ID, "userSelect")  # find drop down
    drop = Select(element)
    drop.select_by_visible_text(user)
    element = driver.find_element(By.XPATH, '//button[text()="Login"]')
    element.click()
    time.sleep(3)
    element = driver.find_element(By.ID, "accountSelect")
    drop = Select(element)
    element = driver.find_element(By.XPATH, '//button[@ng-click="deposit()"]') #search by ng-click
    element.click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//input[@ng-model="amount"]')  # search by ng-model
    element.send_keys("a")
    time.sleep(2)
    val = element.get_attribute("value")
    assert val == ""

    element.send_keys("@#")
    time.sleep(2)
    val = element.get_attribute("value")
    assert val == ""

    element.send_keys("=")
    time.sleep(2)
    val = element.get_attribute("value")
    assert val == ""

#========TEST 3===================================
def test_add_customer_without_first_name(driver): #בדוק שהמערכת לא נותנת להוסיף לקוח חדש ללא שם פרטי
    element = driver.find_element(By.XPATH, '//button[text()="Bank Manager Login"]')
    element.click()  # click button Login
    time.sleep(3)


    element = driver.find_element(By.XPATH, '//button[@ng-click="showCust()"]')
    element.click()
    time.sleep(2)

    rows = driver.find_elements(By.XPATH, '//table/tbody/tr')
    cnt = len(rows)
    element = driver.find_element(By.XPATH, '//button[@ng-click="addCust()"]')  # search by ng-click
    element.click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//input[@ng-model="lName"]')  # search by ng-model
    element.send_keys("נאמנות אברהם")
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//input[@ng-model="postCd"]')  # search by ng-model
    element.send_keys("32290")
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//button[text()="Add Customer"]')
    element.click()  # click button Add Customer
    time.sleep(3)
    element = driver.find_element(By.XPATH, '//button[@ng-click="showCust()"]')
    element.click()
    time.sleep(2)

    rows = driver.find_elements(By.XPATH, '//table/tbody/tr')
    cnt2 = len(rows)
    assert cnt==cnt2






