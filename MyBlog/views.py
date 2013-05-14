from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from Blogdetail.models import Blogs
import settings


def welcome(requset):
    t = get_template('welcome.html')
    print settings.get_path('/static/')
    html = t.render(Context({"STATIC_URL":settings.get_path('/static/')}))
    return HttpResponse(html)

def list_all(requset):
    try:
        data = Blogs.objects.all()
    except Exception, e:
        print e
        data = {}
    t = get_template('list_all.html')
    html = t.render(Context({'data':data,'STATIC_URL':settings.get_path('/static/')}))
    return HttpResponse(html)

def details(requset,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('time.html')
    html =  t.render(Context({'date':dt,'hours':offset}))
    return HttpResponse(html)
