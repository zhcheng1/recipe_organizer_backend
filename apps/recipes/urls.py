
from django.conf.urls import patterns, include, url
from django.conf import settings
from views import *

urlpatterns = patterns(
    '',

    url(r'^recipes/$', RecipeList.as_view(), name='recipe-list'),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view(), name='recipe-list'),

    url(r'^add-recipe/$', AddRecipe.as_view(), name='add-recipe'),

    url(r'^send-email/$', SendEmail),

    url(r'^add-review/$', AddReview.as_view(), name='review-list'),
    url(r'^review/(?P<pk>[0-9]+)$', UpdateReview.as_view(), name='review-list'),
    # Handling media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
