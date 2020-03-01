from django.urls import path, include
from django.views.generic import RedirectView

from .views import SimulatorView, ChartView, UpdateView

urlpatterns = [
    path('', SimulatorView.as_view(), name='simulator'),
    path('chart/<str:code>', ChartView.as_view(), name='chart'),
    path('update', UpdateView.as_view(), name='update'),
]