from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from django.forms import modelformset_factory
from django.http import HttpResponse
from django import forms
import openpyxl
from openpyxl.styles import Alignment
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from .models import TableHeader, TableRow, Category, User
from django.core.paginator import Paginator
from .forms import CategoryForm, TableHeaderForm, TableRowForm

def index(request):
    return render(request, 'admin/index.html')

def settings(request):
    return render(request, 'admin/settings.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.user.is_authenticated:
        return redirect('/account/adminpage')

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = request.POST.get('remember_me')  # Get the value of "Remember Me" checkbox
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                if not remember_me:
                    request.session.set_expiry(0)  
                else:
                    request.session.set_expiry(1209600)  
                if user.is_staff:
                    return redirect('adminpage')
                else:
                    return redirect('adminpage')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'

    return render(request, 'admin/login.html', {'form': form, 'msg': msg})

def logout_view(request):
    logout(request)  
    return redirect('/account/login/')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data['role']
            if role == 'admin':
                user.is_admin = True
                user.is_user = False
            else:
                user.is_admin = False
                user.is_user = True

            user.set_password(form.cleaned_data['password1']) 
            user.save() 
            msg = 'User created successfully'
            return redirect('login_view') 
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, 'admin/register.html', {'form': form, 'msg': msg})

@login_required
def admin(request):
    return render(request,'admin/dashboard.html')

@login_required
def users(request):
    if not request.user.is_admin:
        return HttpResponseForbidden("You do not have permission to view this page.")
    form = SignUpForm1()
    if request.method == "POST":
        if 'edit-user' in request.POST: 
            user_id = request.POST.get('user_id')
            username = request.POST.get('username')  
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            user = get_object_or_404(User, id=user_id)
            if username:  
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                return redirect('users')

        elif 'add-user' in request.POST:  
            form = SignUpForm1(request.POST)
            if form.is_valid():
                form.save() 
                return redirect('users')


        elif 'delete-user' in request.POST:  
            user_id = request.POST.get('user_id')
            user = get_object_or_404(User, id=user_id)
            user.delete()
            return redirect('users')
        
    all_users = User.objects.all()
    return render(request, 'admin/users.html', {'all_users': all_users, 'form': form,})

class SignUpForm1(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': ''
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': ''
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': ''
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': ''
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control', 
                'placeholder': ''
            }),
        }
    # Ensure the password is saved securely
    def save(self, commit=True):
        user = super(SignUpForm1, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

@login_required
def account_view(request):
    user = request.user  
    context = {
        'username': user.username, 
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,  
        'is_admin': user.is_admin, 
        'is_user': user.is_user,  
    }
    return render(request, 'admin/account.html', context)
@login_required
def category_list(request):
    if request.user.is_admin:
        categories = Category.objects.all()
    else:
        categories = Category.objects.filter(user=request.user)
    form = CategoryForm()

    if request.method == "POST":
        if 'edit-category' in request.POST: 
            category_id = request.POST.get('category_id')
            category_name = request.POST.get('category_name')  
            category_decription = request.POST.get('category_decription')
            category = get_object_or_404(Category, id=category_id)
            if category_name:  
                category.category_name = category_name
                category.category_decription = category_decription
                category.save()
                return redirect('adminpage/katalog')

        elif 'add-category' in request.POST:  
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=False)
                category.user = request.user
                category.save()
                return redirect('adminpage/katalog')

        elif 'delete-category' in request.POST:  
            category_id = request.POST.get('category_id')
            category = get_object_or_404(Category, id=category_id)
            category.delete()
            return redirect('adminpage/katalog')

    paginator = Paginator(categories, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': page_obj,
        'form': form,
        'paginator': paginator,
        'page_obj': page_obj,
    }
    return render(request, 'admin/category_list.html', context)

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('katalog')  
    else:
        form = CategoryForm()
    
    return render(request, 'admin/create_category.html', {'form': form})

@login_required
def manage_table_headers(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == "DELETE" and "header_id" in request.GET:
        header_id = request.GET.get("header_id")
        try:
            table_header = TableHeader.objects.get(pk=header_id, references_category=category)
            table_header.delete()
            return JsonResponse({"success": True, "message": "Table header deleted successfully."})
        except TableHeader.DoesNotExist:
            return JsonResponse({"success": False, "message": "Table header not found."}, status=404)

    if request.method == "POST" and "edit_header_id" in request.POST:
        header_id = request.POST.get("edit_header_id")
        header_name = request.POST.get("edit_header_name")
        try:
            table_header = TableHeader.objects.get(pk=header_id, references_category=category)
            table_header.header_name = header_name
            table_header.save()
            return JsonResponse({"success": True, "message": "Table header updated successfully."})
        except TableHeader.DoesNotExist:
            return JsonResponse({"success": False, "message": "Table header not found."}, status=404)

    TableHeaderFormSet = modelformset_factory(
        TableHeader,
        form=TableHeaderForm,
        extra=1,  
        can_delete=True,
    )

    table_headers = TableHeader.objects.filter(references_category=category)

    if request.method == "POST":
        formset = TableHeaderFormSet(request.POST, queryset=table_headers)

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                if not instance.pk: 
                    instance.category = category
                    instance.references_category = category
                instance.save()

            return redirect("manage_table_headers", category_id=category.id)
        else:
            print(formset.errors) 
    else:
        formset = TableHeaderFormSet(queryset=table_headers)

    return render(
        request,
        "admin/manage_table_headers.html",
        {"formset": formset, "category": category},
    )

@login_required
def manage_table_rows(request, category_id, header_id):
    
    header = get_object_or_404(TableHeader, id=header_id)
    category = get_object_or_404(Category, id=category_id)

    table_rows = TableRow.objects.filter(references_category=category_id, header=header )

    TableRowFormSet = modelformset_factory(
        TableRow,
        form=TableRowForm,
        extra=1,  
        can_delete=True,  
    )

    if request.method == "DELETE" and "row_id" in request.GET:
        row_id = request.GET.get("row_id")
        try:
            table_row = TableRow.objects.get(pk=row_id, references_category=category, header=header)
            table_row.delete()
            return JsonResponse({"success": True, "message": "Table row deleted successfully."})
        except TableRow.DoesNotExist:
            return JsonResponse({"success": False, "message": "Table row not found."}, status=404)
        
      
    if request.method == "POST" and "edit_row_id" in request.POST:
        row_id = request.POST.get("edit_row_id")
        row_name = request.POST.get("edit_row_name")
        try:
            table_row = TableRow.objects.get(pk=row_id, references_category=category)
            table_row.row_name = row_name
            table_row.save()
            return JsonResponse({"success": True, "message": "Table row updated successfully."})
        except TableRow.DoesNotExist:
            return JsonResponse({"success": False, "message": "Table row not found."}, status=404)

    if request.method == "POST":
        formset = TableRowFormSet(request.POST, queryset=table_rows)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                if not instance.pk: 
                    instance.references_category = category  
                    instance.category_id = category.id
                instance.header = header
                instance.save()

            for form in formset.forms:
                if form.cleaned_data.get("DELETE"):
                    if form.instance.pk: 
                        print(f"Deleting: {form.instance}") 
                        form.instance.delete()
                        
            formset.save()
            return redirect("manage_table_rows", category_id=category.id, header_id=header_id)
        else:
            print(formset.errors)
    else:
        formset = TableRowFormSet(queryset=table_rows)

    return render(
        request,
        "admin/manage_table_rows.html",  
        {
            "formset": formset,
            "header": header,
            "category_id": category.id,
        },
    )
def references_table(request, category_id):
    category = get_object_or_404(Category, id=category_id)
   
    headers = TableHeader.objects.filter(references_category=category)
    rows = TableRow.objects.filter(references_category=category)

    table_data = []
    for header in headers:
        table_data.append({
            'header': header.header_name,  # Assuming headers have a `title` field
            'rows': rows.filter(header=header),  
        })

    rows_grouped = []
    total_cell_count = 0  
    max_row_count = max(len(item['rows']) for item in table_data) if table_data else 0

    for i in range(max_row_count):
        row = []
        for item in table_data:
            cell = getattr(item['rows'][i], 'row_name', '') if i < len(item['rows']) else ''  # Assuming rows have a `value` field
            row.append(cell)
            if cell:
                total_cell_count += 1
        rows_grouped.append(row)

    # Check if export is requested
    if request.GET.get('export') == 'excel':
        # Create an Excel workbook
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = f"{category.category_name} Data"

        # Write headers
        for col_num, header in enumerate([item['header'] for item in table_data], start=1):
            cell = sheet.cell(row=1, column=col_num, value=header)
            cell.alignment = Alignment(horizontal="center")

        # Write data rows
        for row_num, row in enumerate(rows_grouped, start=2):
            for col_num, cell_value in enumerate(row, start=1):
                sheet.cell(row=row_num, column=col_num, value=cell_value)

        # Prepare the response for file download
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = f'attachment; filename="{category.category_name}_data.xlsx"'
        workbook.save(response)
        return response

    # Handle normal view rendering
    paginator = Paginator(rows_grouped, 15)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    context = {
        'category': category,
        'table_data': table_data,
        'rows_grouped': page_obj,  
        'paginator': paginator,   
        'total_cell_count': total_cell_count,
    }
    return render(request, 'pages/references_table.html', context)


# def admin(request):
#     return render(request,'admin.html')


# def user(request):
#     return render(request,'user.html')