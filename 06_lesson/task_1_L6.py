from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#1) Нажать на кнопку
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/ajax") #переход на сайт

blue_botton = driver.find_element (By.CSS_SELECTOR, '#ajaxButton').click()

content = driver.find_element(By.CSS_SELECTOR, "#content")#ищем элемент с id="content"

txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text#собираем текст из элемента с тегом p и class="bg-success"
#через элеменет в content

print(txt)

driver.quit()
