from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CropPredictionHistory
from .ml_model import predict_crop
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email.split('@')[0]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Galat email ya password!')
    return render(request, 'log.html')

def register_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email.split('@')[0]
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = full_name
            user.save()
            login(request, user)
            return redirect('dashboard')
    return render(request, 'Registration.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login')
def crop_recommendation_view(request):
    if request.method == 'POST':
        n = float(request.POST.get('nitrogen'))
        p = float(request.POST.get('phosphorus'))
        k = float(request.POST.get('potassium'))
        temp = float(request.POST.get('temperature'))
        hum = float(request.POST.get('humidity'))
        ph = float(request.POST.get('ph'))
        rain = float(request.POST.get('rainfall'))
        algo = request.POST.get('algorithm', 'random_forest')

        crop = predict_crop(n, p, k, temp, hum, ph, rain, algo)

        CropPredictionHistory.objects.create(
            user=request.user if request.user.is_authenticated else None,
            nitrogen=n, phosphorus=p, potassium=k,
            temperature=temp, humidity=hum, ph=ph, rainfall=rain,
            algorithm=algo, predicted_crop=crop
        )
        return render(request, 'prediction-result.html', {
    'crop': crop,
    'n': n,
    'p': p,
    'k': k,
    'ph': ph,
    'temp': temp,
    'hum': hum,
    'rain': rain,
    'algo': algo
})
    return render(request, 'crop-recommendation.html')

@login_required(login_url='login')
@login_required(login_url='login')
def prediction_history_view(request):
    history = CropPredictionHistory.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'prediction-history.html', {'history': history})

@login_required(login_url='login')
def crop_info_view(request):
    return render(request, 'crop-info.html')

@login_required(login_url='login')
def about_help_view(request):
    return render(request, 'about-help.html')
