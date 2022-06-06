from django.urls import path
from records import views as record_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', record_views.index_page, name='school_records'),
    path('students/', record_views.students),
    path('add_student/', record_views.add_student),
    path('students/<int:student_id>/', record_views.update_student),
    path('subjects/', record_views.subjects),
    path('add_subject/', record_views.add_subject),
    path('subjects/<int:subject_id>/', record_views.update_subject),
    path('delete/<int:subject_id>/', record_views.delete_subject),
    path('students/<str:name>/', record_views.subjects_student_takes),
    path('subjects/<str:name>/', record_views.students_subject),
    path('records/', record_views.records_all),
    path('add_record/', record_views.add_record),
    path('record/', record_views.records),
    path('record/<int:record_id>/', record_views.update_record),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
