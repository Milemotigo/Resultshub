from django.shortcuts import render
from generics.models import CustomUser
from django.contrib.auth.decorators import login_required
from student.models import Student
from result.models import Result
from college.models import Department
from django.http import HttpResponse

@login_required
def result(request):
    mat_no = request.GET.get('matric_number')
    try:
        if mat_no is not None:
            student = Student.objects.get(matric_number=mat_no)
        else:
            return HttpResponse('Matriculation number required', status=400)
        #query base on where the student matches the provided student object
        results = Result.objects.filter(student=student)
        courses = Department.objects.get(name=student.department)
        total_courses = len(courses)
        for result in results:
            grade = result.grade
            score = result.score
            course_unit = result.course_unit
            remark = result.remark

            total_score += (score * course_unit) / total_courses
        pg = total_score * 100

        if pg >= 70:
            grade = 'A'
            remark = 'EXCELLENT'
        elif pg >= 60:
            grade = 'B'
            remark = 'VERY GOOD'
        elif pg >= 50:
            grade = 'C'
            remark = 'GOOD'
        elif pg >= 45:
            grade = 'D'
            remark = 'SATISFACTORY'
        elif pg >= 40:
            grade = 'E'
            remark = 'PASS'
        else:
            grade = 'F'
            remark = 'FAIL'
    except Student.DoesNotExist:
        return HttpResponse('Student not found', status=404)

    return render(request, 'generics/result/result.html', locals())

@login_required
def payment(request):
    return render(request, 'generics/result/payment.html')
