#TODO: Add functionality to save location, spot to resume download
#TODO: Set up how to download information
#TODO: Set up log file.
#TODO: Upload to online database.
"""
Web Page Scraper for Teacher Evals Page
github/mikur/mikurio

Scrapes All the Websites from the Course Eval and outputs to a database.
"""

from retrieveCourseEvalLinks import browser
import retrieveCourseEvalLinks as retrieve


def read_file():
	"""
	Read the file containing all the links to Course Evals
	"""

	global COURSE_LINKS
	COURSE_LINKS = [line.rstrip('\n') for line in open('CourseEvalLinks.txt')]

def traverse_courses():
	"""
	Go through all the courses available in data.
	"""


def extract_data(url):
	"""
	Get the Course Information from given course website.
	"""
	browser.get(url)
	course_name = browser.find_element_by_tag_name('h1').text
	teacher_name = browser.find_element_by_tag_name('h2').text
	course_info = browser.find_element_by_tag_name('table').text

	print(course_name)
	print(teacher_name)
	print(course_info, end = '\n\n')

def main():

	retrieve.login(retrieve.get_userpass())
	retrieve.set_up_directory("C:\\Users\\Leo\\Envs\\MikuRio\\MikuRio\\CourseEvalRetriever")
	
	read_file()
	
	for course in COURSE_LINKS[0:10]:
		extract_data(course)
		

	browser.quit()	
if __name__ == '__main__':
	main()
