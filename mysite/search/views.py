# # Create your views here.
# from .models import Zipcode
# from django.shortcuts import render
# from .filters import ZipCodeFilter

# def search(request):
#     zipcode_list = Zipcode.objects.all()
#     zipcode_filter = ZipCodeFilter(request.GET, queryset=zipcode_list)
#     print("zipcode_filter : ",zipcode_filter)
    return render(request, 'search/zipcode_list.html', {'filter': zipcode_filter}