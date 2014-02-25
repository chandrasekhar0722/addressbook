from django.conf.urls import patterns, include, url
from contacts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.ListContactView.as_view(), name='contacts-list'),
    url(r'^new$', views.CreateContactView.as_view(), name='contacts-new'),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateContactView.as_view(), name='contacts-edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteContactView.as_view(),name='contacts-delete',),
    url(r'^(?P<pk>\d+)/$', views.ContactView.as_view(),name='contacts-view',),
    url(r'^edit/(?P<pk>\d+)/addresses$', views.EditContactAddressView.as_view(),name='contacts-edit-addresses',),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()

