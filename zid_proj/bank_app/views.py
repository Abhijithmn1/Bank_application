from django.shortcuts import render


from .models import District, Branch


def index(request):
    return render(request, 'index.html')


def form_page(request):
    districts = District.objects.all()
    branches_by_district = {district: Branch.objects.filter(district=district) for district in districts}
    return render(request, 'form.html', {'districts': districts, 'branches_by_district': branches_by_district})


def submit_form(request):

    message = "Application accepted"
    return render(request, 'message.html', {'message': message})