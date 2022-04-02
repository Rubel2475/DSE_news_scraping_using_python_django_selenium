from django.urls import URLPattern, path

from .views import news_duration, news_scrape #news_view userpage_view,news_view 

urlpatterns = [
    path('all_news', news_scrape, name="news"),
    path('duration_form', news_duration, name="duration_form"),
    #path('', news_view),
    #path('', userpage_view),
]