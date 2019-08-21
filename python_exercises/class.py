my_student = {
'name':'ajay',
'grades':[90,70,60,80],
'average':None#someshit
}

def average_grade(studnt):
	return sum(studnt['grades'])/len(studnt['grades'])

class Student:
	def  __init__(self,new_name,new_grade):
		self.name = new_name
		self.grades = new_grade
	def average(self):
		return sum(self.grades)/len(self.grades)

student_one   = Student('ajay',[70,90,96,65])
student_two  = Student('xyz',[70,90,96,65])

print(student_two.name)
print(Student.average(student_two))