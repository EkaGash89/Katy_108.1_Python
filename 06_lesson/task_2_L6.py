from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#2) Переименовать кнопку
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(30)

driver.maximize_window()
driver.get("http://uitestingplayground.com/textinput") #переход на сайт
pole_voda = driver.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

button_text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
    
print(button_text)  # Выведет "SkyPr

driver.quit()




