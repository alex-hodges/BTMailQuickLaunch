from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://home.bt.com/login/loginform?TARGET=$SM$https%3A%2F%2Fsignin1.bt.com%2Fbtmail%2Fsecure%2Femaillogin")
instructionUser = driver.find_element(By.NAME, "USER")
instructionUser.send_keys("")  # ! INSERT EMAIL ADDRESS
instructionPWD = driver.find_element(By.NAME, "NAFMPASSWORD")
instructionPWD.send_keys("")  # ! INSERT PASSWORD
instructionPWD.submit()
