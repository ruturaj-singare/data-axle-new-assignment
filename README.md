# data-axle-new-assignment

We need to add crontab command to crontab -e file of system.

Add below command,

0 8 * * * /path/to/your/virtualenv/bin/python /path/to/your/project/manage.py my_cron_job_notify
