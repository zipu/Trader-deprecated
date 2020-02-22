 #-*- coding: utf-8 -*-
import sys
sys.path.append('..')

import json

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse

from market import Instruments

class SimulatorView(TemplateView):
    template_name = "simulator.html"
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['instruments'] = Instruments.get(is_tradable=True, has_history=True)

       return context

class ChartView(View):
    """ 차트 데이터 반환용 뷰"""
    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        instrument = Instruments.get(code=code)[0]
        #obj = instrument.context_object()
        data = instrument.history().tolist()
        return JsonResponse(data, safe=False)

class UpdateHistoryView(View):
    """ 차트데이터 업데이트 """
    def get(self, request, *args, **kwargs):
        try:
            Instruments.update_history()
            result = "Done"
        except:
            result = "Update has failed"
        
        return JsonResponse(result, safe=False)