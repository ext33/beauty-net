from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# Outputs Vue app
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

# There write your API views
