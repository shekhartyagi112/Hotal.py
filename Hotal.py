from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.ixigo.com/")
driver.find_element(By.XPATH,"//span[contains(text(),'Hotels')]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@aria-label='Dismiss sign-in info.']//span[@class='b6dc9a9e69 e25355d3ee']//*[name()='svg']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='ss']").send_keys("New Delhi")
driver.find_element(By.XPATH," //span[normalize-space()='New Delhi']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//span[contains(@aria-label,'30 April 2023')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[@aria-label='2 May 2023']//span[@aria-hidden='true'][normalize-space()='2']").click()
time.sleep(2)
driver.find_element(By.ID,"xp__guests__toggle").click()
driver.find_element(By.XPATH,"//button[@aria-label='Decrease number of Adults']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[contains(@aria-label,'Increase number of Children')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='xp__guests__inputs-container']/div/div/div[3]/select/option[5]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.close()