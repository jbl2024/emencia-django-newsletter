# --- templates --- start -----------------------------------------------------
import os
from django.conf import settings

def get_templates():
    return ((i,i) for i in os.walk(settings.TEMPLATE_DIRS[0]+'/mailtemplates/').next()[1])
# --- templates --- end -------------------------------------------------------