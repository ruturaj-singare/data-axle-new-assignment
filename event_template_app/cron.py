from django.utils import timezone
from django_cron import CronJobBase, Schedule
from utils.event_functions import send_birthday_emails, send_work_anniversary_emails
from utils.constants import MY_CRON_JOB_TO_SEND_EMAIL_EVENTS, RUN_CRON_TIMINGS

class MyCronJob(CronJobBase):
    RUN_AT_TIMES = RUN_CRON_TIMINGS

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = MY_CRON_JOB_TO_SEND_EMAIL_EVENTS  
    
    def do(self):
        try:
            print("Running my cron job...!!")
            send_birthday_emails()
            send_work_anniversary_emails()
        except Exception as e:
            print("Exception->", e)

