from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup


from email_sender.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


from django.shortcuts import render, HttpResponse
from first_app.forms import UserForm
# Create your views here.
from first_app.models import UserSignUp
def base(request):
    return render(request,"index.html")
def register(request):
    form = UserForm(request.POST)
    registered = False
    if form.is_valid():
        user = form.save(commit=False)
        if UserSignUp.objects.filter(email=user.email).exists():
            return render(request, 'already.html')
        else:
            user.save()
            registered = True
            email_id = request.POST.get('email')
            print(email_id)
            l=[]
            l.append(email_id)
            subject = "Newsletter"

            message ="""
            Thank you, for subscribing to our newsletter,
            We hope that it will be beneficial for you.
            
            
            
            Regards:
            Rishabh Maheshwari
            """
            recepient = l
            send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently=False)
    return render(request, 'home.html', {'form': form, 'registered': registered})


def sent_mail(request):
    details = UserSignUp.objects.all()
    l1 = list(details)
    l = []
    for detail in details:
        l.append(detail.email)
        # print(detail.email)

    url = "https://www.mohfw.gov.in/"

    uClient = ureq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, 'html.parser')
    a = page_soup.tr.findAll("th")
    l2 = []
    for i in a:
        l2.append(i.text)
    del l2[0]
    l2[0] = 'States'
    l2[1] = 'Total Cases'
    l2[2] = 'Cured'
    s2 = "      ||      ".join(l2)
    s2 = s2 + "      ||      "
    b = page_soup.tbody.findAll("tr")
    # l8 = []
    s1 = ""
    del b[0]
    l10 = []
    s4 = ""
    z = b[-2].findAll("td")
    for i in range(0, len(z)):
        l10.append(z[i].text)
    s11 = f"{l10[0]}:  {l10[1]}"
    s12 = f"Cured: {l10[2].strip()}"
    s13 = f"Death: {l10[3].strip()}"
    s14 = f"To get more details on COVID-19, Visit: {url}"
    s4 = s11 + "\n " + s12 + "\n " + s13 + "\n"
    s15 = """
        Stay Safe, Stay At Home
        Regards: Rishabh Maheshwari"""

    for i in range(len(b) - 3):
        c = b[i].findAll("td")
        s = ""

        # l7=[]
        for j in range(1, len(c)):
            # l7.append(c[j].text)
            s = s + c[j].text + "      ||      "
        # l8.append(l7)
        s1 = s1 + s + "\n"
    s1 = s4 + "\n" + "\n" + s14 + "\n" + s2 + "\n" + "\n" + s1 + "\n" + s15
    # print(s1)
    subject = "Corona live updates"

    message = s1
    recepient = l
    send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently=False)
    return render(request, 'sent.html')













