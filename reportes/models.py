from django.db import models

# Create your models here.
class ReportTask(models.Model):
    PENDING = 'PENDING'
    FAILURE = 'FAILURE'
    SUCCESS = 'SUCCESS'
    TASK_STATUS_CHOICES = [
        (PENDING, 'Pendiente'),
        (FAILURE, 'Fracaso'),
        (SUCCESS, 'Exito'),
    ]

    SALES_REPORT = 'SALES REPORT'
    TOP_SELLING_BOOKS = 'TOP_SELLING_BOOOKS'
    REPORT_CHOICES = [
        (SALES_REPORT, 'Reporte de ventas por Libreria'),
        (TOP_SELLING_BOOKS, 'Top de libros vendidos'),
    ]
    type_load = models.CharField('Tipo de reporte', max_length=50, choices=REPORT_CHOICES)
    created_at = models.DateTimeField('Fecha de creación', null=False, blank=False)
    task_id = models.CharField('ID', max_length=100, null=True, blank=True)
    task_status = models.CharField('Estado', max_length=10, choices=TASK_STATUS_CHOICES, default=PENDING)
    task_end = models.DateTimeField('Fin de ejecución', null=True, blank=True)

    def __str__(self):
        return f"Tarea de Reporte - {self.task_id}"

    class Meta:
        verbose_name = 'Tarea de Reporte'
        verbose_name_plural = 'Tareas de Reportes'