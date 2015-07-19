"""
Web Page Scraper for Teacher Evals Page
github/mikur/mikurio
"""

import mechanicalsoup, os, argparse, string
from robobrowser import RoboBrowser
from selenium import webdriver

teacher_links =[]
browser = webdriver.Firefox()

def clean_links(links):
	"""
	Remove links that don't link to teacher evals
	"""
	return links[10:-3]

def get_userpass():
	"""
	Get Username and Password User entered into Command Line
	Returns parser
	"""
	parser = argparse.ArgumentParser(description='WebLogin to UW')
	parser.add_argument('username')
	parser.add_argument('password')

	return parser.parse_args()

def login(user_input):
	"""
	Logs into WebLogin UW
	Username and Password given work
	Pass in Selenium browser to be in the same session
	"""
	browser.get('https://weblogin.washington.edu')
	loginElement = browser.find_element_by_id('weblogin_netid')
	loginElement.send_keys(user_input.username)

	passwordElement = browser.find_element_by_id('weblogin_password')
	passwordElement.send_keys(user_input.password)
	passwordElement.submit()

def get_all_links(url):
	"""
	Open a page listing all courses and retrieve all the teacher links
	"""

	browser.get(url)
	return clean_links(browser.find_elements_by_tag_name('a'))

def main():
	
	login(get_userpass())
	
	list_of_sites = ['https://www.washington.edu/cec/{0}-toc.html'.format(s) for s in string.ascii_lowercase[:23]]
	
	for url in list_of_sites:
		teacher_links.extend(get_all_links(url))
	
	
	print('\n\n\n{}'.format(len(teacher_links)))
	print("Done")	
		

if __name__ == '__main__':
	main()
