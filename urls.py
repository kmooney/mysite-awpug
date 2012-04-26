from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from library.models import Author
from library.views import AddAuthorView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^hello_world/$', 'library.views.hello_world'),
    url(r'^books/$', 'library.views.book_index'),
    url(r'^books/(\d+)/$', 'library.views.book_detail'),
    url(r'^request_details/$', 'library.views.request_details'),
    url(r'^add_author/$', 'library.views.add_author'),
    url(r'^authors/$', ListView.as_view(model=Author)),
    url(r'^add_author_class/$', csrf_exempt(AddAuthorView.as_view())),
)
