from django.shortcuts import render

# Create your views here.

def post_list(request):                                       #function takes request and returns the value from rendering template
    return render(request, 'pages/post_list.html')
