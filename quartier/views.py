# from django.http  import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import NeighborHood,BusinessClass,Profile
from .forms import NewProfileForm,NewBizForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user=request.user
    neighbors= NeighborHood.objects.all()
    profile=Profile.objects.filter(user=current_user).first() 
    return render(request,'index.html',{'neighbor':neighbors,'profile':profile})

@login_required(login_url='/accounts/login/')
def neighborhood(request,neighborhood_id):
    if request.user.id == 1:
        current_user=request.user
        neighbors= NeighborHood.objects.get(id=neighborhood_id)
        print(neighbors)
        biz=BusinessClass.objects.filter(neighborhood=neighbors.id).all()
        profile=Profile.objects.filter(id=current_user.id).first()
        return render(request,'neighborhood.html',{'business':biz,'neighbors':neighbors,'neighborhood_id':neighborhood_id})    

    

@login_required(login_url='/accounts/login/')
def new_business(request):

    current_user = request.user
    if request.method == 'POST':

        form = NewBizForm(request.POST, request.FILES)
        if form.is_valid():
            b_post = form.save(commit=False)
            b_post.user = current_user
            b_post.save()
            return redirect('profile')
       

    else:
        form = NewBizForm()
        return render(request,'new_business.html', {"form": form})


@login_required(login_url='/accounts/login/')
def new_profile(request):
    
    current_user = request.user
    profile=Profile.objects.filter(user=current_user).first()
    if request.method == 'POST':

        form = NewProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('profilee')
       

    else:
        form = NewProfileForm(instance=profile)
         
    return render(request,'profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def myprofile(request):
     current_user= request.user
     profile=Profile.objects.filter(user=current_user).first()
     return render(request,'p.html',{"profile":profile})                



