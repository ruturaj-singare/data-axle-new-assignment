import logging
logger = logging.getLogger(__name__)
from django.utils import timezone
from django_cron import CronJobBase, Schedule


class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ['08:00']  # Schedule to run at 8 am

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'my_cron_job_to_send_email_events'  

    def do(self):
        print("Running my cron job...!!")
