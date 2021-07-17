from django.shortcuts import render
import pymysql as mysql
from django.http import JsonResponse
import json
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def ActionSongsInterface(request):
    try:
     rec =request.session['ADMIN_SES']
     return render(request, 'SongsInterface.html')
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})


@xframe_options_exempt
def ActionSubmitSongs(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    scid=request.POST['scid']
    title = request.POST['title']
    ryear = request.POST['ryear']
    lyrics = request.FILES['lyrics']
    status = request.POST['status']
    type = request.POST['type']
    singers = request.POST['singers']
    director = request.POST['dir']
    mcompany = request.POST['mcompany']
    file = request.FILES['sicon']
    try:
        dbe= mysql.connect(host="localhost",port=3306,user="root",password="1234",db="songvideo")
        cmd=dbe.cursor()
        q="insert into songs(subcategoryid,title,releaseyear,lyrics,status,type,singers,director,musiccompany,poster) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')".format(scid,title,ryear,lyrics.name,status,type,singers,director,mcompany,file.name)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        #upload file
        f=open("d:/MusicMusic/asset/"+file.name,"wb")
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        # upload song
        f = open("d:/MusicMusic/asset/" + file.name, "wb")
        for chunk in lyrics.chunks():
            f.write(chunk)
        f.close()

        return render(request,"SongsInterface.html",{'msg':'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request, "SongsInterface.html", {'msg': 'Fail to submit Record'})

@xframe_options_exempt
def ActionSongsDisplayAll(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    try:
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "select *from songs"
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.close()
        return render(request,"SongsDisplayAll.html",{'rows':rows})
    except Exception as e:
        print(e)
        return render(request, "SongsDisplayAll.html", {'rows': ''})

@xframe_options_exempt
def ActionSongsDisplayById(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    try:
        sid = request.GET['sid']
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "select * from songs where songid={0}".format(sid)
        cmd.execute(q)
        row=cmd.fetchone()
        dbe.close()
        return render(request,"SongsDisplayById.html",{'row':row})
    except Exception as e:
        print(e)
        return render(request, "SongsDisplayById.html", {'row': ''})

@xframe_options_exempt
def ActionSongsEditDeleteSubmit(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    sid = request.POST['sid']

    title = request.POST['title']
    ryear = request.POST['ryear']
    lyrics = request.FILES['lyrics']
    status = request.POST['status']
    type = request.POST['type']
    singers = request.POST['singers']
    director = request.POST['dir']
    mcompany = request.POST['mcompany']
    btn=request.POST['btn']
    try:
     if(btn=='Edit'):
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "update songs set title='{0}',releaseyear='{1}',lyrics='{2}',status='{3}',type='{4}',singers='{5}',director='{6}',musiccompany='{7}' where songid={8}".format(title,ryear,lyrics.name,status,type,singers,director,mcompany,sid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f = open("d:/MusicMusic/asset/" +lyrics.name, "wb")
        for chunk in lyrics.chunks():
            f.write(chunk)
        f.close()
        return ActionSongsDisplayAll(request)

     elif(btn=='Delete'):
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "delete from songs where songid={0}".format(sid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        return ActionSongsDisplayAll(request)
    except Exception as e:
        print(e)
        return ActionSongsDisplayAll(request)

@xframe_options_exempt
def ActionSongsEditPicture(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    sid = request.POST['sid']
    file=request.FILES['sicon']
    try:
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "update songs set poster='{0}' where songid={1}".format(file.name, sid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f = open("d:/MusicMusic/asset/" + file.name, "wb")
        for chunk in file.chunks():
          f.write(chunk)
        f.close()
        return ActionSongsDisplayAll(request)
    except Exception as e:
        print(e)
        return ActionSongsDisplayAll(request)

@xframe_options_exempt
def ActionDisplaySubCategoryJSON(request):
    try:
     rec =request.session['ADMIN_SES']
    except:
     return render(request, 'NewAdminLogin.html', {'msg': ''})
    try:
        cid = request.GET['cid']
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "select * from subcategory where categoryid={0}".format(cid)
        print(q)
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([], safe=False)

