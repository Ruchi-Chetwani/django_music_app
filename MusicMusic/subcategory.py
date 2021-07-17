from django.shortcuts import render
import pymysql as mysql
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def ActionSubCategoryInterface(request):
    try:
     rec =request.session['ADMIN_SES']
     return render(request, 'SubCategoryInterface.html')
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})


@xframe_options_exempt
def ActionSubmitSubCategory(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})

    cid = request.POST['cid']
    scname=request.POST['scname']
    scdesp = request.POST['scdesp']
    file = request.FILES['scicon']
    try:
        dbe= mysql.connect(host="localhost",port=3306,user="root",password="1234",db="songvideo")
        cmd=dbe.cursor()
        q="insert into subcategory(categoryid,subcategoryname,subcategorydescription,subcategoryicon)values('{0}','{1}','{2}','{3}')".format(cid,scname,scdesp,file.name)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        #upload file
        f=open("d:/MusicMusic/asset/"+file.name,"wb")
        for chunk in file.chunks():
            f.write(chunk)
        f.close()

        return render(request,"SubCategoryInterface.html",{'msg':'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request, "SubCategoryInterface.html", {'msg': 'Fail to submit Record'})

@xframe_options_exempt
def ActionSubCategoryDisplayAll(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})

    try:
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid) as categoryname from subcategory S"
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.close()
        return render(request,"SubCategoryDisplayAll.html",{'rows':rows})
    except Exception as e:
        print(e)
        return render(request, "SubCategoryDisplayAll.html", {'rows': ''})

@xframe_options_exempt
def ActionSubCategoryDisplayById(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})


    try:
        scid = request.GET['scid']
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid) as categoryname from subcategory S where S.subcategoryid={0}".format(scid)
        cmd.execute(q)
        row=cmd.fetchone()
        dbe.close()
        return render(request,"SubCategoryDisplayById.html",{'row':row})
    except Exception as e:
        print(e)
        return render(request, "SubCategoryDisplayByID.html", {'row': ''})

@xframe_options_exempt
def ActionSubCategoryEditDeleteSubmit(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    cid=request.POST['cid']
    scid=request.POST['scid']
    scname = request.POST['scname']
    scdesp = request.POST['scdesp']
    btn=request.POST['btn']
    try:
     if(btn=='Edit'):
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "update subcategory set subcategoryname='{0}', subcategorydescription='{1}', categoryid={2} where subcategoryid={3}".format(scname,scdesp,cid,scid)
        print(q)
        cmd.execute(q)

        dbe.commit()
        dbe.close()
        return ActionSubCategoryDisplayAll(request)

     elif(btn=='Delete'):
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "delete from subcategory where subcategoryid={0}".format(scid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        return ActionSubCategoryDisplayAll(request)
    except Exception as e:
        print(e)
        return ActionSubCategoryDisplayAll(request)

@xframe_options_exempt
def ActionSubCategoryEditPicture(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    scid = request.POST['scid']
    file=request.FILES['scicon']
    try:
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "update subcategory set subcategoryicon='{0}' where subcategoryid={1}".format(file.name, scid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f = open("d:/MusicMusic/asset/" + file.name, "wb")
        for chunk in file.chunks():
          f.write(chunk)
        f.close()
        return ActionSubCategoryDisplayAll(request)
    except Exception as e:
        print(e)
        return ActionSubCategoryDisplayAll(request)





