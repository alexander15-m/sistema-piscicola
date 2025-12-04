from django.shortcuts import render

def dashboard(request):
    context = {
        "total_inversion": 1500,
        "total_alimento": 500,
        "total_ventas": 2200,
        "utilidad": 700,
    }
    return render(request, "dashboard.html", context)