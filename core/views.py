from django.shortcuts import render, redirect, get_object_or_404
from core.models import Link, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import LinkSerializer
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import (HttpResponseRedirect,
                         Http404,
                         HttpResponsePermanentRedirect)

from django.contrib.auth.models import User


# Create your views here.

@api_view(['GET'])
def home_api(request, format=None):
    url = request.build_absolute_uri()
    return Response({
        'links':  str(url)+'links/?username=admin',
    })


class LinkViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = LinkSerializer

    pagination_class = None

    def get_queryset(self):

        #queryset = Link.objects.all()
        queryset = []

        username = self.request.query_params.get('username')

        if username is not None:
            user = User.objects.get(username=username)
            queryset = Link.objects.filter(user=user).all()

        return queryset


def login_user(request):
    return render(request, 'login.html')


def register_user(request):
    return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha invalido!")
    return redirect('/')


def submit_register(request):
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

    def verify_user_register():
        if password == password2:
            if len(username) < 4:
                messages.error(
                    request, "Nome de usuário muito pequeno!")
                return
            if User.objects.filter(username=username).exists() == True:
                messages.error(
                    request, "Nome de usuário não disponível!")
                return
            else:
                if User.objects.filter(email=email).exists() == True:
                    messages.error(request, "E-mail não disponível!")
                    return
                else:
                    try:
                        validate_email(email)
                    except ValidationError as e:
                        messages.error(request, "E-mail inválido!")
                    user = User.objects.create_user(username, email, password)

        else:
            messages.error(
                request, "Senhas inválidas")

    verify_user_register()
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        messages.error(request, "Erro ao cadastrar usuário! Tente novamente.")

    return redirect('/register/')


@login_required(login_url='/login/')
def list_links(request):
    user = request.user
    link = Link.objects.filter(user=user)
    #link = Link.objects.all()
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
                                description=description, user=user, background_color=background_color)

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

    link.clicks_count += 1
    link.save()

    return HttpResponsePermanentRedirect(link.url)
