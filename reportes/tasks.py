from celery import shared_task
from celery.signals import task_postrun
from .report_handler import generate_report
from datetime import datetime
from .models import ReportTask

@shared_task
def report_task(type_report, email_recipient):
    reportTask = ReportTask.objects.create(
        task_id = report_task.request.id.__str__(),
        task_status = ReportTask.PENDING,
        type_load = type_report,
        created_at = datetime.now()
    )
    generate_report(type_report, email_recipient)
    reportTask.task_status = ReportTask.SUCCESS
    reportTask.save()

@task_postrun.connect(sender=report_task)
def bulk_load_task_postrun(
    signal=None, sender=None,task_id=None, task=None,
    args=None, kwargs=None, retval=None, state=None, **extras):

    reportTask = ReportTask.objects.get(task_id=task_id)
    reportTask.task_end = datetime.now()
    reportTask.save()

    #si la tarea sufre alguna excepcion no capturada
    if reportTask.task_status == 'PENDING':
        reportTask.task_status = state
        reportTask.save()
        

