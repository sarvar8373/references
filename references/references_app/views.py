from django.template import loader
from django.http import HttpResponse
from .models import Soato, OPF, OKONX, SOOGU, FS, DOCTYPE, COUNTRY, NATION
from django.core.paginator import Paginator
from django.shortcuts import render

def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def soato(request):
    records_list = Soato.objects.all()
    code_filter = request.GET.get('code')
    name_uzl_filter = request.GET.get('name_uzl')

    if code_filter:
        records_list = records_list.filter(code__icontains=code_filter)
    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'soato.html', {'page_obj': page_obj})

def oked(request):
    records_list = OPF.objects.all()
    code_filter = request.GET.get('code')
    name_uzl_filter = request.GET.get('name_uzl')

    if code_filter:
        records_list = records_list.filter(code__icontains=code_filter)
    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'oked.html', {'page_obj': page_obj})

def opf(request):
    records_list = OPF.objects.all()
    code_filter = request.GET.get('code')
    name_uzl_filter = request.GET.get('name_uzl')

    if code_filter:
        records_list = records_list.filter(code__icontains=code_filter)
    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'opf.html', {'page_obj': page_obj})

def okonx(request):
    records_list = OKONX.objects.all()
    code_filter = request.GET.get('code')
    name_uzl_filter = request.GET.get('name_uzl')

    if code_filter:
        records_list = records_list.filter(code__icontains=code_filter)
    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'okonx.html', {'page_obj': page_obj})

def soogu(request):
    records_list = SOOGU.objects.all()
    code_filter = request.GET.get('code')
    name_uzl_filter = request.GET.get('name_uzl')

    if code_filter:
        records_list = records_list.filter(code__icontains=code_filter)
    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'soogu.html', {'page_obj': page_obj})

def fs(request):
    records_list = FS.objects.all()
    code_filter = request.GET.get('code')
    name_uzl_filter = request.GET.get('name_uzl')

    if code_filter:
        records_list = records_list.filter(code__icontains=code_filter)
    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'fs.html', {'page_obj': page_obj})

def doctype(request):
    records_list = DOCTYPE.objects.all()
    name_uzl_filter = request.GET.get('name_uzl')

    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'doctype.html', {'page_obj': page_obj})

def country(request):
    records_list = COUNTRY.objects.all()
    name_uzl_filter = request.GET.get('name_uzl')

    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'country.html', {'page_obj': page_obj})

def country(request):
    records_list = COUNTRY.objects.all()
    name_uzl_filter = request.GET.get('name_uzl')

    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'country.html', {'page_obj': page_obj})

def nation(request):
    records_list = NATION.objects.all()
    name_uzl_filter = request.GET.get('name_uzl')

    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'nation.html', {'page_obj': page_obj})

def login(request):
    template = loader.get_template('admin/login.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('admin/register.html')
    return HttpResponse(template.render())