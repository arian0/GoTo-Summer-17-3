from selenium import webdriver
import lxml.html as html


desired_capabilities = webdriver.DesiredCapabilities.PHANTOMJS.copy()
driver = webdriver.PhantomJS(desired_capabilities=desired_capabilities)
driver.get('https://ru.dotabuff.com/heroes/abaddon')
print(driver.page_source)
