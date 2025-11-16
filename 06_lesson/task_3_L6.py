from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#3) Дождаться картинки
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html") #переход на сайт

wait = WebDriverWait(driver, 40)
wait.until(EC.presence_of_element_located((By.ID, "landscape")))# загрузка картинок

images = driver.find_elements(By.TAG_NAME, "img")

third_image_src = images[2].get_attribute("src")

print(third_image_src)

driver.quit()