from django.shortcuts import render, redirect
from .models import PersonalDetils
from customer_dashboard.services import get_dashboard_data
def customerDashboard(request):
    context = get_dashboard_data(request.user)
    return render(request, 'customer_dashboard/customer_dashboard.html',context)

def cmOrdersHistory(request):

    return render(request, 'customer_dashboard/cm_orders.html')

def cmPersonalDetails(request):
    context = get_dashboard_data(request.user)
    return render(request, 'customer_dashboard/cm_personal_details.html', context)

def cmPersonalDetailsForm(request):
    if request.method=="POST":

        avtar = request.FILES.get('avatar')
        name = request.get('name')
        phone = request.get('phone')
        gender = request.get('gender')
        address = request.gety('address')
        PersonalDetils.objects.create(
            avtar=avtar,
            name=name,
            phone=phone,
            gender=gender,
            address=address
        )
        return redirect("cm_personal_details")
    
    return render(request, 'customer_dashboard/update_rsonal_details.html')
