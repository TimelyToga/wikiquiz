from django.conf.urls import patterns, include, url
from django.contrib import admin

import wikiquiz.settings

urlpatterns = patterns('',
    # url(r'^admin/', include(admin.site.urls)),

    ## MAIN
    url(r'^$', 'webfiles.views.home'),
    url(r'^w/(.*)$', 'webfiles.views.quiz'),
    url(r'^t/(.*)$', 'webfiles.views.test'),

    ## DIRECTORIES
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': wikiquiz.settings.JS_DIR}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': wikiquiz.settings.CSS_DIR}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': wikiquiz.settings.IMG_DIR}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': wikiquiz.settings.CSS_DIR}),
    (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': wikiquiz.settings.IMG_DIR}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': wikiquiz.settings.JS_DIR}),
    (r'^robots.txt$', 'django.views.static.serve', {'path': 'robots.txt', 'document_root': wikiquiz.settings.STATIC_DIR, 'show_indexes': False} ),
    (r'^favicon.ico$', 'django.views.static.serve', {'path': 'favicon.ico', 'document_root': wikiquiz.settings.STATIC_DIR, 'show_indexes': False} ),
)
