"""MusicMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import category
from . import subcategory
from . import songs
from . import Admin
from . import user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('categoryinterface/',category.ActionCategoryInterface),
    path('categorysubmit',category.ActionSubmitCategory),
    path('categorydisplayall/',category.ActionDisplayAll),
    path('categorydisplaybyid/',category.ActionDisplayById),
    path('categoryeditdeletesubmit',category.ActionCategoryEditDeleteSubmit),
    path('categoryeditpicture',category.ActionCategoryEditPicture),
    path('subcategoryinterface/',subcategory.ActionSubCategoryInterface),
    path('subcategorysubmit',subcategory.ActionSubmitSubCategory),
    path('subcategorydisplayall/',subcategory.ActionSubCategoryDisplayAll),
    path('subcategorydisplaybyid/',subcategory.ActionSubCategoryDisplayById),
    path('subcategoryeditdeletesubmit',subcategory.ActionSubCategoryEditDeleteSubmit),
    path('subcategoryeditpicture',subcategory.ActionSubCategoryEditPicture),
    path('songsinterface/',songs.ActionSongsInterface),
    path('songssubmit',songs.ActionSubmitSongs),
    path('songsdisplayall/',songs.ActionSongsDisplayAll),
    path('songsdisplaybyid/',songs.ActionSongsDisplayById),
    path('songseditdeletesubmit',songs.ActionSongsEditDeleteSubmit),
    path('songseditpicture',songs.ActionSongsEditPicture),
    path('adminlogin/',Admin.ActionAdminLogin),
    path('checkadminlogin',Admin.ActionCheckLogin),
    path('categorydisplayalljson/',category.ActionDisplayJSON),
    path('displaysubcategoryjson/',songs.ActionDisplaySubCategoryJSON),
    path('mainpage/',user.ActionMainInterface),
    path('categorypage/',user.ActionCategoryPage),
    path('playlistpage/',user.ActionPlaylistPage),
    path('artistpage/',user.ActionArtistPage),
    path('subcategorypage/',user.ActionSubCategoryPage),
    path('searchpage/',user.ActionSearchSongPage),
    path('searchpagejson/',user.ActionSearchSongJson),
    path('playsong/',user.ActionPlaySong),
    path('logout/',Admin.ActionLogout),
]
urlpatterns+=staticfiles_urlpatterns()
