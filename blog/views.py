from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from .models import Leave
from django.utils import timezone


User = get_user_model()
#UserModel = get_user_model()

# Create your views here.

def index(request):
	return render(request, 'blog/index.html')

def loginform(request):
	return render(request, 'blog/index.html')

class crud():
    def savedata(request):
        # model = Customer
        # template_name = 'firstapp/results.html'
        sv = Leave(from_date=timezone.now())
        sv.save()
        # return redirect()

        return HttpResponseRedirect(reverse('test'))


    def pay(request):
        v = Leave(to_date=timezone.now())
        v.save()
        return HttpResponseRedirect(reverse('test'))


@login_required
def home(request):
	current_user = request.user
	user_id = current_user.id
	print(user_id)
	context = {'user_id': user_id}
	return render(request, 'blog/home.html', context)


def registerform(request):
	return render(request, 'blog/register.html')


class RegisterView(SuccessMessageMixin, CreateView):
	model = User
	fields = ['username', 'password', 'email']
	template_name = 'blog/register.html'
	success_url = reverse_lazy('registerform')
	success_message = "Account was created successfull"

	def form_valid(self, form):
		form.instance.password = make_password(form.instance.password)
		return super().form_valid(form)


from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve, reverse
from django.http import HttpResponseRedirect
from motech import settings
from django.contrib.auth.decorators import login_required



class LoginRequiredMiddleware(MiddlewareMixin):
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings by setting a tuple of routes to ignore
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), """
        The Login Required middleware needs to be after AuthenticationMiddleware.
        Also make sure to include the template context_processor:
        'django.contrib.auth.context_processors.auth'."""

        if not request.user.is_authenticated:
            current_route_name = resolve(request.path_info).url_name

            if not current_route_name in settings.AUTH_EXEMPT_ROUTES:
                return HttpResponseRedirect(reverse(settings.AUTH_LOGIN_ROUTE))

def regi(request):
	return render(request, 'blog/reg.html')

@login_required
def test(request):
	return render(request, 'blog/test.html')	

def add_vehicle(request):
    return render(request, 'blog/add.html')

def register(request):
    if request.method == 'POST':
    	#first_name=request.POST['first_name']
    	first_name = request.POST.get('first_name')
    	last_name = request.POST.get('last_name')
    	#last_name=request.POST['last_name']
    	username=request.POST['username']
    	user_type=request.POST['user_type']
    	print(user_type)
    	is_admin = ""
    	is_cashier = ""
    	is_register = ""

    	if user_type == is_admin:
    		is_admin=1
    		user = User.objects.create_user(username,is_admin)
    	elif user_type == is_cashier:
    		is_cashier=1
    		user = User(username,is_cashier=1)
    	else:
    		is_register="1"
    		user = User(first_name, last_name, username, is_register=True)
    	print(user_type)	    		
    	#user = User.objects.create_user(first_name,last_name,username)
    	print(first_name)
    else:
    	return HttpResponse("No")


"""
def register(request):
    if request.method == 'POST':
    	user = User.objects.create_user(
                username=cleaned_data['username'],
                password=cleaned_data['password1'],
                is_staff=True,
                is_active=True,
                is_superuser=True,
                email=cleaned_data['email'],
                first_name=cleaned_data['first_name'],
                last_name=cleaned_data['last_name']
            )
    	return HttpResponse("Ok")
    else:
        HttpResponse("No")
"""
