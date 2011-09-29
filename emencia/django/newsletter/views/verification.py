# --- subscriber verification --- start ---------------------------------------
"""
Views for emencia.django.newsletter Subscriber Verification

TODO:
    - add language strings
    - add template for mail
"""
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from emencia.django.newsletter.models import SubscriberVerification

def view_subscriber_verification(request, form_class):
    """
    A simple view that shows a form for subscription for the newsletter.
    """
    context = {}

    if request.POST:
        context['form'] = form_class(request.POST)
        subscription = SubscriberVerification()
        if context['form'].is_valid():
            contact = context['form'].save()

            subscription.contact = context['form'].instance
            subscription.save()
            link_id = subscription.link_id

            # select smtpserver, maybe, a boolean field for 'standard' will be
            # a nice idea.
            server = SMTPServer.objects.get(id=1)

            # set server settings to django
            settings.EMAIL_HOST = server.host
            settings.EMAIL_HOST_PASSWORD = server.password
            settings.EMAIL_HOST_USER = server.user
            settings.EMAIL_PORT = server.port
            settings.EMAIL_USE_TLS = server.tls

            # mail settings
            subject = 'Subriber verification'
            message = 'Thanks for Subscription, please klick the following ' \
                'link to Verificate your email adaress.'
            #find a way for a not hardcoded mail.
            from_mail = 'no_reply@freshmilk.de'
            to_mail = context['form'].instance.email

            #add language string
            text_content = '{0}' \
                '\n\n' \
                'http://{1}/newsletters/subscribe/{2}'\
                .format(message, str(request.get_host()), str(link_id))
            html_content = '<body><p>{0}</p>' \
                '<p><a href="http://{1}/newsletters/subscribe/{2}">verify link</a></p></body>'\
                .format(message, str(request.get_host()), str(link_id))
            msg = EmailMultiAlternatives(
                subject,
                text_content,
                from_mail,
                [to_mail]
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

            #dummy, will delete the line after this function is ready.
            #context['form'].instance.delete()

    else:
        context['form'] = form_class()

    return render_to_response('newsletter/subscriber_verification.html',
                              context,
                              context_instance=RequestContext(request))

def view_uuid_verification(request, link_id):
    """
    A simple view that shows if verification is true or false.
    """
    subscription = {}
    context = {}
    context['link_id'] = link_id

    subscription['object'] = SubscriberVerification.objects.get(link_id=link_id)
    subscription['contact'] = subscription['object'].contact

    subscription['contact'].verified = True
    subscription['contact'].save()

    subscription['object'].delete()

    return render_to_response('newsletter/uuid_verification.html',
                              context,
                              context_instance=RequestContext(request))

# --- subscriber verification --- end -----------------------------------------