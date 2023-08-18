import logging
logger = logging.getLogger(__name__)
from django.utils import timezone
from django_cron import CronJobBase, Schedule
from utils.event_functions import send_anniversary_birthday_emails, send_birthday_emails

class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ['08:00']  # Schedule to run at 8 am

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'my_cron_job_to_send_email_events'  

    def do(self):
        print("Running my cron job...!!")
        send_birthday_emails()
        send_anniversary_birthday_emails()
