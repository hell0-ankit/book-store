from django.shortcuts import render
def customerDashboard(request):
    return render(request, 'customer_dashboard/customer_dashboard.html')

def cmOrdersHistory(request):

    return render(request, 'customer_dashboard/cm_orders.html')

def cmPersonalDetails(request):
    
    return render(request, 'customer_dashboard/cm_personal_details.html')

def cmPersonalDetailsForm(request):
    
    return render(request, 'customer_dashboard/update_rsonal_details.html')
