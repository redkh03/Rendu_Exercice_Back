from rest_framework import serializers
from .models import Candidate, Recruiter, JobPost , Trainee

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'
class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'
