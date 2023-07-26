from django.shortcuts import render
from .models import District, Branch


def index(request):
    return render(request, 'index.html')


def confirmation(request):
    return render(request, 'message.html')


def form_page(request):
    if request.method == 'POST':
        return redirect('confirmation')

    districts = District.objects.all()
    branches_by_district = {district: Branch.objects.filter(district=district) for district in districts}
    return render(request, 'form.html', {'districts': districts, 'branches_by_district': branches_by_district})


