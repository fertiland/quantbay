from django.shortcuts import render

from django.views.generic.list import ListView
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Q

from pinganalpha.securities.models import CombineTradeInfo, SummaryTradeInfo, AnalyzeTradeInfo, TechnicalsTradeInfo

# Create your views here.
class CombineSectionsSharpeRatioList(ListView):
    context_object_name = 'section_list'
    def get_queryset(self):
        sections_list = self.kwargs['sections'].split('+')
        delta = int(self.kwargs['delta'])
        sharpeRatio = float(self.kwargs['sharpeRatio'])
        return CombineTradeInfo.objects.filter(section__in=sections_list, createtime__gte=datetime.now()-timedelta(days=delta), sharperatio__gte=sharpeRatio).order_by('code', 'createtime')

class CombineSectionsList(ListView):
    context_object_name = 'section_list'
    def get_queryset(self):
        sections_list = self.kwargs['sections'].split('+')
        delta = int(self.kwargs['delta'])
        return CombineTradeInfo.objects.filter(section__in=sections_list, createtime__gte=datetime.now()-timedelta(days=delta)).order_by('code', 'createtime')

class CombineCodesList(ListView):
    context_object_name = 'section_list'
    def get_queryset(self):
        codes_list = self.kwargs['codes'].split('+')
        delta = int(self.kwargs['delta'])
        return CombineTradeInfo.objects.filter(code__in=codes_list, createtime__gte=datetime.now()-timedelta(days=delta)).order_by('code', 'createtime')

class TechnicalsCodesList(ListView):
    context_object_name = 'section_list'
    def get_queryset(self):
        codes_list = self.kwargs['codes'].split('+')
        delta = int(self.kwargs['delta'])
        return TechnicalsTradeInfo.objects.filter(code__in=codes_list, createtime__gte=datetime.now()-timedelta(days=delta)).order_by('code', 'createtime')

class TechnicalsAlgorithmsList(ListView):
    context_object_name = 'section_list'
    def get_queryset(self):
        codes_list = self.kwargs['codes'].split('+')
        algorithms_list = self.kwargs['algorithms'].split('+')
        delta = int(self.kwargs['delta'])
        return TechnicalsTradeInfo.objects.filter(code__in=codes_list,algorithm__in=algorithms_list, createtime__gte=datetime.now()-timedelta(days=delta)).order_by('code', 'createtime')

class SummarySectionsList(ListView):
    context_object_name = 'section_list'
    def get_queryset(self):
        sections_list = self.kwargs['sections'].split('+')
        delta = int(self.kwargs['delta'])
        return SummaryTradeInfo.objects.filter(section__in=sections_list, createtime__gte=datetime.now()-timedelta(days=delta)).order_by('createtime')

class PredictSectionsList(ListView):
    context_object_name = 'section_list'
    def get_queryset(self):
        sections_list = self.kwargs['sections'].split('+')
        delta = int(self.kwargs['delta'])
        if sections_list[0] == "passedDays":
            return SummaryTradeInfo.objects.filter(Q(section__in=sections_list) & (Q(buyratio__gt=0.8)|Q(buyratio__lt=0.2)) & Q(createtime__gte=datetime.now()-timedelta(days=delta))).order_by('createtime')
        else:
            return SummaryTradeInfo.objects.filter(Q(section__in=sections_list) & (Q(buyratio__gt=0.7)|Q(buyratio__lt=0.3)) & Q(createtime__gte=datetime.now()-timedelta(days=delta))).order_by('createtime')

class AnalyzeSectionsCorrectRatioList(ListView):
    context_object_name = 'section_list'
    def get_queryset(self):
        sections_list = self.kwargs['sections'].split('+')
        delta = int(self.kwargs['delta'])
        correctRatio = float(self.kwargs['correctRatio'])
        return AnalyzeTradeInfo.objects.filter(section__in=sections_list, createtime__gte=datetime.now()-timedelta(days=delta), correctratio__gte=correctRatio).order_by('code', 'createtime')

class AnalyzeSectionsList(ListView):
    context_object_name = 'section_list'
    def get_queryset(self):
        sections_list = self.kwargs['sections'].split('+')
        delta = int(self.kwargs['delta'])
        return AnalyzeTradeInfo.objects.filter(section__in=sections_list, createtime__gte=datetime.now()-timedelta(days=delta)).order_by('code', 'createtime')

class AnalyzeCodesList(ListView):
    context_object_name = 'section_list'
    def get_queryset(self):
        codes_list = self.kwargs['codes'].split('+')
        delta = int(self.kwargs['delta'])
        return AnalyzeTradeInfo.objects.filter(code__in=codes_list, createtime__gte=datetime.now()-timedelta(days=delta)).order_by('code', 'createtime')
