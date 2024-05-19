from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from materials.models import Subscription, Course
from users.models import User

from datetime import datetime, timezone , timedelta

@shared_task
def send_email(course_id):
    course = Course.objects.get(pk=course_id)
    subscribers = Subscription.objects.get(course=course_id)

    send_mail(
        subject=f'Курс {course} обновлен',
        message=f'Курс {course},на который вы подписаны обновлён',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscribers.user.email]
        # recipient_list=[subscribers.user.email,'ibish_acmilan@mail.ru']
    )

@shared_task
def check_user():
    active_users = User.objects.filter(is_active=True)
    now = datetime.now(timezone.utc)
    for user in active_users:
        if user.last_login:
            if now - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()
                print(f"Пользователь {user} заблокирован за пассивность")