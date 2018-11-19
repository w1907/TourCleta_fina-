from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from authenticate.forms import SignUpForm
from authenticate.models import Profile
from reserva.models import Order

def signin(request):
	data = {}
	template = "signin.html"
	logout(request)
	username = password = ""
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('core.index'))
			else:
				messages.warning(request, "Correo o contraseña invalidos")
		else:
			messages.warning(request, "Correo o contraseña invalidos")
	return render(request, template, data)

def signout(request):
	logout(request)
	return HttpResponseRedirect(reverse('authenticate.signin'))

def register(request):
	template = 'register.html'
	if request.POST:
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.telefono = form.cleaned_data.get('telefono')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect(reverse('core.index'))
	else:
		form = SignUpForm()
	return render(request, template, {'form': form})

def perfil(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	print(my_user_profile.id)
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	print(my_orders)
	context = {
		'my_user_profile': my_user_profile,
		'my_orders': my_orders
	}

	return render(request, "profile.html", context)