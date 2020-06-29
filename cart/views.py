from django.shortcuts import render
# Create your views here.
def addcart(request):
    if request.method == "POST":
        name = request.POST['NAME']
    else:
        print('some errors')
    print(name)
    return render(request, "cart/cart.html", {'name': name})

