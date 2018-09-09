from django.views.generic.base import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_api.models import *


