from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# chrome
import os, time
from selenium import webdriver
cwd = os.getcwd() + '/'
driver = webdriver.Chrome('C:/Users/ak66h_000/Downloads/chromedriver.exe')
driver.get("http://127.0.0.1:5000/")
driver.get("http://127.0.0.1:8080/")

# opera
from selenium import webdriver
from selenium.webdriver.chrome import service
webdriver_service = service.Service('C:/Users/ak66h_000/Downloads/operadriver.exe')
webdriver_service.start()
driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
driver.get("http://127.0.0.1:8080/")

checkboxs = driver.find_elements_by_name('cols')
for checkbox in checkboxs:
    print(checkbox.get_attribute("value"))
	checkbox.click()

driver.get("http://127.0.0.1:5000/")
driver.find_element_by_xpath("//a[@href='#tabs-9']").click()
driver.find_element_by_xpath("//input[@id='sel']").click()

driver.get("http://127.0.0.1:8080/")
driver.get("http://127.0.0.1:5000/")
driver.find_element_by_xpath("//input[@value='forweb']").click()
driver.find_element_by_xpath("//input[@value='Show fields']").click()
driver.find_element_by_xpath("//button[text()='開盤價']").click()
driver.find_element_by_xpath("//button[text()='收盤價']").click()
driver.find_element_by_xpath("//input[@value='query']").click()

driver.get("http://127.0.0.1:8080/hi")
driver.get("http://127.0.0.1:5000/")
driver.find_element_by_xpath("//a[@href='#tabs-11']").click()

driver.get("http://127.0.0.1:5000/")
driver.get("http://127.0.0.1:5000/react")
driver.get("http://127.0.0.1:5000/")
driver.get("http://127.0.0.1:5000/testajax")

'`開盤價`'.encode()

from urllib import parse
parse.unquote('`%E9%96%8B%E7%9B%A4%E5%83%B9`')
parse.quote_plus('開盤價')
