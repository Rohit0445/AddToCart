
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
