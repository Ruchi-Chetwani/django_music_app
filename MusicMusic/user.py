from django.shortcuts import render
import pymysql as mysql
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse
import ast


@xframe_options_exempt
def ActionMainInterface(request):
    try:
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        q = "select *from category"
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return render(request, 'solmusic/index.html', {'rows':rows})
    except Exception as e:
        print(e)
        return render(request, 'solmusic/index.html', {'rows':[]})

def FetchAllRecords(q):
    try:
        dbe = mysql.connect(host="localhost", port=3306, user="root", password="1234", db="songvideo")
        cmd = dbe.cursor()
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return rows
    except Exception as e:
        print(e)
        return []

@xframe_options_exempt
def ActionCategoryPage(request):
    try:
        q = "select * from category"
        rows = FetchAllRecords(q)
        q="select * from songs"
        srows=FetchAllRecords(q)
        return render(request, 'solmusic/category.html',{'rows':rows,'srows':srows})
    except Exception as e:
        print(e)
        return render(request, 'solmusic/category.html', {'rows':[],'srows':[]})

@xframe_options_exempt
def ActionPlaylistPage(request):
    try:
        q = "select * from category"
        rows = FetchAllRecords(q)
        q = "select * from subcategory"
        srows = FetchAllRecords(q)
        return render(request, 'solmusic/playlist.html',{'rows':rows,'srows':srows})
    except Exception as e:
        print(e)
        return render(request, 'solmusic/playlist.html', {'rows':[],'srows':[]})

@xframe_options_exempt
def ActionArtistPage(request):
    try:
        sc = request.GET['scid']
        sc=ast.literal_eval(sc)
        q = "select * from songs where subcategoryid={0} ".format(sc[0])
        rows = FetchAllRecords(q)

        return render(request, 'solmusic/artist.html',{'rows':rows,'sc':sc})
    except Exception as e:
        print(e)
        return render(request, 'solmusic/artist.html',{'rows':[],'sc':[]})

@xframe_options_exempt
def ActionSubCategoryPage(request):
    try:
        cid=request.GET['cid']
        q = "select * from subcategory where categoryid={0} ".format(cid)
        rows = FetchAllRecords(q)
        return render(request, 'solmusic/subcategory.html',{'rows':rows})
    except Exception as e:
        print(e)
        return render(request, 'solmusic/subcategory.html', {'rows':[]})


@xframe_options_exempt
def ActionSearchSongPage(request):
    try:
        q = "select * from songs"
        rows = FetchAllRecords(q)
        return render(request, 'solmusic/searchsong.html',{'rows':rows})
    except Exception as e:
        print(e)
        return render(request, 'solmusic/searchsong.html',{'rows':[]})

@xframe_options_exempt
def ActionSearchSongJson(request):
    try:
        pat=request.GET['pat']
        q = "select * from songs where title like '%{0}%'".format(pat)
        print(q)
        rows = FetchAllRecords(q)
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print(e)
        return JsonResponse(rows,safe=False)

@xframe_options_exempt
def ActionPlaySong(request):
    try:
        sg=request.GET['sg']
        print('xxxxxx',sg)
        sg=sg.split(",")
        print(sg)
        q = "select * from songs where songid={0}".format(sg[0])
        print(q)
        rows = FetchAllRecords(q)
        print(rows)
        return render(request, 'solmusic/playsong.html',{'row':rows[0]})
    except Exception as e:
        print(e)
        return render(request, 'solmusic/playsong.html', {'row': []})
