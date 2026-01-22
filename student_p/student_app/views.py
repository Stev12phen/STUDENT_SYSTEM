from django.shortcuts import render, redirect, HttpResponse
from .models import Student, Department, Lecture
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django. contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required












def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')


# def add_student(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name')
#         last_name  = request.POST.get('last_name')
#         email      = request.POST.get('email')
#         age        = request.POST.get('age')
#         image      = request.FILES.get('image')  # for image

#         Student.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             age=age,
#             image=image
#         )

#         return redirect('success')  # or any page you want

#     return render(request, 'add_student.html')



def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password = request.POST.get('password')
        password2= request.POST.get('password2')

        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'register_user.html')


def student_info(request):
    students= Student.objects.all()
    return render(request, 'student_info.html', {'students': students})




def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('success')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'Login.html')





def add_lecturer(request):
    departments = Department.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        department_id = request.POST.get('department')
        image = request.FILES.get('image')


        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return redirect('add_lecturer')
        if User.objects.filter(username=username).exists():
            messages.error(request, "username alreeady exists")
            return redirect('login')

        # Create the User first
        user = User.objects.create_user(username=username, password=password, email=email)
        

        department = Department.objects.get(id=department_id)

        Lecture.objects.create(
            name=name,
            phone=phone,
            email=email,
            department=department,
            image=image,
            user= user

        )
        messages.success(request, f"lecturer {name} added successfully")

        return redirect('success')  # or any page

    return render(request, 'add_lecturer.html', {'departments': departments})





@staff_member_required
def view_lecturers(request):
    lecturers= Lecture.objects.all()
    return render(request, 'view_lecturers.html', {'lecturers': lecturers})


def logout_user(request):
    logout(request)
    messages.error(request, "Logged out successfully")
    return redirect('home')





def register_student(request):
    if request.method == "POST":
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        image = request.FILES.get('image')

        # Get user credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Validate passwords
        if password != password2:
            
            return redirect('register_student')

        # Check if username exists
        if User.objects.filter(username=username).exists():

            
            return redirect('login')

        # Create the User first
        user = User.objects.create_user(username=username, password=password, email=email)
        
        # Create the Student and link to User
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            image=image,
            user=user
        )

        messages.success(request, f"Student {first_name} registered successfully")
        return redirect('success')

    return render(request, 'register_student.html')



def Student_details(request, student_id):
    student= Student.objects.get(id = student_id)
    return render(request, 'student_details.html', {'student': student})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    messages.success(request, "Student deleted successfully")
    return redirect('student_info')



