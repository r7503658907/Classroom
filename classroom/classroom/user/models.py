from django.db import models
genderType = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
)
bloodGroupType =(
    ("A+", "A+"),
    ("A-", "A-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("A+", "A+"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("O+", "O+"),
    ("O-", "O-"),

)
castType = (
    ("EWS", "EWS"),
    ("General", "General"),
    ("NT", "NT"),
    ("OBC", "OBC"),
    ("SBC", "SBC"),
    ("SC", "SC"),
    ("ST", "ST"),
    ("VJ", "VJ"),
)
class StudentDetail(models.Model):
    studentId = models.CharField(max_length=100, primary_key=True)
    studentName = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=10)
    email = models.EmailField()
    gender = models.CharField(max_length=100,choices=genderType)
    dateOfBirth = models.DateField()
    nationality = models.CharField(max_length=100)
    birthPlace = models.CharField(max_length=100)
    motherTongue = models.CharField(max_length=100)
    cast = models.CharField(max_length=100,choices=castType)
    religion = models.CharField(max_length=100)
    bloodGroup = models.CharField(max_length=100,choices=bloodGroupType)
    aadharNumber = models.IntegerField()
    studentGroup = models.TextField()
    extraActivities = models.TextField()
    StudentImage = models.CharField(max_length=100)
    Batch = models.TextField()
    admissionDate = models.DateField()
    siblingDetail = models.TextField()
    Document = models.TextField()
    admissionStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.studentId


class parentsDetail(models.Model):
    parentsId = models.AutoField(primary_key=True)
    studentId = models.ForeignKey(StudentDetail,on_delete=models.CASCADE)
    parentsDetailData = models.TextField()
    Address = models.TextField()

    def __str__(self):
        return str(self.parentsId)
