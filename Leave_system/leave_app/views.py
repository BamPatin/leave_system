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

def info(request):
    try:
        person=Person.objects.get(username=request.username)
    except Exception as e:
        person = None
        print('Exception : ', e)

    context = {
        'person': person,
    }

    return render(request, 'info.html')

def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    #try:
        #   user = Person.objects.get(username=username , password=password)
    #except:
        #   user = None
    user=auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        user.position = user.position.upper()
        if user.position=='HR':
            return redirect('/hr')
        elif user.position=='BOSS':
            return redirect('/leader')
        else:
            return redirect('/info')
    else:
        messages.info(request, 'Username or Password is incorrect')
        return redirect('/')
        
def hr(request):
    return render(request, 'hr.html')

def leader(request):
    return render(request, 'leader.html')

def createForm(request):
    return render(request, 'createForm.html')

def addForm(request):
    if request.method == "POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        nickname=request.POST.get('nickname')
        tel=request.POST.get('tel')
        team=request.POST.get('team')
        position=request.POST.get('position')
        email=request.POST.get('email')
        password=request.POST.get('password')
        leader=request.POST.get('leader')

        person=Person.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            tel=tel,
            team=team,
            position=position,
            email=email,
            password=password,
            leader=leader
        )
        person.set_password(password)  #แปลงpasswordเป็นการเข้ารหัส
        person.save()
        number = Number.objects.create(username=person)
        number.save()
        
        return render(request, "result.html")

    else:
        return render(request, "createForm.html")
    
def result(request):
    return render(request, 'result.html')

def formleave(request) :
    if request.method == "POST" :
        #รับข้อมูล
        username_id = request.user.id           #ข้อมูลของผู้login
        typeleave = request.POST["typeleave"]
        numberleave = request.POST["numberleave"]
        From_Date = request.POST["From_Date"]
        To_Date = request.POST["To_Date"]
        reason = request.POST["reason"]
        
        number_instance = Number.objects.filter(username_id=username_id).first()

        if typeleave =='S' :
           if number_instance.sick < int(numberleave) :
               messages.success(request,"วันลาป่วยของคุณไม่เพียงพอ กรุณากรอกฟอร์มขอลาใหม่อีกครั้ง")
               return redirect('/formleave')        
            
        elif typeleave =='P' :
            if number_instance.personal < int(numberleave) :
               messages.success(request,"วันลากิจของคุณไม่เพียงพอ กรุณากรอกฟอร์มขอลาใหม่อีกครั้ง")
               return redirect('/formleave')      
           
        else :
            if number_instance.vacation < int(numberleave) :
               messages.success(request,"วันลาพักร้อนของคุณไม่เพียงพอ กรุณากรอกฟอร์มขอลาใหม่อีกครั้ง")
               return redirect('/formleave')  
        
        #บันทึกข้อมูล
        form = Form.objects.create(
            # name=name,
            # email=email,
            username_id = username_id,
            typeleave=typeleave,
            numberleave=numberleave,
            From_Date = From_Date,
            To_Date = To_Date,
            reason = reason
        )
        form.save()
        # messages.success(request,"บันทึกข้อมูลเรียบร้อย")

        leader = request.user.leader
        person_instance = Person.objects.filter(username=leader).first()

        leader_email = person_instance.email

        # send email
        subject = 'Test Email : Leave System'
        body = '''
            <p> เรื่อง ขออนุญาติลา </p>
            .......................
        '''
        email = EmailMessage(subject=subject , body=body , to=[leader_email])
        email.content_subtype = 'html'
        email.send()
        # messages.success(request,"รอการยืนยัน")
        #เปลี่ยนเส้นทาง
        return redirect('/status')        
    return render(request, 'formleave.html') 


    
        
def status(request) :
    # if request.method == "POST" :
    username_id = request.user.id 
    all_person = Form.objects.filter(username_id=username_id) 
    all_number = Number.objects.filter(username_id=username_id) 
    return render(request,"status.html",{"all_person":all_person , "all_number":all_number})

   
def approve(request) :
    username = request.user.username
    allow = Form.objects.filter(username__leader=username,show=0)
    return render(request,"approve.html",{"allow":allow})


def success(request,person_id):
    # เรียกใช้ข้อมูลจากโมเดล Form
    form_instance = Form.objects.get(pk=person_id)
    numberleave_value = form_instance.numberleave
    typeleave_value = form_instance.typeleave
    
    form_instance.show = 1  #เปลี่ยนเป็นTrue
    form_instance.save() 
    
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
    
    # เรียกใช้ข้อมูลจากโมเดล Person
    person_instance = Person.objects.filter(username=form_instance.username).first()
    person_email = person_instance.email


    subject = 'Test Email'
    body = '''
        <p> mission complete  </p>
    '''
    email = EmailMessage(subject=subject , body=body , to=[person_email])
    email.content_subtype = 'html'
    email.send()
    # messages.success(request,"อนุมัติคำขอของคุณ")
    return redirect("/approve")



def unsuccess(request,person_id) :
    form_instance = Form.objects.get(pk=person_id)
    form_instance.show = 1  #เปลี่ยนเป็นTrue
    form_instance.save() 
    
    # เรียกใช้ข้อมูลจากโมเดล Person
    person_instance = Person.objects.filter(username=form_instance.username).first()
    person_email = person_instance.email
    
    subject = 'Test Email'
    body = '''
        <p> mission fail  </p>
    '''
    email = EmailMessage(subject=subject , body=body , to=[person_email])
    email.content_subtype = 'html'
    email.send()
    # messages.success(request,"ไม่อนุมัติคำขอของคุณ")
    return redirect("/approve")

def logout(request):
    auth.logout(request)
    return redirect('/')