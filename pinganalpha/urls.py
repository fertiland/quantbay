from django.conf.urls import patterns, include, url
from pinganalpha.views import hello, current_datetime, buyRatioMatplotlib, sellRatioMatplotlib, correctCompositeRatioMatplotlib
from django.contrib import admin
from pinganalpha.securities.views import PredictSectionsList, SummarySectionsList, CombineCodesList, CombineSectionsList,CombineSectionsSharpeRatioList, AnalyzeCodesList, AnalyzeSectionsList, TechnicalsCodesList, TechnicalsAlgorithmsList, AnalyzeSectionsCorrectRatioList

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pingan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    #url(r'', main),
    url(r'^time/$', current_datetime),
    url(r'^buyRatio/$', buyRatioMatplotlib),
    url(r'^sellRatio/$', sellRatioMatplotlib),
    url(r'^correctRatio/$', correctCompositeRatioMatplotlib),
    url(r'^summary/(?P<sections>[\w\+]+)/(?P<delta>[0-9]+)/$', SummarySectionsList.as_view(), name='summary-sections-list'),
    url(r'^predict/(?P<sections>[\w\+]+)/(?P<delta>[0-9]+)/$', PredictSectionsList.as_view(), name='predict-sections-list'),
    url(r'^combine/(?P<codes>[0-9\+]+)/(?P<delta>[0-9]+)/$', CombineCodesList.as_view(), name='combine-codes-list'),
    url(r'^combine/(?P<sections>[\w\+]+)/(?P<delta>[0-9]+)/$', CombineSectionsList.as_view(), name='combine-sections-list'),
    url(r'^combine/(?P<sections>[\w\+]+)/(?P<delta>[0-9]+)/(?P<sharpeRatio>[0-9\.]+)/$', CombineSectionsSharpeRatioList.as_view(), name='combine-sections-sharpe-ratio-list'),
    url(r'^analyze/(?P<codes>[0-9\+]+)/(?P<delta>[0-9]+)/$', AnalyzeCodesList.as_view(), name='analyze-codes-list'),
    url(r'^analyze/(?P<sections>[\w\+]+)/(?P<delta>[0-9]+)/$', AnalyzeSectionsList.as_view(), name='analyze-section-list'),
    url(r'^analyze/(?P<sections>[\w\+]+)/(?P<delta>[0-9]+)/(?P<correctRatio>[0-9\.]+)/$', AnalyzeSectionsCorrectRatioList.as_view(), name='analyze-sections-correct-ratio-list'),
    url(r'^technicals/(?P<codes>[0-9\+]+)/(?P<delta>[0-9]+)/$', TechnicalsCodesList.as_view(), name='technicals-codes-list'),
    url(r'^technicals/(?P<codes>[0-9\+]+)/(?P<algorithms>[\w\+]+)/(?P<delta>[0-9]+)/$', TechnicalsAlgorithmsList.as_view(), name='technicals-codes-list'),
)
