from rest_framework import serializers
from records.models import Student, Subject, Record, Event


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'grade', 'age')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'description', 'extra_curricular')


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('id', 'date', 'student', 'subject', 'time_spent', 'completed')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'event_length', 'start_time', 'student', 'description')

class StudentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name','description','extra_curricular')


class SubjectStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name','last_name','age', 'grade')