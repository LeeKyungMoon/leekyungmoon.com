import os
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class HomeView(TemplateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class kbo_salary_prediction_modeling_randomforest_pdf_view(View):
    def get(self, request, *args, **kwargs):
        current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        current_path += '/leekyungmoon/project/kbo-salary-prediction-modeling-randomforest.pdf'
        with open(current_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'filename=kbo-salary-prediction-modeling-randomforest.pdf'
            return response


class kcc17_are_you_overestimated(View):
    def get(self, request, *args, **kwargs):
        current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        current_path += '/leekyungmoon/publish/kcc17_are_you_overestimated.pdf'
        with open(current_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'filename=kcc17_are_you_overestimated.pdf'
            return response


class CV_view(View):
    def get(self, request, *args, **kwargs):
        current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        current_path += '/leekyungmoon/cv.pdf'
        with open(current_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'filename=cv.pdf'
            return response