from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from getpass import getpass



try:
	# set values to send

	username = input('Type your GH login: ')
	password = getpass('Type your GH password: ')
	repname = input('Type your desired repository name: ') or 'testrepository'
	repdesc = input('Type your desired repository description: ') or 'test repository created via Selenium'
	priv = input('Type your desired repository privacy (private / public): ') or 'private'

	# find login elements

	browser = webdriver.Chrome()
	link = 'http://github.com/login'
	browser.get(link)
	login = browser.find_element(By.ID, 'login_field')
	passw = browser.find_element(By.ID, 'password')
	submitbtn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")

	# send login inputs
	login.send_keys(username)
	passw.send_keys(password)
	submitbtn.click()
	# creating new repo elements
	newrepolink = 'http://github.com/new'
	browser.get(newrepolink)
	reponame = browser.find_element(By.ID, 'repository_name')
	repodesc = browser.find_element(By.ID, 'repository_description')
	if priv == 'private':
		privacy1 = browser.find_element(By.ID, 'repository_visibility_private')
		privacy1.click()
	# inputs for creating new repo
	reponame.send_keys(repname)
	repodesc.send_keys(repdesc)


	time.sleep(2)

	create = browser.find_element(By.XPATH, "//*[@id='new_repository']/div[5]/button")
	action = ActionChains(browser)
	action.move_to_element(create).click().perform()
finally:
	time.sleep(5)
	browser.quit()