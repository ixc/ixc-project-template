"""
Views for ``{{ project_name }}`` app.
"""

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse


def index(request):
    context = {}
    return TemplateResponse(request, '{{ project_name }}/index.html', context)
