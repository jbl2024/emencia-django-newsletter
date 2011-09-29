"""Utils for newsletter"""
from BeautifulSoup import BeautifulSoup
from django.core.urlresolvers import reverse

from emencia.django.newsletter.models import Link

# --- tracking ankers --- start -----------------------------------------------
from emencia.django.newsletter.settings import TRACKING_ANKERS
# --- tracking ankers --- end -------------------------------------------------


def body_insertion(content, insertion, end=False):
    """Insert an HTML content into the body HTML node"""
    if not content.startswith('<body'):
        content = '<body>%s</body>' % content
    soup = BeautifulSoup(content)

    if end:
        soup.body.append(insertion)
    else:
        soup.body.insert(0, insertion)
    return soup.prettify()


def track_links(content, context):
    """Convert all links in the template for the user
    to track his navigation"""
    if not context.get('uidb36'):
        return content

    soup = BeautifulSoup(content)
    for link_markup in soup('a'):
        if link_markup.get('href') and \
               'no-track' not in link_markup.get('rel', ''):

            # --- tracking ankers --- start -----------------------------------
            if TRACKING_ANKERS:
                if '#' in link_markup.get('href')[0]:
                    continue
            # --- tracking ankers --- end -------------------------------------

            link_href = link_markup['href']
            link_title = link_markup.get('title', link_href)
            link, created = Link.objects.get_or_create(url=link_href,
                                                       defaults={'title': link_title})
            link_markup['href'] = 'http://%s%s' % (context['domain'], reverse('newsletter_newsletter_tracking_link',
                                                                              args=[context['newsletter'].slug,
                                                                                    context['uidb36'], context['token'],
                                                                                    link.pk]))
    return soup.prettify()
