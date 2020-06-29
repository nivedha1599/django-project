"""pra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from pra import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView
from django.conf.urls import url, include
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap



sitemaps = {
    "posts": PostSitemap,
}




urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^courses/', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^$', CourseListView.as_view(), name='course_list'),
    url(r'^upload/', include('profile_maker.urls')),
    url(r'^blogs/', include('blogs.urls')),
    url(r'^chat/', include('chat.urls')),
    url(r'^blog/', include('blog.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^polls/', include('polls.urls')),
    path('', include('LMSapp.urls')),
    # path('cart/', include('cart.urls')),
    # path('', include('quiz.urls')),
 
    
   
    
   
   
   
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
