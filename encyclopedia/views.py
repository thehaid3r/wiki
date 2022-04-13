from django.shortcuts import render ,redirect
import markdown2
from . import util
from encyclopedia.forms import new
import secrets


def index(request):
    entries= util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def wiki(request,title: str):
    if title.casefold() in map(str.casefold,util.list_entries()):
        entry=util.get_entry(title)
        
        return render(request,'encyclopedia/entry.html',context={
            'entry':markdown2.markdown(entry),
            'entry1':title
            })

    else:
        return redirect('notfound')

def notfound(request):
    return render(request,'encyclopedia/notfound.html')

def searchbar(request):
    q=request.GET.get('q')
    entries= util.list_entries()
    entry_list=[]
    for entry in entries :
        if q.lower() == entry.lower():
            return redirect('wiki',entry)
        elif q.lower() in entry.lower() :
            entry_list.append(entry)
    if entry_list==[]:
            return redirect('notfound') 
    else :      
        return render(request,'encyclopedia/searchbar.html',context={
            'entry_list':entry_list,
        })
def new_entry(request):
    form=new()
    if request.method=='POST':
        form=new(request.POST)
        if form.is_valid() :
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title.casefold() in map(str.casefold,util.list_entries()):
                return render(request,'encyclopedia/new_entry.html',context={
                    'title':title,
                    'true':True,
                    'form':form
                    })
            else :
                util.save_entry(title,content)
                return redirect('wiki',title)
        
        
            

    return render(request,'encyclopedia/new_entry.html',context={
        'true':False,
        'form':form
    })
def edit(request,title: str):
    if request.method=='POST':
        form=new(request.POST)
        if form.is_valid() :
            title1 = form.cleaned_data["title"]
            content1 = form.cleaned_data["content"]
            util.save_entry(title1,content1)
            return redirect('wiki',title1)
    else:        
        if title.casefold() in map(str.casefold,util.list_entries()):
            print("title")
            form=new()
            form.fields["title"].initial=title
            form.fields["content"].initial=util.get_entry(title)
            return render(request,'encyclopedia/edit.html',context={
                'form':form,
                'form1':form.fields["title"].initial,
                'form2':form.fields["content"].initial
            })
        else:
            print(title)    
        return render(request,'encyclopedia/edit.html')    
def random(request):
    return redirect('wiki',secrets.choice(util.list_entries()))

