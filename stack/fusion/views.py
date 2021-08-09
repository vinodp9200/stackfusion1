from django.shortcuts import render,HttpResponse,redirect
from .models import userform
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method=='POST':
        n=request.POST.get('name')
        d=request.POST.get('dob')
        e=request.POST.get('email')
        p=request.POST.get('phone')
        send_mail(
            'Thanks for register stackfusion',
            'Hi {},\nyour form successfully applied and i will conduct you as soon as possible.'
            '\n\n Thanks and Regards\nVinod Pal'.format(n),
            'palvinodr1996@gmail.com',
            [e],
            fail_silently=False,
        )
        data=userform()
        data.name=n
        data.dob=d
        data.email=e
        data.phone_number=p
        data.save()
        return redirect('/showall')

    return render(request,'index.html')


def showallsub_data(request):
    data=userform.objects.all().order_by('-id')
    context={'data':data}
    return render(request,'alluser.html',context)

