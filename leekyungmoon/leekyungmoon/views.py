from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View



class HomeView(TemplateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class kbo_salary_randomforest_pdf_view(View):
    def get(self, request, *args, **kwargs):
        with open('/Users/kyungmoon/leekyungmoon.com/leekyungmoon/leekyungmoon/test_cv.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'filename=test_cv.pdf'
            return response

"""
def kbo_salary_randomforest_pdf_view(request):
    print('request came')
    with open('/Users/kyungmoon/leekyungmoon.com/leekyungmoon/leekyungmoon/test_cv.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=test_cv.pdf'
        return response
"""