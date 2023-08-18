from datetime import date
from django.core.mail import send_mail
from event_template_app.models import StoredTemplate
from django.conf import settings
from .constants import *


def send_anniversary_birthday_emails(employee, template_id):
    
    try:
        stored_template = StoredTemplate.objects.get(id=template_id)
    except StoredTemplate.DoesNotExist:
        return False

    context = {
        SEND_EMAIL_KEY_EMPLOYEE: employee,
    }

    subject = stored_template.render_template({SEND_EMAIL_KEY_SUBJECT: employee.name})
    message = stored_template.render_template(context)
    recipient_list = [employee.email]

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
    
    return True
