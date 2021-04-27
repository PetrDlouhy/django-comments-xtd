from django.conf.urls import url
from django.views.generic import ListView

from .models import Quote
from .views import QuoteDetailView


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Quote.objects.published()),
        name='quotes'),

    url((r'^(?P<slug>[-\w]+)/$'), QuoteDetailView.as_view(),
        name='quote-detail'),
]
