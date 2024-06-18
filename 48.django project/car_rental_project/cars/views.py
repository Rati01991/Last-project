from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Car, Rental
from .forms import CarForm, RentalForm  # Ensure this line is correct

def car_list(request):
    cars = Car.objects.filter(available=True)
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def rent_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.user = request.user
            rental.car = car
            rental.save()
            car.available = False
            car.save()
            return redirect('car_list')
    else:
        form = RentalForm()
    return render(request, 'cars/rent_car.html', {'form': form, 'car': car})

def post_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            if request.user.is_authenticated:
                car.owner = request.user
            car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/post_car.html', {'form': form})

@login_required
def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/update_car.html', {'form': form, 'car': car})

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'cars/delete_car.html', {'car': car})