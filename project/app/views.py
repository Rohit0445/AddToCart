
from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

# Create your views here.


   

def landing(req):

    items = Item.objects.all()
   

    if req.method == 'POST':
        form = ItemForm(req.POST, req.FILES)  # include request.FILES for image
        if form.is_valid():
            form.save()
            return redirect('landing')  # redirect after saving
        else:
          form = ItemForm()
    
        return render(req, 'landing.html', {'form': form})

    return render(req,'landing.html',{'items': items})


def addtocart(req,pk):
    cart = req.session.get('cart',[])
    
    x=cart.append(pk)
    # print(cart)
    req.session['cart']=x
    form = ItemForm()
    items = Item.objects.all()
    return render(req,'landing.html',{'items': items})

def cart(req):
    cart = req.session.get('cart',[])
    print(cart)

    
    


    
    
    

