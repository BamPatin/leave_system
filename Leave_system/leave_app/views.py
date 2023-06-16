from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from leave_app.models import Form , Number


# Create your views here.
def home(request) :
    return render(request,"home.html")

def formleave(request) :
    if request.method == "POST" :
        #รับข้อมูล
        # date = request.POST["date"]
        # id
        # name
        name = request.POST["name"]
        email = request.POST["email"]
        typeleave = request.POST["typeleave"]
        numberleave = request.POST["numberleave"]
        From_Date = request.POST["From_Date"]
        To_Date = request.POST["To_Date"]

        #บันทึกข้อมูล

        form = Form.objects.create(
            name=name,
            email=email,
            typeleave=typeleave,
            numberleave=numberleave,
            From_Date = From_Date,
            To_Date = To_Date
        )
        form.save()
        # messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        
        # send email
        subject = 'Test Email'
        body = '''
            <p> This is a test maill messege </p>
        '''
        email = EmailMessage(subject=subject , body=body , to=['patinya.bamm@gmail.com'])
        email.content_subtype = 'html'
        email.send()
        messages.success(request,"รอการยืนยัน")
        #เปลี่ยนเส้นทาง
        return redirect("/")

    else:
        return render(request,"formleave.html")
    
        # sick = request.POST["sick"]
        # personal = request.POST["personal"]
        # vacation = request.POST["vacation"]
        
def status(request) :
    all_person = Form.objects.all()
    return render(request,"status.html",{"all_person":all_person})
   
def approve(request) :
    all_person = Form.objects.all()
    return render(request,"approve.html",{"all_person":all_person})

def success(request) :
    subject = 'Test Email'
    body = '''
        <p> mission complete  </p>
    '''
    email = EmailMessage(subject=subject , body=body , to=['patinya.bamm@gmail.com'])
    email.content_subtype = 'html'
    email.send()
    messages.success(request,"อนุมัติคำขอของคุณ")
    return redirect("/")

def unsuccess(request) :
    subject = 'Test Email'
    body = '''
        <p> mission fail  </p>
    '''
    email = EmailMessage(subject=subject , body=body , to=['patinya.bamm@gmail.com'])
    email.content_subtype = 'html'
    email.send()
    messages.success(request,"ไม่อนุมัติคำขอของคุณ")
    return redirect("/")