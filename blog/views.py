from django.http import HttpResponse

# blog views
def home(request):
    return HttpResponse("Welcome home!")

def about(request):
    return HttpResponse("About")

def post_detail(request, pk):
    return HttpResponse(f"Post #{pk}")