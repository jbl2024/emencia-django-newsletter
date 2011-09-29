# --- subscriber verification --- start ---------------------------------------
"""Urls for the emencia.django.newsletter Subscriber Verification"""
from django.conf.urls.defaults import url, patterns

from emencia.django.newsletter.forms import SubscriberVerificationForm

urlpatterns = patterns(
    'emencia.django.newsletter.views.verification',
    url(
        r'^$',
        'view_subscriber_verification',
        {'form_class': SubscriberVerificationForm},
        name='newsletter_subscriber_verification',
    ),
    url(r'^([\w-]+)/$', 'view_uuid_verification'),
)

# --- subscriber verification --- end -----------------------------------------