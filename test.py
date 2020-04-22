from selenium import webdriver
from selenium import webdriver

browser = webdriver.Firefox(executable_path="C:\VM\geckodriver.exe")

browser.get("http://localhost/vmxid_api/public/lapangan-tembak") #this will load the the google homepage. 
results = browser.find_elements_by_class_name('card-body')
email = browser.find_element_by_id("email")
email.clear()
email.send_keys("admin@gmail.com")
password = browser.find_element_by_id("password")
password.clear()
password.send_keys("12345678")
browser.find_element_by_class_name("btn-info").click();
print(results[0].text)

#you can specify any page you want here.
# driver.close()

# driver = webdriver.Chrome(r'C:\VM\chromedriver.exe')
# driver.maximize_window()
# driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
# assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title

# eleUserMessage = driver.find_element_by_id("user-message")
# eleUserMessage.clear()
# eleUserMessage.send_keys("Test Python")

# eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
# eleShowMsgBtn.click()

# eleYourMsg=driver.find_element_by_id("display")
# assert "Test Python" in eleYourMsg.text
# driver.close()