from django.shortcuts import render
import pymysql as mysql
from django.contrib import auth

def ActionAdminLogin(request):
    return render(request,'NewAdminLogin.html',{'msg':''})

def ActionCheckLogin(request):
    adminid=request.POST['adminid']
    password=request.POST['password']
    try:
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q="select * from adminlogin where adminid='{0}' and password='{1}'".format(adminid,password)
        cmd.execute(q)
        rec = cmd.fetchone()
        dbe.close()
        if(rec):
            request.session['ADMIN_SES']=rec
            return render(request,"Dashboard.html",{'admin':request.session['ADMIN_SES']})
        else:
            return render(request,"NewAdminLogin.html",{'msg':'InvalidAdminId/Password'})

    except Exception as e:
        return render(request, "NewAdminLogin.html", {'msg': 'Server Error'})

def ActionLogout(request):
    auth.logout(request)
    return render(request,"NewAdminLogin.html",{'msg':[]})