 #-*- coding: utf-8 -*-
import sys
sys.path.append('..')

import json
import threading
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse

from market import Instruments

# 종목 업데이트시 진행상태를 확인하기 위한 값
UPDATE_STATUS = False 

class SimulatorView(TemplateView):
    template_name = "simulator.html"
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['sectors'] = Instruments.sectors()
       #context['instruments'] = Instruments.get(is_tradable=True, has_history=True)
       context['last_update'] = Instruments.last_update()


       return context

class ChartView(View):
    """ 차트 데이터 반환용 뷰"""
    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        instrument = Instruments.get(code=code)[0]
        #obj = instrument.context_object()
        data = instrument.history().tolist()
        return JsonResponse(data, safe=False)

class UpdateView(View):
    """ 차트데이터 업데이트 """
    def get(self, request, *args, **kwargs):
        global UPDATE_STATUS
        if request.GET.get("action") == 'start':
            UPDATE_STATUS = True
            try:
                t = threading.Thread(target=update_history)
                t.setDaemon(True)
                t.start()
            except:
                print("Update has failed")

        return JsonResponse(UPDATE_STATUS, safe=False)

def update_history():
    global UPDATE_STATUS
    #UPDATE_STATUS = True
    Instruments.update_history()
    Instruments.define_sectors()
    UPDATE_STATUS = False
