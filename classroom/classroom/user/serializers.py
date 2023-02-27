from rest_framework import serializers


class StudentDetailSerializer(serializers.Serializer):
    studentName = serializers.CharField(max_length=100)
    contactNumber = serializers.CharField(max_length=10)
    email = serializers.EmailField(required=False)
    gender = serializers.CharField(max_length=100)
    dateOfBirth = serializers.DateField()
    nationality = serializers.CharField(max_length=100)
    birthPlace = serializers.CharField(max_length=100,required=False)
    motherTongue = serializers.CharField(max_length=100)
    cast = serializers.CharField(max_length=100)
    religion = serializers.CharField(max_length=100)
    bloodGroup = serializers.CharField(max_length=100, required=False)
    aadharNumber = serializers.IntegerField()
    studentGroup = serializers.JSONField(required=False)
    extraActivities = serializers.JSONField(required=False)
    StudentImage = serializers.CharField(max_length=100)
    Batch = serializers.JSONField()
    admissionDate = serializers.DateField()
    siblingDetail = serializers.JSONField(required=False)
    Document = serializers.JSONField()
    admissionStatus = serializers.BooleanField(required=False)


class parentsDetailSerializer(serializers.Serializer):
    studentId= serializers.CharField(max_length=100)
    parentsDetailData = serializers.JSONField()
    Address = serializers.JSONField()

