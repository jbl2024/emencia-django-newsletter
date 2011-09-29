"""Default urls for the emencia.django.newsletter"""
from django.conf.urls.defaults import url, include, patterns

urlpatterns = patterns('',
    url(r'^mailing/', include('emencia.django.newsletter.urls.mailing_list')),
    url(r'^tracking/', include('emencia.django.newsletter.urls.tracking')),
    url(r'^statistics/', include('emencia.django.newsletter.urls.statistics')),
    # --- subscriber verification --- start -----------------------------------
    url(r'^subscribe/',
        include('emencia.django.newsletter.urls.verification')
    ),
    # --- subscriber verification --- end -------------------------------------
    url(r'^', include('emencia.django.newsletter.urls.newsletter')),
)
