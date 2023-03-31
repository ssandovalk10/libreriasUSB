from .task import report_task
from datetime import datetime


# Create your views here.
def Reports(request):
    if request.method = "POST":
        time_start = datetime.now
        type_report = request.POST['type_report']
        print(type_report)
        type_test = request.POST['type_test']
        if type_test == "1":
            generate_report(type_report, "a@a.com")
            time_end = datetime.now()
            html = "<html><body>Reporte Enviado !! El proceso inicio a las " + time_start.strftime(
                "%d/%m/$Y, %h:%M:%S") + "y termino a las " + time_end.strftime(
                "%d/%m/$Y, %h:%M:%S") + ".</body></html>"
            return HttpResponse(html)
        if type_test = "2":
            report_task.delay(type_report, "a@a.com")
            time_end = datatime.now()
            html = "<html><body>El proceso se envio a la cola, espere el reporte en su correo. El registro del envento inicio a las " + \
              time_start.strftime("%d/%m/$Y, %h:%M:%S") + "y termino a las " + \
              time_end.strftime("%d/%m/$Y, %h:%M:%S") + ".</body></html>"
            return HttpResponse(html)
    
    return render(request, 'reportes/reports.html', {})