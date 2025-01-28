from django.shortcuts import render
from newsapp.models import Employee


# Create your views here.

def index(request):
    return render(request, 'newsapp/index.html')


def empinfo(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request, 'newsapp/emp.html', context=my_dict)


def moviesinfo(request):
    head_msg = "Latest Movies Information"
    msg1 = 'OG from power start pawan kalyan'
    msg2 = 'Game Changer from Ram Charan'
    msg3 = 'Sprit from Prabhas'
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request, 'newsapp/news.html', context=my_dict)

def sportsinfo(request):
    head_msg = "Latest Sports Information"
    msg1 = 'OG from power start pawan kalyan'
    msg2 = 'Game Changer from Ram Charan'
    msg3 = 'Sprit from Prabhas'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request, 'newsapp/news.html', context=my_dict)
    return render(request, 'newsapp/news.html')

def politicsinfo(request):
    head_msg = "Latest Politics Information"
    msg1 = 'OG from power start pawan kalyan'
    msg2 = 'Game Changer from Ram Charan'
    msg3 = 'Sprit from Prabhas'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request, 'newsapp/news.html', context=my_dict)
    return render(request, 'newsapp/news.html')
