# --- subscriber verification --- start ---------------------------------------
"""
Views for emencia.django.newsletter Subscriber Verification
"""
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from emencia.django.newsletter.models \
    import Newsletter, MailingList, SubscriberVerification
from emencia.django.newsletter.mailer import Mailer

def view_subscriber_verification(request, form_class):
    """
    A simple view that shows a form for subscription for the newsletter.
    """
    context = {}

    if request.POST:
        context['form'] = form_class(request.POST)
        subscription = SubscriberVerification()
        if context['form'].is_valid():
            context['form'].save()
            contact_mail = context['form'].instance.email

            subscription.contact = context['form'].instance
            subscription.save()
            link_id = subscription.link_id

            message = 'Thanks for Subscription, please klick the following' \
                'link to Verificate your email adaress.' \
                '' \
                'http://localhost:8000/newsletters/subscribe/{0}'\
                .format(str(link_id))

            #create mailing list with the one contact
            mailing_list =

            #use emencia mailer
            newsletter = Newsletter
            with newsletter as n:
                n.title = 'Hello World'
                n.content = '<body>Hello World</body>'
                n.mailing_list = ''
                n.test_contacts = ''

            #print dir(newsletter.content)
            """
            mailer = Mailer(newsletter, test=True)
            try:
                mailer.run()
            except HTMLParseError:
                self.message_user(request, _('Unable send newsletter, due to errors within HTML.'))
            self.message_user(request, _('%s succesfully sent.') % newsletter)
            """

            #dummy, will delete the line after this function is ready.
            context['form'].instance.delete()

    else:
        context['form'] = form_class()

    return render_to_response('newsletter/subscriber_verification.html',
                              context,
                              context_instance=RequestContext(request))

# --- subscriber verification --- end -----------------------------------------