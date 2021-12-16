"""zanex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import hrms.views
from hrms import views as hrmsviews
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_page, name='loginpage'),
    path('', views.mylogin, name='login'),
    path('logout', views.logout_user, name='logout'),

    path('HRMS/', hrms.views.EmployeesListView, name='hrmshome'),

    path("index", views.index, name='index'),
    
    path("accordion", views.accordion, name='accordion'),
    
    path("advancedforms", views.advancedforms, name='advancedforms'),

    path("alerts", views.alerts, name='alerts'),
    
    path("avatars", views.avatars, name='avatars'),
    
    path("badge", views.badge, name='badge'),
    
    path("blog", views.blog, name='blog'),
    
    path("blog2", views.blog2, name='blog2'),
    
    path("blog3", views.blog3, name='blog3'),
    
    path("blogstyles", views.blogstyles, name='blogstyles'),
    
    path("breadcrumbs", views.breadcrumbs, name='breadcrumbs'),
    
    path("buttons", views.buttons, name='buttons'),
    
    path("calendar", views.calendar, name='calendar'),
    
    path("cards", views.cards, name='cards'),
    
    path("cardsimage", views.cardsimage, name='cardsimage'),
    
    path("carousel", views.carousel, name='carousel'),
    
    path("cart", views.cart, name='cart'),
    
    path("chartapex", views.chartapex, name='chartapex'),
    
    path("chartc3", views.chartc3, name='chartc3'),
    
    path("chartchartist", views.chartchartist, name='chartchartist'),
    
    path("chartechart", views.chartechart, name='chartechart'),
    
    path("chartflot", views.chartflot, name='chartflot'),
    
    path("chartmorris", views.chartmorris, name='chartmorris'),
    
    path("chartpeity", views.chartpeity, name='chartpeity'),
    
    path("chat", views.chat, name='chat'),
    
    path("chat2", views.chat2, name='chat2'),
    
    path("chat3", views.chat3, name='chat3'),
    
    path("coming", views.coming, name='coming'),
    
    path("construction", views.construction, name='construction'),
    
    path("contactlist", views.contactlist, name='contactlist'),
    
    path("contactlist2", views.contactlist2, name='contactlist2'),
    
    path("cookies", views.cookies, name='cookies'),
    
    path("counters", views.counters, name='counters'),
    
    path("datatable", views.datatable, name='datatable'),
    
    path("dragula", views.dragula, name='dragula'),
    
    path("dropdown", views.dropdown, name='dropdown'),
    
    path("editprofile", views.editprofile, name='editprofile'),
    
    path("elementcolors", views.elementcolors, name='elementcolors'),
    
    path("elementflex", views.elementflex, name='elementflex'),
    
    path("elementheight", views.elementheight, name='elementheight'),
    
    path("elementsborder", views.elementsborder, name='elementsborder'),
    
    path("elementsdisplay", views.elementsdisplay, name='elementsdisplay'),
    
    path("elementsmargin", views.elementsmargin, name='elementsmargin'),
    
    path("elementspaddning", views.elementspaddning, name='elementspaddning'),
    
    path("elementtypography", views.elementtypography, name='elementtypography'),
    
    path("elementwidth", views.elementwidth, name='elementwidth'),
    
    path("emailcompose", views.emailcompose, name='emailcompose'),
    
    path("emailinbox", views.emailinbox, name='emailinbox'),
    
    path("emailread", views.emailread, name='emailread'),
    
    path("empty", views.empty, name='empty'),
    
    path("error400", views.error400, name='error400'),
    
    path("error401", views.error401, name='error401'),
    
    path("error403", views.error403, name='error403'),
    
    path("error404", views.error404, name='error404'),
    
    path("error500", views.error500, name='error500'),
    
    path("error503", views.error503, name='error503'),
    
    path("faq", views.faq, name='faq'),
    
    path("filemanager", views.filemanager, name='filemanager'),
    
    path("filemanagerlist", views.filemanagerlist, name='filemanagerlist'),
    
    path("footers", views.footers, name='footers'),
    
    path("forgotpassword1", views.forgotpassword1, name='forgotpassword1'),
    
    path("forgotpassword2", views.forgotpassword2, name='forgotpassword2'),
    
    path("forgotpassword3", views.forgotpassword3, name='forgotpassword3'),
    
    path("formelements", views.formelements, name='formelements'),
    
    path("formsizes", views.formsizes, name='formsizes'),
    
    path("formtreeview", views.formtreeview, name='formtreeview'),
    
    path("formwizard", views.formwizard, name='formwizard'),
    
    path("gallery", views.gallery, name='gallery'),
    
    path("headers", views.headers, name='headers'),
    
    path("icons", views.icons, name='icons'),
    
    path("icons2", views.icons2, name='icons2'),
    
    path("icons3", views.icons3, name='icons3'),
    
    path("icons4", views.icons4, name='icons4'),
    
    path("icons5", views.icons5, name='icons5'),
    
    path("icons6", views.icons6, name='icons6'),
    
    path("icons7", views.icons7, name='icons7'),
    
    path("icons8", views.icons8, name='icons8'),
    
    path("icons9", views.icons9, name='icons9'),
    
    path("icons10", views.icons10, name='icons10'),
    
    path("icons11", views.icons11, name='icons11'),
    
    path("icons12", views.icons12, name='icons12'),
    
    path("imagecomparison", views.imagecomparison, name='imagecomparison'),
    
    path("imgcrop", views.imgcrop, name='imgcrop'),
    
    path("index", views.index, name='index'),

    path("index2", views.index2, name='index2'),
    
    path("index3", views.index3, name='index3'),
    
    path("index4", views.index4, name='index4'),
    
    path("index5", views.index5, name='index5'),
    
    path("invoice1", views.invoice1, name='invoice1'),
    
    path("invoice2", views.invoice2, name='invoice2'),
    
    path("invoice3", views.invoice3, name='invoice3'),
    
    path("invoiceadd", views.invoiceadd, name='invoiceadd'),
    
    path("invoiceedit", views.invoiceedit, name='invoiceedit'),
    
    path("invoicelist", views.invoicelist, name='invoicelist'),
    
    path("list", views.list, name='list'),
    
    path("loaders", views.loaders, name='loaders'),
    
    path("lockscreen1", views.lockscreen1, name='lockscreen1'),
    
    path("lockscreen2", views.lockscreen2, name='lockscreen2'),
    
    path("lockscreen3", views.lockscreen3, name='lockscreen3'),
    
    path("login1", views.login1, name='login1'),

    
    path("login3", views.login3, name='login3'),
    
    path("maps", views.maps, name='maps'),
    
    path("maps2", views.maps2, name='maps2'),
    
    path("maps3", views.maps3, name='maps3'),
    
    path("mediaobject", views.mediaobject, name='mediaobject'),
    
    path("modal", views.modal, name='modal'),
    
    path("navigation", views.navigation, name='navigation'),
    
    path("notify", views.notify, name='notify'),
    
    path("pagesessiontimeout", views.pagesessiontimeout, name='pagesessiontimeout'),
    
    path("pagination", views.pagination, name='pagination'),
    
    path("panels", views.panels, name='panels'),
    
    path("popover", views.popover, name='popover'),
    
    path("pricing", views.pricing, name='pricing'),
    
    path("pricing2", views.pricing2, name='pricing2'),
    
    path("pricing3", views.pricing3, name='pricing3'),
    
    path("profile1", views.profile1, name='profile1'),
    
    path("profile2", views.profile2, name='profile2'),
    
    path("profile3", views.profile3, name='profile3'),
    
    path("progress", views.progress, name='progress'),
    
    path("rangeslider", views.rangeslider, name='rangeslider'),
    
    path("rating", views.rating, name='rating'),

    path("register1", views.register1, name='register1'),
    
    path("register2", views.register2, name='register2'),
    
    path("register3", views.register3, name='register3'),
    
    path("resetpassword1", views.resetpassword1, name='resetpassword1'),
    
    path("resetpassword2", views.resetpassword2, name='resetpassword2'),
    
    path("resetpassword3", views.resetpassword3, name='resetpassword3'),
    
    path("search", views.search, name='search'),
    
    path("shop", views.shop, name='shop'),
    
    path("shopdes", views.shopdes, name='shopdes'),
    
    path("sweetalert", views.sweetalert, name='sweetalert'),
    
    path("tables", views.tables, name='tables'),
    
    path("tabs", views.tabs, name='tabs'),
    
    path("tags", views.tags, name='tags'),
    
    path("terms", views.terms, name='terms'),
    
    path("timeline", views.timeline, name='timeline'),
    
    path("todolist", views.todolist, name='todolist'),
    
    path("todolist2", views.todolist2, name='todolist2'),
    
    path("todolist3", views.todolist3, name='todolist3'),
    
    path("tooltip", views.tooltip, name='tooltip'),
    
    path("userslist1", views.userslist1, name='userslist1'),
    
    path("userslist2", views.userslist2, name='userslist2'),
    
    path("userslist3", views.userslist3, name='userslist3'),
    
    path("userslist4", views.userslist4, name='userslist4'),
    
    path("widgets1", views.widgets1, name='widgets1'),
    
    path("widgets2", views.widgets2, name='widgets2'),
    
    path("wysiwyag", views.wysiwyag, name='wysiwyag'),
]