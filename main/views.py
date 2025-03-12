from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .tasks import check_password
from main.models import Task

class PasswordCheckView(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            password = str(request.data['password'])
        except KeyError:
            return Response({"error": "Field password is required"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": "Invalid params"}, status=status.HTTP_400_BAD_REQUEST)


        task = Task.objects.create()

        check_password.delay(password=password, task_id=task.id)
        
        return Response({"task_id": str(task.id)})


class CheckTaskStatus(APIView):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('task_id', None)

        if task_id is None:
            return Response({"error": "Invalid params"}, status=status.HTTP_400_BAD_REQUEST)
        

        task = Task.objects.filter(id=task_id)

        if not task.exists():
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        task_status = 'completed' if task[0].completed else 'processing'
        task = task[0]

        data = None

        if task.instance:
            data = {
                "hashed_password": task.instance.hash_prefix,
                "breach_count": task.instance.breach_count,
                "safe": True if task.instance.breach_count == 0 else False
            }

        return Response({
            "task_id": str(task.id), 
            "status": task_status,
            "data": data            
        })