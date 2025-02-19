from celery import shared_task

@shared_task(name="reminder_message_send")
def reminder_message_send() -> None:
    pass