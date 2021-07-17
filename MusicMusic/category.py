from django.shortcuts import render
import pymysql as mysql
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse


@xframe_options_exempt
def ActionCategoryInterface(request):
    try:
     rec =request.session['ADMIN_SES']
     return render(request,'CategoryInterface.html')
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
@xframe_options_exempt
def ActionSubmitCategory(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    cname=request.POST['cname']
    cdesp = request.POST['cdesp']
    file = request.FILES['cicon']
    try:
        dbe= mysql.connect(host="localhost",port=3306,user="root",password="1234",db="songvideo")
        cmd=dbe.cursor()
        q="insert into category(categoryname,categorydescription,categoryicon)values('{0}','{1}','{2}')".format(cname,cdesp,file.name)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        #upload file
        f=open("d:/MusicMusic/asset/"+file.name,"wb")
        for chunk in file.chunks():
            f.write(chunk)
        f.close()

        return render(request,"CategoryInterface.html",{'msg':'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request, "CategoryInterface.html", {'msg': 'Fail to submit Record'})

@xframe_options_exempt
def ActionDisplayAll(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    try:
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "select *from category"
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.close()
        return render(request,"CategoryDisplayAll.html",{'rows':rows})
    except Exception as e:
        print(e)
        return render(request, "CategoryDisplayAll.html", {'rows': ''})
@xframe_options_exempt
def ActionDisplayById(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    try:
        cid = request.GET['cid']
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "select * from category where categoryid={0}".format(cid)
        cmd.execute(q)
        row=cmd.fetchone()
        dbe.close()
        return render(request,"CategoryDisplayById.html",{'row':row})
    except Exception as e:
        print(e)
        return render(request, "CategoryDisplayByID.html", {'row': ''})

@xframe_options_exempt
def ActionCategoryEditDeleteSubmit(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    cid=request.POST['cid']
    cname = request.POST['cname']
    cdesp = request.POST['cdesp']
    btn=request.POST['btn']
    try:
     if(btn=='Edit'):
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "update category set categoryname='{0}',categorydescription='{1}' where categoryid={2}".format(cname,cdesp,cid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        return ActionDisplayAll(request)

     elif(btn=='Delete'):
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "delete from category where categoryid={0}".format(cid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        return ActionDisplayAll(request)
    except Exception as e:
        print(e)
        return ActionDisplayAll(request)
@xframe_options_exempt
def ActionCategoryEditPicture(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    cid = request.POST['cid']
    file=request.FILES['cicon']
    try:
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "update category set categoryicon='{0}' where categoryid={1}".format(file.name, cid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f = open("d:/MusicMusic/asset/" + file.name, "wb")
        for chunk in file.chunks():
          f.write(chunk)
        f.close()
        return ActionDisplayAll(request)
    except Exception as e:
        print(e)
        return ActionDisplayAll(request)

@xframe_options_exempt
def ActionDisplayJSON(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})

    try:
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "select *from category"
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([], safe=False)
