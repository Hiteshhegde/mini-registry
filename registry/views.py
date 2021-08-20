from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import DomainName
# Create your views here.

class DomainnameView(View):

    def get(self,request, **kwargs):
        domainname = get_object_or_404(DomainName, pk=1)
        return HttpResponse(f"This is {domainname.domain_name} home")

    def post(self, request, **kwargs):
        form = request.POST
        return 

    def patch(self, request):
        form = request.POST
        return
    
    def delete(self, request, **kwargs):
        domainname = get_object_or_404(DomainName, pk= kwargs)
        return 

