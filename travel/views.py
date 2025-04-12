from django.shortcuts import render, redirect
from .models import login_table
from .models import country
from .models import state_table
from .models import city_table
from .models import detail_table
from .models import package_type_table
from .models import package_details
from .models import booking_details
from .models import feedback
from .models import contactform
from .models import package_details
from .models import card_detail
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

    
# Create your views here.

def index(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        packagedata = package_details.objects.all()

        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None


        fetchdid = login_table.objects.filter(role="agent").values('id')
        print(fetchdid)

        agentsdata = detail_table.objects.filter(login_id__in=fetchdid)
        print(agentsdata)

        context = {
            'userdata': userdata,
            'Agent': Agent,
            'packagedata': packagedata,
            'profiledata': profiledata,
            'agentsdata': agentsdata,
        }

        return render(request, 'index.html', context)

    except:
        packagedata = package_details.objects.all()

        fetchdid = login_table.objects.filter(role="agent").values('id')
        print(fetchdid)

        agentsdata = detail_table.objects.filter(login_id__in=fetchdid)

        context = {
            'packagedata': packagedata,
            'agentsdata': agentsdata,
        }
        return render(request,'index.html', context)

def basic(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        context = {
            'userdata': userdata,
            'Agent': Agent,
        }

        return render(request, 'basic.html', context)

    except:
        pass
    return render(request,'basic.html')

def agents(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)


        fetchdid = login_table.objects.filter(role="agent").values('id')
        print(fetchdid)

        agentsdata = detail_table.objects.filter(login_id__in=fetchdid)
        print(agentsdata)

        context = {
            'userdata': userdata,
            'Agent': Agent,
            'agentsdata': agentsdata,
        }

        return render(request, 'agents.html', context)

    except:
        fetchdid = login_table.objects.filter(role="agent").values('id')
        print(fetchdid)

        agentsdata = detail_table.objects.filter(login_id__in=fetchdid)

        context = {
            'agentsdata': agentsdata,
        }
    return render(request,'agents.html', context)


def about(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        context = {
            'userdata': userdata,
            'Agent': Agent,
            'profiledata': profiledata,
        }
        return render(request, 'about.html',context)
    except:
        pass

    return render(request,'about.html')

def contact(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        context = {
            'userdata': userdata,
            'Agent': Agent,
            'profiledata': profiledata,
        }
        return render(request, 'contact.html',context)
    except:
        pass
    return render(request,'contact.html')

def register(request):
    return render(request,'register.html')

def bookingconfirmed(request):
    return render(request,'bookingconfirmed.html')

def packages(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        packagedata = package_details.objects.all()

        default_page = 1
        page = request.GET.get('page', default_page)

        # Get queryset of items to paginate
        items = package_details.objects.all()

        # Paginate items
        items_per_page = 3
        paginator = Paginator(items, items_per_page)

        try:
            items_page = paginator.page(page)
        except PageNotAnInteger:
            items_page = paginator.page(default_page)
        except EmptyPage:
            items_page = paginator.page(paginator.num_pages)

        context = {
            'userdata': userdata,
            'Agent': Agent,
            'packagedata': packagedata,
            'items_page': items_page,
            'profiledata': profiledata,
        }

        return render(request, 'destination-list.html', context)

    except:
        packagedata = package_details.objects.all()

        default_page = 1
        page = request.GET.get('page', default_page)

        # Get queryset of items to paginate
        items = package_details.objects.all()

        # Paginate items
        items_per_page = 3
        paginator = Paginator(items, items_per_page)

        try:
            items_page = paginator.page(page)
        except PageNotAnInteger:
            items_page = paginator.page(default_page)
        except EmptyPage:
            items_page = paginator.page(paginator.num_pages)

        context = {
            'packagedata': packagedata,
            'items_page': items_page,
        }
        return render(request, 'destination-list.html', context)

def agentpackages(request, apkid):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        packagedata = package_details.objects.filter(login_id=apkid)

        default_page = 1
        page = request.GET.get('page', default_page)

        # Get queryset of items to paginate
        items = package_details.objects.filter(login_id=apkid)

        # Paginate items
        items_per_page = 3
        paginator = Paginator(items, items_per_page)

        try:
            items_page = paginator.page(page)
        except PageNotAnInteger:
            items_page = paginator.page(default_page)
        except EmptyPage:
            items_page = paginator.page(paginator.num_pages)

        context = {
            'userdata': userdata,
            'Agent': Agent,
            'packagedata': packagedata,
            'items_page': items_page,
            'profiledata': profiledata,
        }

        return render(request, 'destination-list.html', context)

    except:
        packagedata = package_details.objects.all()

        default_page = 1
        page = request.GET.get('page', default_page)

        # Get queryset of items to paginate
        items = package_details.objects.filter(login_id=apkid)

        # Paginate items
        items_per_page = 3
        paginator = Paginator(items, items_per_page)

        try:
            items_page = paginator.page(page)
        except PageNotAnInteger:
            items_page = paginator.page(default_page)
        except EmptyPage:
            items_page = paginator.page(paginator.num_pages)

        context = {
            'packagedata': packagedata,
            'items_page': items_page,
        }
        return render(request, 'destination-list.html', context)

def viewpackages(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        packagedata = package_details.objects.filter(login_id=uid)


        default_page = 1
        page = request.GET.get('page', default_page)

        # Get queryset of items to paginate
        items = package_details.objects.filter(login_id=uid)

        # Paginate items
        items_per_page = 3
        paginator = Paginator(items, items_per_page)

        try:
            items_page = paginator.page(page)
        except PageNotAnInteger:
            items_page = paginator.page(default_page)
        except EmptyPage:
            items_page = paginator.page(paginator.num_pages)

        context = {
            'userdata': userdata,
            'Agent': Agent,
            'packagedata': packagedata,
            'items_page': items_page,
            'profiledata': profiledata,
        }

        return render(request, 'viewpackages.html', context)

    except:
        return redirect(packages)


def destinationdetailes(request, ddid):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        packagedata = package_details.objects.get(id=ddid)
        print(packagedata)
        context = {
            'userdata': userdata,
            'Agent': Agent,
            'packagedata': packagedata,
        }

        return render(request, 'destination-detail.html', context)

    except:
        packagedata = package_details.objects.get(id=ddid)
        context = {
            'packagedata': packagedata,
        }

    return render(request,'destination-detail.html', context)

def viewdata(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password_name")
        role = request.POST.get("usertype")

        logindata = login_table(email=email, phone_no=phone, password=password,
                                role=role, status="1")
        logindata.save()
        messages.success(request, 'Data Inserted Successfully. you can login now')
        return redirect(index)
    else:
        messages.error(request, 'error occured')

    return redirect(index)

def checklogin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            user = login_table.objects.get(email=username, password=password)
            request.session['log_user'] = user.email
            request.session['log_id'] = user.id
            request.session.save()

        except login_table.DoesNotExist:
            user = None

        if user is not None:
            print("successfully logged in")
            messages.success(request, 'Successfully Logged In')
            redirect(index)

        else:
            print("not logged in")
            messages.error(request, 'Invalid USER ID')
    return redirect(index)

def logout(request):
    try:
        del request.session['log_user']
        del request.session['log_id']
    except:
        pass
    return redirect(index)

def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST['email']
        try:
            user = login_table.objects.get(email=username)

        except login_table.DoesNotExist:
            user = None
        #if user exist then only below condition will run otherwise it will give error as described in else condition.
        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'krushanuinfolabz@gmail.com',
                [username],
                fail_silently=False,
            )
            # NOTE: must include below details in settings.py
            # detail tutorial - https://www.geeksforgeeks.org/setup-sending-email-in-django-project/
            # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            # EMAIL_HOST = 'smtp.gmail.com'
            # EMAIL_USE_TLS = True
            # EMAIL_PORT = 587
            # EMAIL_HOST_USER = 'mail from which email will be sent'
            # EMAIL_HOST_PASSWORD = 'pjobvjckluqrtpkl'   #turn on 2 step verification and then generate app password which will be 16 digit code and past it here

            #############################################

            #now update the password in model
            cuser = login_table.objects.get(email=username)
            cuser.password = password
            cuser.save(update_fields=['password'])

            print('Mail sent')
            messages.info(request, 'mail is sent')
            return redirect(index)

        else:
            messages.info(request, 'This account does not exist')
    return redirect(index)



def addpackage(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)
        package_type = package_type_table.objects.all()
        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        if profiledata is None:
            messages.error(request, 'Please complete your profile to add package.')
        else:
            context = {
                'userdata': userdata,
                'Agent': Agent,
                'profiledata': profiledata,
                'package_type': package_type,
            }

            return render(request, 'addpackage.html', context)
    except:
        pass
    return render(request, 'addpackage.html')

def completeprofile(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        statedetail = state_table.objects.all()
        citydetail = city_table.objects.all()
        countrydetail = country.objects.all()

        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        context = {
            'userdata': userdata,
            'Agent': Agent,
            'profiledata': profiledata,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'countrydetail': countrydetail,
        }

        return render(request, 'completeprofile.html', context)

    except:
        pass
    return render(request,'completeprofile.html')

def completeprofilesubmit(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        uname = request.POST.get("name")
        uaddress = request.POST.get("address")
        udob = request.POST.get("date")
        file = request.FILES['dp']
        ucountry = request.POST.get("countryname")
        ucity = request.POST.get("cityname")
        ustate = request.POST.get("statename")

        userdata = detail_table(login_id=login_table(id=uid), name=uname, dob=udob, address=uaddress,display_pic=file, country_id=country(id=ucountry), city_id=city_table(id=ucity), state_id=state_table(id=ustate))
        userdata.save()
        messages.success(request, 'Data Inserted Successfully.')
        return redirect(index)
    else:
        messages.error(request, 'error occured')

def yourprofile(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            uid = request.session['log_id']
            statedetail = state_table.objects.all()
            citydetail = city_table.objects.all()
            countrydetail = country.objects.all()

            try:
                profiledata = detail_table.objects.get(login_id=uid)
            except detail_table.DoesNotExist:
                profiledata = None

            details = {
                'statedetail': statedetail,
                'citydetail': citydetail,
                'countrydetail': countrydetail,
                'profiledata': profiledata,
                'Agent': Agent,

            }
            return render(request, 'yourprofile.html', details)
        except:
            pass
    except:
        pass
    return render(request, 'yourprofile.html')

def agentprofile(request, apid):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            uid = request.session['log_id']
            statedetail = state_table.objects.all()
            citydetail = city_table.objects.all()
            countrydetail = country.objects.all()

            try:
                profiledata = detail_table.objects.get(id=apid)
            except detail_table.DoesNotExist:
                profiledata = None

            details = {
                'statedetail': statedetail,
                'citydetail': citydetail,
                'countrydetail': countrydetail,
                'profiledata': profiledata,
                'Agent': Agent,

            }
            return render(request, 'agentprofile.html', details)
        except:
            pass
    except:
        pass
    return render(request, 'agentprofile.html')

def addpackagesubmit(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        pname = request.POST.get("name")
        ptype = request.POST.get("type")
        pstatus = request.POST.get("status")
        pdesc = request.POST.get("description")
        pdays = request.POST.get("days")
        file = request.FILES['dp']
        pprice = request.POST.get("price")
        statbtn = False
        if pstatus == "open":
            statbtn = True

        packdata = package_details(login_id=login_table(id=uid), package_name=pname, type_id=package_type_table(id=ptype),package_status=pstatus,status_button=statbtn, package_image=file, no_of_day=pdays, package_description=pdesc, package_price=pprice)
        packdata.save()
        messages.success(request, 'Data Inserted Successfully.')
        return redirect(addpackage)
    else:
        messages.error(request, 'error occured')

def deletepackage(request, dpid):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            checkbooking = booking_details.objects.get(package_data=package_details(id=dpid))
        except booking_details.DoesNotExist:
            checkbooking = None

        if checkbooking is None:
            package_details.objects.get(id=dpid).delete()
            context = {
                'userdata': userdata,
                'Agent': Agent,
            }

            return redirect(viewpackages)

        else:
            messages.error(request, 'User booking is there for this package.')


    except:
        pass
    messages.error(request, 'Error deleting package.')
    return redirect(viewpackages)


def closepackage(request, cpid):
    cp = package_details.objects.get(id=cpid)
    cp.package_status = "closed"
    cp.status_button = False
    cp.save(update_fields=['package_status','status_button'])
    return redirect(viewpackages)

def reopenpackage(request, ropid):
    rop = package_details.objects.get(id=ropid)
    rop.package_status = "open"
    rop.status_button = True
    rop.save(update_fields=['package_status','status_button'])
    return redirect(viewpackages)

#def bookpackage(request, bpkid):
 #   uid = request.session['log_id']

  #  userdata = login_table.objects.get(id=uid)
   # Agent = False
    #if userdata.role == "agent":
     #   Agent = True
      #  print(userdata.role)
#    stat = "confirmed"
#    pstat = "pending"
#
#    try:
#        profiledata = detail_table.objects.get(login_id=uid)
#    except detail_table.DoesNotExist:
#        profiledata = None
#
#    packagedetails = package_details.objects.get(id=bpkid)
#    if packagedetails.package_status == "open":
#        bookingdata = booking_details(login_id=login_table(id=uid), booking_status=stat, package_data=package_details(id=bpkid), payment_status=pstat)
#        print("check")
#        bookingdata.save()
#    else:
#        messages.error(request, 'Package is full.')

#    context = {
#        'userdata': userdata,
#        'Agent': Agent,
#        'profiledata': profiledata,
#    }

#    return render(request, 'bookingconfirmed.html', context)

def bookpackage(request):
    uid = request.session['log_id']
    userdata = login_table.objects.get(id=uid)
    Agent = False
    if userdata.role == "agent":
        Agent = True
        print(userdata.role)
    stat = "confirmed"
    pstat = "pending"

    try:
        profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
        profiledata = None

    if request.method == 'POST':
        bname = request.POST.get("name")
        nooa = request.POST.get("noofadults")
        nooc = request.POST.get("noofchild")
        bpkid = request.POST.get("packid")
        card_number = request.POST.get("number")
        card_cvv = request.POST.get("security-code")
        exp_date = request.POST.get("expiration-month-and-year")

        carddetail = card_detail.objects.get()

        ocn = carddetail.card_number
        ocvv = carddetail.card_cvv
        oexpd = carddetail.exp_date
        cb = carddetail.card_balance

        packagedetails = package_details.objects.get(id=bpkid)
        pamount = packagedetails.package_price

        if ocn == card_number and ocvv == card_cvv and oexpd == exp_date:
            print("payment expected")
            cb = cb - pamount
            carddetail.card_balance = cb
            carddetail.save(update_fields=['card_balance'])



            if packagedetails.package_status == "open":
                bookingdata = booking_details(login_id=login_table(id=uid), booking_status=stat,booking_name=bname,no_of_adults=nooa,no_of_child=nooc, package_data=package_details(id=bpkid), payment_status=stat)
                print("check")
                bookingdata.save()
            else:
                messages.error(request, 'Package is full.')
        else:
            messages.error(request, 'Payment Failed')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'userdata': userdata,
        'Agent': Agent,
        'profiledata': profiledata,
    }

    return render(request, 'bookingconfirmed.html', context)



def submitreview(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        ratings = request.POST.get("input-1")
        feedbackdetails = request.POST.get("feedback")
        subreview = feedback(login_id=login_table(id=uid), ratings=ratings, comment=feedbackdetails)
        subreview.save()
        messages.success(request, 'Review is submitted successfully.')
    else:
        pass
    return redirect(index)

def bookedpackages(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        bookedpackagedata = booking_details.objects.filter(login_id=uid)


        context = {
            'userdata': userdata,
            'Agent': Agent,
            'bookedpackagedata': bookedpackagedata,
            'profiledata': profiledata,
        }

        return render(request, 'bookedpackages.html', context)

    except:
        pass
    return render(request, 'bookedpackages.html', context)

def viewmybookings(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        fetchproid = package_details.objects.filter(login_id=uid).values('id')
        print(fetchproid)
        mybookings = booking_details.objects.filter(package_data__in=fetchproid)
        print(mybookings)

        context = {
            'userdata': userdata,
            'Agent': Agent,
            'mybookings': mybookings,
            'profiledata': profiledata,
        }

        return render(request, 'viewmybookings.html', context)

    except:
        pass
    return render(request, 'viewmybookings.html', context)


def submitcontact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")

        subreview = contactform(name=name, email=email,comment=comment)
        subreview.save()
        messages.success(request, 'Your response recorded Successfully.')

    return redirect(contact)

def searchresult(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        Agent = False
        if userdata.role == "agent":
            Agent = True
            print(userdata.role)

        try:
            profiledata = detail_table.objects.get(login_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        if request.method == 'POST':
            ptype = request.POST.get("type")

            search_data = package_details.objects.filter(type_id=package_type_table(id=ptype))

        context = {
            'userdata': userdata,
            'Agent': Agent,
            'profiledata': profiledata,
            'search_data': search_data,
        }

        return render(request, 'searchresults.html', context)

    except:
        if request.method == 'POST':
            ptype = request.POST.get("type")

            search_data = package_details.objects.filter(type_id=package_type_table(id=ptype))

            context = {
                'search_data': search_data,
            }

    return render(request, 'searchresults.html', context)

def destroy(request,id):
    uid=request.session['log_id']
    getdetails=booking_details.objects.get(package_data=id,login_id=uid)
    getdetails.delete()
    return redirect(bookedpackages)

def gallery(request):
    return render(request,'gallery.html')

