
from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponseRedirect
from records.serializers import *
from .models import Student, Subject, Record, Event
from .forms import AddStudent, AddSubject, AddRecord, GetRecordForm


def index_page(request):
    return render(request, 'records/hello_school_records.html', {})

def students(request):
    students = Student.objects.all()

    return render(request, 'records/student_list.html', {'students':students})

def add_student(request):
    submitted = False
    if request.method =="POST":
        form = AddStudent(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_student?submitted=True')

    else:
        form = AddStudent
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'records/add_student.html', {'form': form, 'submitted':submitted})


def add_subject(request):
    submitted = False
    if request.method =="POST":
        form = AddSubject(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_subject?submitted=True')

    else:
        form = AddSubject
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'records/add_subject.html', {'form': form, 'submitted':submitted})

def add_record(request):
    submitted = False
    if request.method =="POST":
        form = AddRecord(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_record?submitted=True')

    else:
        form = AddRecord
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'records/add_record.html', {'form': form, 'submitted':submitted})

def subjects(request):
    subjects = Subject.objects.all()

    return render(request, 'records/subject_list.html', {'subjects':subjects})

def records_all(request):
    records = Record.objects.all().order_by('student', 'subject')

    return render(request, 'records/records_all_list.html', {'records':records})


def records(request):

    if request.method == "POST":
           
        form_data = GetRecordForm(request.POST)
 
        year = form_data['year'].value()
        month = form_data['month'].value()
        date = month + '/' + str(year)

        fname = form_data['fname'].value()
        sname = form_data['sname'].value()

        try:
            students = Student.objects.get(first_name=fname)
        except Student.DoesNotExist:
            message = 'Student does not exist'
            return render(request, 'records/error.html', {'message': message})

        try:
            subject = Subject.objects.get(name=sname)
        except Subject.DoesNotExist:
            message = 'Subject does not exist'
            return render(request, 'records/error.html', {'message': message})
    
        subject_id = subject.id

        get_record = students.record_set.filter(date__year=year, date__month=month, subject=subject_id).order_by('subject')

        time_spent = get_record.aggregate(sum=Sum('time_spent'))
        record= True
    
        context = {'date':date, 'student':students, 'subject': subject, 'time_spent': time_spent, 'record':record}

        return render(request, 'records/record.html', context)

    else:
        form = GetRecordForm
        return render(request, 'records/record.html', {'form': form})



def update_record(request, record_id):
    record = Record.objects.get(pk=record_id)

    form = AddRecord(request.POST or None, instance=record)

    if form.is_valid():
        form.save()
        message = 'Your record has been successfully updated!'
        return render(request, 'records/update.html', {'message': message})

    return render(request, 'records/update_record.html', {'record':record, 'form':form})
    

def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)

    form = AddStudent(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        message = 'Your record has been successfully updated!'
        return render(request, 'records/update.html', {'message': message})

    return render(request, 'records/update_student.html', {'student':student, 'form':form})


def update_subject(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)

    form = AddSubject(request.POST or None, instance=subject)

    if form.is_valid():
        form.save()
        message = 'Your record has been successfully updated!'
        return render(request, 'records/update.html', {'message': message})

    return render(request, 'records/update_subject.html', {'student':subject, 'form':form})

def delete_subject(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    
    subject.delete()

    message = 'Your record has been successfully deleted!'
    return render(request, 'records/update.html', {'message': message})

    


def subjects_student_takes(request, name):

    try:
        student = Student.objects.get(first_name=name)
    except Student.DoesNotExist:
        return render(request, 'records/error.html', {'message': 'The student does not exist'})    

    subjects = student.subject_set.all()        
    return render(request, 'records/student_to_subjects.html', {'subjects': subjects, 'student': student})
        

def students_subject(request, name):

    try:
        subject = Subject.objects.get(name=name)
    except Subject.DoesNotExist:
        return render(request, 'records/error.html', {'message': 'The subject does not exist'})
    
    students = subject.student.all()        
    return render(request, 'records/subject_to_students.html', {'students': students, 'subject': subject})


