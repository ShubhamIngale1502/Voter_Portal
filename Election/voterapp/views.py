from django.shortcuts import render, redirect
from .forms import VoterForm
from .models import Voter

def create(request):
    template_name = 'voterapp/insert.html'
    form = VoterForm()
    if request.method == 'POST':
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    context = {'forms':form}
    return render(request, template_name,context)

def show_Details(request):
    template_name = 'voterapp/show.html'
    data = Voter.objects.all()
    context = {'voters':data}
    return render(request, template_name,context)

def candidate_details(request,pk):
    template_name = 'voterapp/candidate.html'
    data = Voter.objects.get(pk=pk)
    context = {'voter':data}
    return render(request,template_name,context)

def update_Details(request,pk):
    template_name = 'voterapp/insert.html'
    obj = Voter.objects.get(pk=pk)
    form = VoterForm(instance=obj)
    if request.method == 'POST':
        form = VoterForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show')
    context = {'forms': form}
    return render(request, template_name,context)

def delete_Details(request,pk):
    template_name = 'voterapp/delete.html'
    obj = Voter.objects.get(pk=pk)
    if request.method == 'GET':
        context = {'forms': obj}
        return render(request, template_name,context)
    obj.delete()
    return redirect('show')


