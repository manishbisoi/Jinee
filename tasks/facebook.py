from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

EmailString = str(input("Enter the Email ID :: "))
pswd = getpass.getpass("Enter the Password :: ") 

driver = webdriver.Firefox()
driver.get('http://www.facebook.com')
element = driver.find_element_by_name("email")
element.send_keys(EmailString)
element1 = driver.find_element_by_name("pass")
element1.send_keys(pswd,Keys.TAB,Keys.ENTER)
#except ConnectionError:
	#print('Please check your internet connection and try again. Sorry for inconvenience.')
