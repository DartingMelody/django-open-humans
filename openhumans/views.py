import json
import logging
try:
    from urllib2 import HTTPError
except ImportError:
    from urllib.error import HTTPError

from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.safestring import mark_safe

import ohapi
import requests

from .helpers import oh_code_to_member, oh_client_info
OH_BASE_URL = settings.OPENHUMANS_OH_BASE_URL
OH_API_BASE = OH_BASE_URL + '/api/direct-sharing'


def login_member(request):
    code = request.GET.get('code', '')
    try:
        oh_member = oh_code_to_member(code=code)
    except Exception:
        oh_member = None
        print("exception while logging in")
    if oh_member:
        # Log in the user.
        user = oh_member.user
        login(request, user,
              backend='django.contrib.auth.backends.ModelBackend')


def complete(request):
    """
    Receive user from Open Humans. Store data, start data upload task.
    """
    # logger.debug("Received user returning from Open Humans.")

    login_member(request)
    if not request.user.is_authenticated:
        # logger.debug('Invalid code exchange. User returned to start page.')
        print('Invalid code exchange. User returned to start page.')
        return redirect('/')
    else:
        return redirect('overview')
