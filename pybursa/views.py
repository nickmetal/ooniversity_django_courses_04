# encoding: utf-8
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.utils import timezone
import settings
from courses.models import Course


def index(request):
    course_qs = Course.objects.all()
    return render(request, 'index.html',
            {"courses":course_qs})


@login_required
def contact(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        context = [{'name':'Nick Nickolaev',
                    'skype':'some.login',
                    'email':'somemail@gmail.com',
                    'phone':'+38 099 000 00 02',
                    'lvl':'Director'
                    },
                    {'name':'Дария Михалевич',
                    'skype':'darka.darka.darka.darka.',
                    'email':'daria.mykhalevych@gmail.com',
                    'phone':'+38 096 469 15 57',
                    'lvl':'Manager'
                    },
                  {'name':'Павел Обод',
                'skype':'azaless',
                'email':'tbursa100@gmail.com',
                'phone':'+38 099 000 00 01',
                'lvl':'Founder'
                }]

        data = "Text Some 123123"

        return render(request, 'contact.html', {"contacts":context, "data":data})


# def handler404(request):
#     response = render_to_response('404.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response


# def handler500(request):
#     response = render_to_response('500.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 500
#     return response



def my_login(request):
    print request.body
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print "---->",username, password
        if user is not None:
            if user.is_active:
                login(request, user)
                # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
                print "----> here ", request.GET['next'].strip("/")
                print "----> request.path ", request.path

                path_to_redirect = '%s' % request.GET['next'].strip("/") or request.path
                print "path_to_redirect", path_to_redirect
                return redirect(path_to_redirect)
                # return redirect('index')

            else:
            # Return a 'disabled account' error message
                print "----> disabled account "

        else:
            print "----> invalid login "
            # Return an 'invalid login' error message.


    if "next" in request.GET:
        message = "Для просмотра этой страницы введите ваши данные"
    else:
        message = "Вход в систему"

    return render(request, 'login.html', {"message": message})

def my_logout(request):
    return redirect('%s' % request.path)


def getJSNdata(request):
    now=timezone.localtime(timezone.now()).strftime('%H:%M:%S')
    print request.method

    out_data = {"time":now}
    #print "request.GET", request.GET
    #print "request.POST", request.POST
    print "request.user", request.user

    if 'getStudent' in request.GET:
        stud_link = request.GET.get('getStudent')
        stud_id = stud_link.split('/')[-2]#[u'#', u'students', u'2', u'']
        #print stud_id
        out_data.update({"studentID": stud_id})

    return JsonResponse(out_data)

def test(request):
    return render(request, 'test.html')
