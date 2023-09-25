from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from .tasks import add_numbers
from huey.contrib.djhuey import HUEY
from huey.exceptions import TaskException

# Create your views here.
def addnum_view(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    task = add_numbers(a,b)

    # Redirect to the view to retrieve the task result, passing the task_id as a URL parameter
    #return HttpResponseRedirect(f'/huey/{task.id}/')
    return HttpResponse(f'The result available at:\n\t<a href="localhost:8000/huey/{task.id}/">link</a>')

def get_task_result(request, task_id):
    try:
        # Retrieve the task result using the task_id
        task_result = HUEY.result(task_id)

        if task_result:
            return HttpResponse(f'result: {task_result}')
        else:
            return HttpResponse('error: Task failed or is still pending')

    except TaskException:
        return HttpResponse('error: Task not found')
    
def wait_test(request):
    return render(request,"hueytask/wait.html",{})

def check_task_status(request):
    # Implement logic to check the status of the task
    debu = False
    if debu:  # Replace with your logic to check if the task is complete
        return JsonResponse({'status': 'task_complete'})
    else:
        return JsonResponse({'status': 'task_running'})