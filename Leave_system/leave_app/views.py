from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from leave_app.models import Form , Number ,Person
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate


# Create your views here.
def home(request) :
    return render(request,"home.html")

def login(request) :
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username , password=password)

        if user is not None :
            auth.login(request,user)
            messages.success(request,"เข้าสู่ระบบสำเร็จ")
            return redirect('/formleave')
        else :
            messages.success(request,"ไม่สามารถเข้าสู่ระบบได้")
            return redirect('/')
    #else:
    #   form = LoginForm()
    return render(request, 'home.html') #, {'form': form})

def formleave(request) :
    if request.method == "POST" :
        #รับข้อมูล
        # date = request.POST["date"]
        # id
        # name
        # name = request.POST["name"]
        # email = request.POST["email"]
        username_id = request.user.id           #ข้อมูลของผู้login
        username = request.user.username
        typeleave = request.POST["typeleave"]
        numberleave = request.POST["numberleave"]
        From_Date = request.POST["From_Date"]
        To_Date = request.POST["To_Date"]
        reason = request.POST["reason"]


        #บันทึกข้อมูล

        form = Form.objects.create(
            # name=name,
            # email=email,
            username_id = username_id,
            username = username,
            typeleave=typeleave,
            numberleave=numberleave,
            From_Date = From_Date,
            To_Date = To_Date,
            reason = reason
        )
        # person = Person.objects.get(id=person_id) 
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
        return redirect('/status')
    # else :
    #     return redirect('/')
    
    return render(request, 'formleave.html') 


    
        
def status(request) :
    # if request.method == "POST" :
    username_id = request.user.id 
    all_person = Form.objects.filter(username_id=username_id) 
    all_number = Number.objects.filter(username_id=username_id) 
    return render(request,"status.html",{"all_person":all_person , "all_number":all_number})

   
def approve(request) :
    username = request.user.username
    allow = Form.objects.filter(username__leader=username)
    return render(request,"approve.html",{"allow":allow})

def success(request,person_id):
    # เรียกใช้ข้อมูลจากโมเดล Form
    form_instance = Form.objects.get(pk=person_id)
    numberleave_value = form_instance.numberleave
    typeleave_value = form_instance.typeleave

    # เรียกใช้ข้อมูลจากโมเดล Number
    number_instance = Number.objects.filter(username=form_instance.username).first()
    
    if typeleave_value =='S' :
        leave_value = number_instance.sick
        number_instance.sick = leave_value - numberleave_value
    elif typeleave_value =='P' :
        leave_value = number_instance.personal
        number_instance.personal = leave_value - numberleave_value
    else :
        leave_value = number_instance.vacation
        number_instance.vacation = leave_value - numberleave_value
        
    number_instance.save()       



    subject = 'Test Email'
    body = '''
        <p> mission complete  </p>
    '''
    email = EmailMessage(subject=subject , body=body , to=['patinya.bamm@gmail.com'])
    email.content_subtype = 'html'
    email.send()
    messages.success(request,"อนุมัติคำขอของคุณ")
    return redirect("/approve")




def unsuccess(request) :
    subject = 'Test Email'
    body = '''
        <p> mission fail  </p>
    '''
    email = EmailMessage(subject=subject , body=body , to=['patinya.bamm@gmail.com'])
    email.content_subtype = 'html'
    email.send()
    messages.success(request,"ไม่อนุมัติคำขอของคุณ")
    return redirect("/approve")