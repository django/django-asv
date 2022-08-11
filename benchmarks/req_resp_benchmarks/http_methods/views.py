from django.http import HttpResponse

def test_view(request):
    if request.method == "GET":
        return HttpResponse("GET method")
    if request.method == "POST":
        return HttpResponse("POST method")
