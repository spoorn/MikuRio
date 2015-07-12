# Web Page Scraper for Teacher Evals Page
# github/mikur/mikurio

import mechanicalsoup, os, argparse

parser = argparse.ArgumentParser(description='WebLogin to UW')
parser.add_argument('username')
parser.add_argument('password')

args = parser.parse_args()

browser = mechanicalsoup.Browser()

login_page = browser.get('https://weblogin.washington.edu/')
login_form = login_page.soup.body.div.div.div.form.ul
#login_form = login_page.soup.select(".weblogin_netid")

login_form.select("#weblogin_netid")[0]['value'] = args.username 
login_form.select("#weblogin_password")[0]['value'] = args.password

logged_page = browser.submit(login_form, login_page.url)

