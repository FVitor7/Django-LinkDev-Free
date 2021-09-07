from django.shortcuts import render, redirect, get_object_or_404
from core.models import Link, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import LinkSerializer
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import (HttpResponseRedirect,
                         Http404,
                         HttpResponsePermanentRedirect)

from django.contrib.auth.models import User
from django.db.models import F


# Create your views here.

@api_view(['GET'])
def home_api(request, format=None):
    url = request.build_absolute_uri()
    return Response({
        'links':  str(url)+'links/?username=admin',
    })


class LinkViewSet(viewsets.ModelViewSet):

    http_method_names = ['get']
    lookup_field = 'id'
    serializer_class = LinkSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = []

        username = self.request.query_params.get('username')

        if username is not None:
            user = User.objects.get(username__iexact=username)
            queryset = Link.objects.filter(user=user).all()
            return queryset


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            temp_user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            messages.error(
                request, "O nome de usuário inserido não pertence a uma conta. \
                    Verifique seu nome de usuário e tente novamente.")
            return redirect('/')

        user = authenticate(request, username=temp_user, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(
                request, "Sua senha está incorreta. Confira-a.")

    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Corrija os erros abaixo:')

    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, 'app/dashboard.html')


@login_required(login_url='/login/')
def list_links(request):
    user = request.user
    link = Link.objects.filter(user=user)
    data = {'links': link}
    return render(request, 'links.html', data)


@login_required(login_url='/login/')
def new_link(request):
    id_link = request.GET.get('id')
    data = {}
    if id_link:
        data['link'] = Link.objects.get(id=id_link)
    return render(request, 'new_link.html', data)


@login_required(login_url='/login/')
def submit_link(request):
    if request.POST:
        title = request.POST.get('title')
        url = request.POST.get('url')
        description = request.POST.get('description')
        background_color = request.POST.get('background_color')
        user = request.user
        id_link = request.POST.get('id_link')

        if id_link:
            link = Link.objects.get(id=id_link)
            if link.user == user:
                link.title = title
                link.url = url
                link.description = description
                link.background_color = background_color
                link.save()

        else:
            Link.objects.create(title=title, url=url,
                                description=description, user=user,
                                background_color=background_color)

    return redirect('/')


@login_required(login_url='/login/')
def delete_link(request, id_link):
    user = request.user
    try:
        link = Link.objects.get(id=id_link)
    except Exception:
        raise Http404()
    if user == link.user:
        link.delete()
    else:
        raise Http404()
    return redirect('/')


def template_user(request, username):
    try:
        user = User.objects.get(username=username)
        data = {"username": user}
    except Exception:
        raise Http404()
    return render(request, 'template_user.html', data)


def redirect_url(request, username, id_link):
    try:
        link = Link.objects.get(id=id_link)

    except Exception:
        raise Http404()   
       
    link.stories_filed += 1
    link.save(update_fields=['id_link'])
    #link.update(id_link=F('id_link') + 1)
    
    return HttpResponsePermanentRedirect(link.url)
