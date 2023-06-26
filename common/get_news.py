from django.db.models import Q

from hospital.apps.web.home.models import LatestNews


def get_latest_news(self):
    
    news = LatestNews.objects.exclude(
        Q(bool_deleted=True)
    ).values('code','author__username', 'image', 'title', 'author__image', 'label', 'datetime_created', 'publish', 'description', 'read_me') \
            .order_by('-datetime_created')
            
    return news
