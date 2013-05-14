# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from models import *
from MyBlog import settings


def detail(requeset,page):
    try:
        page = int(page)
    except ValueError:
        raise Http404()
    try:
        pagedetail = Blogs.objects.get(id=page)
    except Exception, e:
        print e
        pagedetail = {}
    print pagedetail.photo.name
    name = pagedetail.photo.name.split('/')[-1]
    print name
    t = get_template('pagedetail.html')
    html =  t.render(Context({'passage':pagedetail,'name':name,'STATIC_URL':settings.get_path('/static/')}))
    return HttpResponse(html)

