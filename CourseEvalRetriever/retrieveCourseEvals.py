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


def main():

	retrieve.login(retrieve.get_userpass())
	retrieve.set_up_directory("C:\\Users\\Leo\\Documents\\MikuRio\\CourseEvalRetriever")
	
		

	
if __name__ == '__main__':
	main()
