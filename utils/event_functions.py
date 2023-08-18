from datetime import date
from employee_app.models import Employee
from .utility_functions import send_anniversary_birthday_emails

def send_work_anniversary_emails():
    today = date.today()
    employees = Employee.objects.filter(hire_date__month=today.month, hire_date__day=today.day)

    for employee in employees:
        template_id = 1  # ID of  "Work Anniversary" template
        send_anniversary_birthday_emails(employee, template_id)

def send_birthday_emails():
    today = date.today()
    employees = Employee.objects.filter(birth_date__month=today.month, birth_date__day=today.day)

    for employee in employees:
        template_id = 2  # ID of the "Birthday" template
        send_anniversary_birthday_emails(employee, template_id)
