"""
Create your views here.
"""
from django.views import View
from django.shortcuts import redirect


class DeleteFile(View):

    def post(self, request):
        """
        Delete specified file in Open Humans for this project member.
        """
        if request.user.is_authenticated:
            oh_member = request.user.openhumansmember
            file_id = None
            file_basename = None
            if "file_id" in request.POST:
                file_id = request.POST["file_id"]
            if "file_basename" in request.POST: 
                file_basename = request.POST["file_basename"]
            next_url = request.POST["next_url"]
            oh_member.delete_single_file(
                file_id=file_id,
                file_basename=file_basename)
            return redirect(next_url)
        return redirect(next_url)


class DeleteAllFiles(View):

    def post(self, request):
        """
        Delete all project files in Open Humans for this project member.
        """
        if request.user.is_authenticated:
            next_url = request.POST["next_url"]
            oh_member = request.user.openhumansmember
            oh_member.delete_all_files()
            return redirect(next_url)
        return redirect(next_url)
