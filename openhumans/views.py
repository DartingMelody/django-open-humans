
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect

class DeleteConnection(View):
    def post(self, request):
        openhumansmember = request.user.openhumansmember
        logout(request)
        openhumansmember.delete()
        return redirect('index')

        
