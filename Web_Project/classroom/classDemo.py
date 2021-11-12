from Account.models import Student, Faculty

class classForStudent:
    faculty = Faculty
    enroll = []
    lecturer = []
    
    def putKeyOfClassroomKey(self, id):
        self.lecturer = Faculty.objects.filter(classroom = id)
        #all_students = Student.objects.get(classroom = id)
        #for st in
        self.enroll =  Student.objects.filter(classroom = id)
        # self.enroll.append(st)
             
    def studentList(self):
        return self.enroll
    
    def facultyList(self):
        return self.lecturer

    
    #this method basically for check, is everything store succesfuly or not
    def __iter__(self):
        return self.enroll.__iter__()
    
    

class classForFaculty:
    student = Student
    enroll = []
    lecturer = []
    
    def putKeyOfClassroomKey(self, id):
        self.lecturer = Faculty.objects.filter(classroom = id)
        #all_students = Student.objects.get(classroom = id)
        #for st in 
        self.enroll =  Student.objects.filter(classroom = id)
        # self.enroll.append(st)
             
    def studentList(self):
        return self.enroll
    
    def facultyList(self):
        return self.lecturer

    
    #this method basically for check, is everything store succesfuly or not
    def __iter__(self):
        return self.enroll.__iter__()