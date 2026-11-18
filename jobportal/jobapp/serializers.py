from rest_framework import serializers
from .models import Job,Applications

class JobSerializer(serializers.Serializer):
    employer = serializers.CharField(max_length= 100)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1000)
    category = serializers.ChoiceField(choices= Job.Catchoices, default="software")
    experience_level = serializers.ChoiceField(choices= Job.EXPERIENCE_CHOICES, default="fresher")
    location = serializers.CharField(max_length=50)
    posted_date = serializers.DateTimeField(read_only= True)
    is_open = serializers.BooleanField(default= True)

class ApplicationSerializer(serializers.Serializer):
    
    job_id = serializers.IntegerField()
    candidate_name = serializers.CharField(max_length= 50)
    mobile_no = serializers.CharField()
    place = serializers.CharField(max_length= 50)
    cover_letter = serializers.CharField(max_length= 1000)
    status = serializers.ChoiceField(choices= Applications.status_choices, default= "pending", read_only= True)
    remarks	= serializers.CharField(read_only= True)
    applied_date = serializers.DateTimeField(read_only= True)

    def validate(self, validate_data):
        job_id = validate_data.get("job_id")
        if not Job.objects.filter(id = job_id).exists():
            raise serializers.ValidationError("job does not exist!")
        return validate_data

class ReviewSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices= Applications.status_choices)
    remarks	= serializers.CharField(max_length = 1000)
