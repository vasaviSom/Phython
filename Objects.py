
from selenium.webdriver.common import keys
from selenium import webdriver
import time
class Objects:
    
 def Login(self,a, b):
    "this"
    driver=webdriver.Chrome(executable_path=r"C:\Users\dell\Downloads\chromedriver.exe")
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    inputElement = driver.find_element_by_link_text("Sign in")
    inputElement.click()
    time.sleep(10)
    inputElement = driver.find_element_by_id('email')
    inputElement.send_keys(a)
    inputElement = driver.find_element_by_id('passwd')
    inputElement.send_keys(b)
    inputElement = driver.find_element_by_id('SubmitLogin')
    inputElement.click()
    try:
      if (driver.find_element_by_id('SubmitLogin')):
       print ('Failed')
       return False
    except:
       print ('Passed') 
       return True
   
   
   
   
   
   
    
    
 

    
   


