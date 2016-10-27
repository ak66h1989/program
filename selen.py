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
# opera
from selenium.webdriver.chrome import service
webdriver_service = service.Service('C:/Users/ak66h_000/Downloads/operadriver.exe')
webdriver_service.start()
driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
driver.get("http://127.0.0.1:5000/")

checkboxs=driver.find_elements_by_name('cols')
for checkbox in checkboxs:
    print(checkbox.get_attribute("value"))
	checkbox.click()

driver.get("http://127.0.0.1:5000/")
driver.find_element_by_xpath("//a[@href='#tabs-9']").click()
driver.find_element_by_xpath("//input[@id='sel']").click()



