from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

#Api librarys
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import MyModel
from .serializers import FileUploadSerializer
from .forms import AnalyzForm
from .models import AnalyzResult
import math

def HomePage(request):
    return render(request, 'index.html')

def JadvalPage(request):
    results = AnalyzResult.objects.order_by('-id')[:100]  # Oxirgi 10 natija
    context = {'results': results}
    return render(request, 'table.html', context)


def KasalikPage(request):
    return render(request, 'kasalik.html')

def calculate_cardiovascular_risk(age, systolic_blood_pressure, total_cholesterol, hdl_cholesterol, on_blood_pressure_medication, cigarette_smoker, diabetes_present):
    risk_factors = (math.log(age) * 3.06117) + (math.log(total_cholesterol) * 1.12370) - (math.log(hdl_cholesterol) * 0.93263) + (math.log(systolic_blood_pressure) * on_blood_pressure_medication) + cigarette_smoker + diabetes_present - 23.9802
    
    risk = 100 * (1 - math.exp(-0.88936 * risk_factors))
    
    return risk


def FormPage(request):
    if request.method == 'POST':
        form = AnalyzForm(request.POST)
        if form.is_valid():
            # Formani to'g'ri to'ldirilganini tekshirish
            # Ma'lumotlarni olish
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            buying = form.cleaned_data['buying']
            # Boshqa modullar uchun ma'lumotlarni olish
            systolic_blood_pressure = form.cleaned_data['systolic_blood_pressure']
            total_cholesterol = form.cleaned_data['total_cholesterol']
            hdl_cholesterol = form.cleaned_data['hdl_cholesterol']
            on_blood_pressure_medication = form.cleaned_data['on_blood_pressure_medication']
            cigarette_smoker = form.cleaned_data['cigarette_smoker']
            diabetes_present = form.cleaned_data['diabetes_present']
            # Ma'lumotlarni ishlash va bazaga saqlash


            # return redirect('form')  # Muvaffaqiyatli yuborildi
            risk = calculate_cardiovascular_risk(int(age), int(systolic_blood_pressure), int(total_cholesterol), int(hdl_cholesterol), int(on_blood_pressure_medication), int(cigarette_smoker), int(diabetes_present))
            risk = f"{risk:.2f}"
            text = f"10-year cardiovascular risk: {risk}"
            AnalyzResult.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                buying=buying,
                systolic_blood_pressure=systolic_blood_pressure,
                total_cholesterol=total_cholesterol,
                hdl_cholesterol=hdl_cholesterol,
                on_blood_pressure_medication=on_blood_pressure_medication,
                cigarette_smoker=cigarette_smoker,
                diabetes_present=diabetes_present,
                predict = risk
            )
            return render(request, 'form.html', {'text':text})
    else:
        form = AnalyzForm()
    return render(request, 'form.html', {'form': form})


class MyApiView(APIView):
    def post(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    return Response({"error": "Password notug'ri"}, status=status.HTTP_400_BAD_REQUEST)
                
                file_obj = request.FILES['file']
                my_model = MyModel(user=username, password=password, file=file_obj)
                my_model.save()

                return Response({"success": "File saqlandi"}, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                return Response({"error": "User topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def SignPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not uname or not password1:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'signup.html')

        if User.objects.filter(username=uname).exists():
            messages.error(request, 'This username is already taken. Please choose a different username.')
            return render(request, 'signup.html')

        if password1 != password2:
            messages.error(request, 'Passwords do not match. Please make sure the passwords match.')
            return render(request, 'signup.html')

        my_user = User.objects.create_user(uname, email, password1)
        my_user.save()
        return redirect('login')

    return render(request, 'signup.html')




def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Username yoki password xatolik!"
            return render(request, 'login.html', {'error': error_message})

    return render(request, 'login.html')



def LogoutPage(request):
    logout(request)
    return redirect('home')

