from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'name':'Mahendra SINGH DhOni','count':1,'dt':dt}
    return render(request,'filters.html',d)

def userfilters(request):
    d={'name':'Mahendra SINGH Dhoni','g1':'AsdfGklm MnBHjkjh'}
    return render(request,'userfilters.html',d)