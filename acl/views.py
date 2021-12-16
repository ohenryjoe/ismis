from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from acl.models import User
from hrms.models import Employees


@login_required()
def custom_page_not_found_view(request, exception):
    return render(request, "acl/error404.html", {})


@login_required()
def custom_error_view(request, exception=None):
    return render(request, "acl/error500.html", {})


@login_required()
def custom_permission_denied_view(request, exception=None):
    return render(request, "acl/error403.html", {})


@login_required()
def custom_bad_request_view(request, exception=None):
    return render(request, "acl/error400.html", {})


# Create your views here.
from acl.forms import LoginForm


def login_page(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(email=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/HRMIS', {'request': request, })
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    return render(request, "acl/login.html", {"form": form, "msg": msg})


def mylogin(request, *args, **kwargs):
    return redirect('/HRMIS', {'request': request})



@login_required()
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required()
def index(request):
    curruser = get_object_or_404(User, pk=request.user.pk)
    curruser = curruser.is_admin
    if curruser:
        return render(request, 'hrms/DirectorateDashboard.html', {'curruser': curruser})
    else:
        return render(request, 'hrms/EmployeeDashboard.html', {'curruser': curruser})


@login_required()
def accordion(request):
    return render(request, 'acl/accordion.html')


@login_required()
def advancedforms(request):
    return render(request, 'acl/advancedforms.html')


@login_required()
def alerts(request):
    return render(request, 'acl/alerts.html')


@login_required()
def avatars(request):
    return render(request, 'acl/avatars.html')


@login_required()
def badge(request):
    return render(request, 'acl/badge.html')


@login_required()
def blog(request):
    return render(request, 'acl/blog.html')


@login_required()
def blog2(request):
    return render(request, 'acl/blog2.html')


@login_required()
def blog3(request):
    return render(request, 'acl/blog3.html')


@login_required()
def blogstyles(request):
    return render(request, 'acl/blogstyles.html')


@login_required()
def breadcrumbs(request):
    return render(request, 'acl/breadcrumbs.html')


@login_required()
def buttons(request):
    return render(request, 'acl/buttons.html')


@login_required()
def calendar(request):
    return render(request, 'acl/calendar.html')


@login_required()
def cards(request):
    return render(request, 'acl/cards.html')


@login_required()
def cardsimage(request):
    return render(request, 'acl/cardsimage.html')


@login_required()
def carousel(request):
    return render(request, 'acl/carousel.html')


@login_required()
def cart(request):
    return render(request, 'acl/cart.html')


@login_required()
def chartapex(request):
    return render(request, 'acl/chartapex.html')


@login_required()
def chartc3(request):
    return render(request, 'acl/chartc3.html')


@login_required()
def chartchartist(request):
    return render(request, 'acl/chartchartist.html')


@login_required()
def chartechart(request):
    return render(request, 'acl/chartechart.html')


@login_required()
def chartflot(request):
    return render(request, 'acl/chartflot.html')


@login_required()
def chartmorris(request):
    return render(request, 'acl/chartmorris.html')


@login_required()
def chartpeity(request):
    return render(request, 'acl/chartpeity.html')


@login_required()
def chat(request):
    return render(request, 'acl/chat.html')


@login_required()
def chat2(request):
    return render(request, 'acl/chat2.html')


@login_required()
def chat3(request):
    return render(request, 'acl/chat3.html')


@login_required()
def coming(request):
    return render(request, 'acl/coming.html')


@login_required()
def construction(request):
    return render(request, 'acl/construction.html')


@login_required()
def contactlist(request):
    return render(request, 'acl/contactlist.html')


@login_required()
def contactlist2(request):
    return render(request, 'acl/contactlist2.html')


@login_required()
def cookies(request):
    return render(request, 'acl/cookies.html')


@login_required()
def counters(request):
    return render(request, 'acl/counters.html')


@login_required()
def datatable(request):
    return render(request, 'acl/datatable.html')


@login_required()
def dragula(request):
    return render(request, 'acl/dragula.html')


@login_required()
def dropdown(request):
    return render(request, 'acl/dropdown.html')


@login_required()
def editprofile(request):
    return render(request, 'acl/editprofile.html')


@login_required()
def elementcolors(request):
    return render(request, 'acl/elementcolors.html')


@login_required()
def elementflex(request):
    return render(request, 'acl/elementflex.html')


@login_required()
def elementheight(request):
    return render(request, 'acl/elementheight.html')


@login_required()
def elementsborder(request):
    return render(request, 'acl/elementsborder.html')


@login_required()
def elementsdisplay(request):
    return render(request, 'acl/elementsdisplay.html')


@login_required()
def elementsmargin(request):
    return render(request, 'acl/elementsmargin.html')


@login_required()
def elementspaddning(request):
    return render(request, 'acl/elementspaddning.html')


@login_required()
def elementtypography(request):
    return render(request, 'acl/elementtypography.html')


@login_required()
def elementwidth(request):
    return render(request, 'acl/elementwidth.html')


@login_required()
def emailcompose(request):
    return render(request, 'acl/emailcompose.html')


@login_required()
def emailinbox(request):
    return render(request, 'acl/emailinbox.html')


@login_required()
def emailread(request):
    return render(request, 'acl/emailread.html')


@login_required()
def empty(request):
    return render(request, 'acl/empty.html')


@login_required()
def error400(request):
    return render(request, 'acl/error400.html')


@login_required()
def error401(request):
    return render(request, 'acl/error401.html')


@login_required()
def error403(request):
    return render(request, 'acl/error403.html')


@login_required()
def error404(request):
    return render(request, 'acl/error404.html')


@login_required()
def error500(request):
    return render(request, 'acl/error500.html')


@login_required()
def error503(request):
    return render(request, 'acl/error503.html')


@login_required()
def faq(request):
    return render(request, 'acl/faq.html')


@login_required()
def filemanager(request):
    return render(request, 'acl/filemanager.html')


@login_required()
def filemanagerlist(request):
    return render(request, 'acl/filemanagerlist.html')


@login_required()
def footers(request):
    return render(request, 'acl/footers.html')


@login_required()
def forgotpassword1(request):
    return render(request, 'acl/forgotpassword1.html')


@login_required()
def forgotpassword2(request):
    return render(request, 'acl/forgotpassword2.html')


@login_required()
def forgotpassword3(request):
    return render(request, 'acl/forgotpassword3.html')


@login_required()
def formelements(request):
    return render(request, 'acl/formelements.html')


@login_required()
def formsizes(request):
    return render(request, 'acl/formsizes.html')


@login_required()
def formtreeview(request):
    return render(request, 'acl/formtreeview.html')


@login_required()
def formwizard(request):
    return render(request, 'acl/formwizard.html')


@login_required()
def gallery(request):
    return render(request, 'acl/gallery.html')


@login_required()
def headers(request):
    return render(request, 'acl/headers.html')


@login_required()
def icons(request):
    return render(request, 'acl/icons.html')


@login_required()
def icons2(request):
    return render(request, 'acl/icons2.html')


@login_required()
def icons3(request):
    return render(request, 'acl/icons3.html')


@login_required()
def icons4(request):
    return render(request, 'acl/icons4.html')


@login_required()
def icons5(request):
    return render(request, 'acl/icons5.html')


@login_required()
def icons6(request):
    return render(request, 'acl/icons6.html')


@login_required()
def icons7(request):
    return render(request, 'acl/icons7.html')


@login_required()
def icons8(request):
    return render(request, 'acl/icons8.html')


@login_required()
def icons9(request):
    return render(request, 'acl/icons9.html')


@login_required()
def icons10(request):
    return render(request, 'acl/icons10.html')


@login_required()
def icons11(request):
    return render(request, 'acl/icons11.html')


@login_required()
def icons12(request):
    return render(request, 'acl/icons12.html')


@login_required()
def imagecomparison(request):
    return render(request, 'acl/imagecomparison.html')


@login_required()
def imgcrop(request):
    return render(request, 'acl/imgcrop.html')


@login_required()
def index2(request):
    return render(request, 'acl/index2.html')


@login_required()
def index3(request):
    return render(request, 'acl/index3.html')


@login_required()
def index4(request):
    return render(request, 'acl/index4.html')


@login_required()
def index5(request):
    return render(request, 'acl/index5.html')


@login_required()
def invoice1(request):
    return render(request, 'acl/invoice1.html')


@login_required()
def invoice2(request):
    return render(request, 'acl/invoice2.html')


@login_required()
def invoice3(request):
    return render(request, 'acl/invoice3.html')


@login_required()
def invoiceadd(request):
    return render(request, 'acl/invoiceadd.html')


@login_required()
def invoiceedit(request):
    return render(request, 'acl/invoiceedit.html')


@login_required()
def invoicelist(request):
    return render(request, 'acl/invoicelist.html')


@login_required()
def list(request):
    return render(request, 'acl/list.html')


@login_required()
def loaders(request):
    return render(request, 'acl/loaders.html')


@login_required()
def lockscreen1(request):
    return render(request, 'acl/lockscreen1.html')


@login_required()
def lockscreen2(request):
    return render(request, 'acl/lockscreen2.html')


@login_required()
def lockscreen3(request):
    return render(request, 'acl/lockscreen3.html')


@login_required()
def login1(request):
    return render(request, 'acl/login1.html')


# @login_required()
# def login2(request):
#     return render(request, 'acl/login2.html')

@login_required()
def login3(request):
    return render(request, 'acl/login3.html')


@login_required()
def maps(request):
    return render(request, 'acl/maps.html')


@login_required()
def maps2(request):
    return render(request, 'acl/maps2.html')


@login_required()
def maps3(request):
    return render(request, 'acl/maps3.html')


@login_required()
def mediaobject(request):
    return render(request, 'acl/mediaobject.html')


@login_required()
def modal(request):
    return render(request, 'acl/modal.html')


@login_required()
def navigation(request):
    return render(request, 'acl/navigation.html')


@login_required()
def notify(request):
    return render(request, 'acl/notify.html')


@login_required()
def pagesessiontimeout(request):
    return render(request, 'acl/pagesessiontimeout.html')


@login_required()
def pagination(request):
    return render(request, 'acl/pagination.html')


@login_required()
def panels(request):
    return render(request, 'acl/panels.html')


@login_required()
def popover(request):
    return render(request, 'acl/popover.html')


@login_required()
def pricing(request):
    return render(request, 'acl/pricing.html')


@login_required()
def pricing2(request):
    return render(request, 'acl/pricing2.html')


@login_required()
def pricing3(request):
    return render(request, 'acl/pricing3.html')


@login_required()
def profile1(request):
    return render(request, 'acl/profile1.html')


@login_required()
def profile2(request):
    return render(request, 'acl/profile2.html')


@login_required()
def profile3(request):
    return render(request, 'acl/profile3.html')


@login_required()
def progress(request):
    return render(request, 'acl/progress.html')


@login_required()
def rangeslider(request):
    return render(request, 'acl/rangeslider.html')


@login_required()
def rating(request):
    return render(request, 'acl/rating.html')


@login_required()
def register1(request):
    return render(request, 'acl/register1.html')


def register2(request):
    return render(request, 'acl/register2.html')


@login_required()
def register3(request):
    return render(request, 'acl/register3.html')


@login_required()
def resetpassword1(request):
    return render(request, 'acl/resetpassword1.html')


@login_required()
def resetpassword2(request):
    return render(request, 'acl/resetpassword2.html')


@login_required()
def resetpassword3(request):
    return render(request, 'acl/resetpassword3.html')


@login_required()
def search(request):
    return render(request, 'acl/search.html')


@login_required()
def shop(request):
    return render(request, 'acl/shop.html')


@login_required()
def shopdes(request):
    return render(request, 'acl/shopdes.html')


@login_required()
def sweetalert(request):
    return render(request, 'acl/sweetalert.html')


@login_required()
def tables(request):
    return render(request, 'acl/tables.html')


@login_required()
def tabs(request):
    return render(request, 'acl/tabs.html')


@login_required()
def tags(request):
    return render(request, 'acl/tags.html')


@login_required()
def terms(request):
    return render(request, 'acl/terms.html')


@login_required()
def timeline(request):
    return render(request, 'acl/timeline.html')


@login_required()
def todolist(request):
    return render(request, 'acl/todolist.html')


@login_required()
def todolist2(request):
    return render(request, 'acl/todolist2.html')


@login_required()
def todolist3(request):
    return render(request, 'acl/todolist3.html')


@login_required()
def tooltip(request):
    return render(request, 'acl/tooltip.html')


@login_required()
def userslist1(request):
    return render(request, 'acl/userslist1.html')


@login_required()
def userslist2(request):
    return render(request, 'acl/userslist2.html')


@login_required()
def userslist3(request):
    return render(request, 'acl/userslist3.html')


@login_required()
def userslist4(request):
    return render(request, 'acl/userslist4.html')


@login_required()
def widgets1(request):
    return render(request, 'acl/widgets1.html')


@login_required()
def widgets2(request):
    return render(request, 'acl/widgets2.html')


@login_required()
def wysiwyag(request):
    return render(request, 'acl/wysiwyag.html')
