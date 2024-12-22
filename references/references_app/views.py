from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Soato, OPF, OKONX, SOOGU, FS, DOCTYPE, COUNTRY, NATION
from django.core.paginator import Paginator
from account.models import Category,TableHeader, TableRow
from openpyxl import load_workbook
from django.contrib.auth.decorators import login_required
import openpyxl
from openpyxl.styles import Alignment
from datetime import datetime

def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def generic_list_view(request, model, template_name, extra_context=None):
    # Fetch all records from the model
    records_list = model.objects.all()
    code_filter = request.GET.get('code')
    name_uzl_filter = request.GET.get('name_uzl')
    name_ru_filter = request.GET.get('name_ru')

    # Apply filters if present
    if code_filter:
        records_list = records_list.filter(code__icontains=code_filter)
    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)
    if name_ru_filter:
        records_list = records_list.filter(name_ru__icontains=name_ru_filter)

    if request.GET.get('export') == 'excel':
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = f"{model.__name__} Data"

        fields = [field.name for field in model._meta.fields]
        for col_num, field_name in enumerate(fields, start=1):
            cell = sheet.cell(row=1, column=col_num, value=field_name)
            cell.alignment = Alignment(horizontal="center")

        for row_num, record in enumerate(records_list, start=2):
            for col_num, field_name in enumerate(fields, start=1):
                value = getattr(record, field_name, '')
                # Convert timezone-aware datetime to naive datetime
                if isinstance(value, datetime) and value.tzinfo is not None:
                    value = value.astimezone(None).replace(tzinfo=None)
                sheet.cell(row=row_num, column=col_num, value=value)

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = f'attachment; filename="{model.__name__}_data.xlsx"'
        workbook.save(response)
        return response

    paginator = Paginator(records_list, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = records_list.count()

    context = {
        'page_obj': page_obj,
        'count': count,
    }
    if extra_context:
        context.update(extra_context)

    return render(request, template_name, context)
def soato(request):
    return generic_list_view(request, Soato, 'soato.html' )


def oked(request):
    return generic_list_view(request, OPF, 'oked.html')

def opf(request):
    return generic_list_view(request, OPF, 'opf.html')

def okonx(request):
    return generic_list_view(request, OKONX, 'okonx.html')

def soogu(request):
    return generic_list_view(request, SOOGU, 'soogu.html')

def fs(request):
    return generic_list_view(request, FS, 'fs.html')

def doctype(request):
    return generic_list_view(request, DOCTYPE, 'doctype.html')

def country(request):
    return generic_list_view(request, COUNTRY, 'country.html')

def nation(request):
    return generic_list_view(request, NATION, 'nation.html')

def reflists(request):
    references = [
        {'type': 'reference', 'title': 'soato', 'description': 'soato_text', 'link': 'soato', 'count': Soato.objects.count()},
        {'type': 'reference', 'title': 'oked', 'description': 'oked_text', 'link': 'oked', 'count': OPF.objects.count()},
        {'type': 'reference', 'title': 'okonx', 'description': 'okonx_text', 'link': 'okonx', 'count': OKONX.objects.count()},
        {'type': 'reference', 'title': 'opf', 'description': 'opf_text', 'link': 'opf', 'count': OPF.objects.count()},
        {'type': 'reference', 'title': 'fs', 'description': 'fs_text', 'link': 'fs', 'count': FS.objects.count()},
        {'type': 'reference', 'title': 'soogu', 'description': 'soogu_text', 'link': 'soogu', 'count': SOOGU.objects.count()},
        {'type': 'reference', 'title': 'doctype', 'description': 'doctype_text', 'link': 'doctype', 'count': DOCTYPE.objects.count()},
        {'type': 'reference', 'title': 'country', 'description': 'country_text', 'link': 'country', 'count': COUNTRY.objects.count()},
        {'type': 'reference', 'title': 'nation', 'description': 'nation_text', 'link': 'nation', 'count': NATION.objects.count()},
    ]

    categories = Category.objects.all()

    categories_list = []
    for category in categories:
        headers = TableHeader.objects.filter(references_category=category)
        column_count = len(headers)  # Total columns for the category

        categories_list.append({
            'type': 'category',
            'id': category.id,
            'category_name': category.category_name,
            'category_decription': category.category_decription,
            'cell_count': column_count,  
        })

    combined_list = references + categories_list

    paginator = Paginator(combined_list, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/references.html', {
        'page_obj': page_obj,
    })

def category_search(request):
    query = request.GET.get('keyword', '') 
    categories = Category.objects.filter(category_name=query) if query else Category.objects.all()

    return render(request, 'pages/search_page.html', {'categories': categories, 'query': query})

def import_classifier(request):
    if request.method == 'POST' and request.FILES.get('file'):
        excel_file = request.FILES['file']
        
        try:
            workbook = load_workbook(excel_file)
            sheet = workbook.active
            for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header row
                if any(row): 
                    try:
                        id, version, code, s_comment, s_create, s_status, name_ru, name_uz, name_uzl, name_short_ru, name_short_uz, name_short_uzl, s_user_id  = row
                        
                        # Debug: print data to inspect
                        # Convert fields to appropriate types where necessary
                        version = int(version) if version is not None else 0
                        s_user_id = int(s_user_id) if s_user_id is not None else None
                        
                        # Create a new SOOGU object and save it
                        COUNTRY.objects.create(
                            id=int(id),
                            version=version,
                            code=code,
                            s_comment=s_comment,
                            s_create=s_create,
                            s_status=s_status,
                            name_ru=name_ru,
                            name_uz=name_uz,
                            name_uzl=name_uzl,
                            name_short_ru=name_short_ru,
                            name_short_uz=name_short_uz,
                            name_short_uzl=name_short_uzl,
                            s_user_id=s_user_id,
                            
                        )

                    except Exception as e:
                        # Log any error in case of data mismatch or missing values
                        print(f"Error importing row: {row} - {e}")
                        continue

        except Exception as e:
            # Log any critical errors related to file processing
            return HttpResponse(f"Failed to process file: {e}")

        return HttpResponse("File uploaded and data imported successfully!")

    return render(request, 'import_classifier.html')

@login_required
def references(request):
    records_list = DOCTYPE.objects.all()
    name_uzl_filter = request.GET.get('name_uzl')

    if name_uzl_filter:
        records_list = records_list.filter(name_uzl__icontains=name_uzl_filter)

    paginator = Paginator(records_list, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'admin/references.html', {'page_obj': page_obj})
