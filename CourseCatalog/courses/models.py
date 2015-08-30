from django.db import models

class Course(models.Model):
	department = models.CharField(max_length=260)
	course_name = models.CharField(max_length=260)
	teacher = models.CharField(max_length=40)
	standing = models.CharField(max_length=30)
	quarter = models.CharField(max_length=4)
	surveyed = models.IntegerField()
	enrolled = models.IntegerField()

	# Add in date updated. 
	def __str__(self):
			return course_name

	""" 
	Add function to other script
	def breakdown_course(course):
		
		Splits the full course name into course name, teacher, quarter
		taught and course id.
		COULD MAKE BETTER USING SPLIT()
		

		#Get department by going through string until its only a title
		i = 0 
		while i < len(course) and not course[:-i].isTitle():
			i = i +1

		department = course[:-i-2]
		other_part = course[len(department) +1 :]

		# Get course name and number by iterating through string until its 
		# comprised off all uppercases and numbers.
		i = 1
		while i < len(other_part) and other_part[:i].isupper():
			i = i +1
		course_name = other_part[:i-2].strip()

		# Retrieve teacher name and standing.
		other_part = other_part[len(course_name) + 1:].strip()

		quarter = other_part[-4:]
		other_part = other_part[:-4].strip()

		teacher = ' '.join(other_part.split()[:2])
		standing = ' '.join(other_part.split()[2:])

		return (department, course_name, teacher, standing, quarter)

	"""
class Rating(models.Model):
		course = models.ForeignKey(Course)
		course_whole = models.DecimalField(max_digits )
		course_content = 
		instructor_contrib = 
		instctr_effect = 
		instructor_interest = 
		amount_learned = 
		grading_techniques = 

	

