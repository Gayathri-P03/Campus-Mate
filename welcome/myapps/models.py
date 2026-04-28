from django.db import models

class CollegeStudent(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.reg_no})"
class GroupMessage(models.Model):

    group_name = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    message = models.TextField()
    file = models.FileField(upload_to="chat_files/",blank=True,null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.group_name}"
class CollegeStudent(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.reg_no})"

class Result(models.Model):
    student_name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20)

    design_marks = models.IntegerField()
    arvr_marks = models.IntegerField()
    bda_marks = models.IntegerField()
    ethics_marks = models.IntegerField()
    iot_marks = models.IntegerField()
    pom_marks = models.IntegerField()

    def design_result(self):
        return "P" if self.design_marks >= 50 else "F"

    def arvr_result(self):
        return "P" if self.arvr_marks >= 50 else "F"

    def bda_result(self):
        return "P" if self.bda_marks >= 50 else "F"

    def ethics_result(self):
        return "P" if self.ethics_marks >= 50 else "F"

    def iot_result(self):
        return "P" if self.iot_marks >= 50 else "F"

    def pom_result(self):
        return "P" if self.pom_marks >= 50 else "F"

    def __str__(self):
        return self.student_name

class Assignment(models.Model):
    student_name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    assignment_no = models.CharField(max_length=50)
    date = models.DateField()
    assignment_file = models.FileField(upload_to='assignments/')
    section = models.CharField(max_length=1)

    def __str__(self):
        return self.student_name

class Certificate(models.Model):

    student_name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    date = models.DateField()
    organization = models.CharField(max_length=200)
    certificate_file = models.FileField(upload_to="certificates/")

    def __str__(self):
        return self.student_name

class Feedback(models.Model):

    student_name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=50)

    staff_name = models.CharField(max_length=100)

    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.staff_name}"

class NoDueVerification(models.Model):

    student_name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)

    status = models.CharField(max_length=20)  # Verified / Not Verified
    # ✅ ADD THIS
    office_status = models.CharField(max_length=20, blank=True, null=True)
    superintendent_status = models.CharField(max_length=20, blank=True, null=True)
    hod_status = models.CharField(max_length=20, blank=True, null=True)
    principal_status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.student_name

class StudentProfileVerification(models.Model):

    student_name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=50)

    staff_name = models.CharField(max_length=100)   # who verified

    status = models.CharField(max_length=20)  # Verified / Not Verified

    def __str__(self):
        return f"{self.student_name} - {self.staff_name}"