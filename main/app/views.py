from django.shortcuts import render

from .models import Product
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import ProductForm


class ProductView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class LoginingView(LoginView):
    model = User
    template_name = 'login.html'
    success_url = '/'


class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'add_product.html'
    login_url = '/login'
    success_url = '/product'
    form_class = ProductForm
