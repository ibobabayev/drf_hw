from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
@shared_task
def send_email(course,request):
    send_mail(
        subject='Курс обновлен',
        message=f'Курс {course},на который вы подписаны обновлён',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email,'ibish_acmilan@mail.ru']
        # recipient_list=[request.user.email]
    )