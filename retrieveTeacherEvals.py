# Web Page Scraper for Teacher Evals Page
# github/mikur/mikurio

import mechanicalsoup, os, argparse, string
from robobrowser import RoboBrowser
from selenium import webdriver

parser = argparse.ArgumentParser(description='WebLogin to UW')
parser.add_argument('username')
parser.add_argument('password')

args = parser.parse_args()

"""
# using mechanical browser, but need javascript so using selenium.
browser = mechanicalsoup.Browser()
login_page = browser.get('https://weblogin.washington.edu/')
login_form = login_page.soup.body.div.div.div.form
#print(login_form)

login_form.select("#weblogin_netid")[0]['value'] = args.username 
login_form.select("#weblogin_password")[0]['value'] = args.password
logged_page = browser.submit(login_form, login_page.url)

mainPage = browser.get('https://www.washington.edu/cec/a-toc.html')
"""

"""
selenium_browser = webdriver.Firefox()
selenium_browser.get('https://weblogin.washington.edu')
loginElement = selenium_browser.find_element_by_id('weblogin_netid')
loginElement.send_keys(args.username)
passwordElement = selenium_browser.find_element_by_id('weblogin_password')
passwordElement.send_keys(args.password)
passwordElement.submit()
"""

list_of_sites = ['https://www.washington.edu/cec/{0}-toc.html'.format(s) for s in string.ascii_lowercase[:23]]
		

