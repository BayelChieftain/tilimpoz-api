from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('core.urls')),
                  path('api/team/', include('team.urls')),
                  path('api/faq/', include('faq.urls')),
                  path('api/contacts/', include('contacts.urls')),
                  path('api/qa/', include('qa.urls')),
                  path('api/rules/', include('rules.urls')),
                  path('api/etymology/', include('etymology.urls')),
                  path('api/tilibizde/', include('tilibizde.urls')),
                  path('api/documents/', include('documents.urls')),
                  path('api/books/', include('books.urls')),
                  path('api/categories/', include('categories.urls')),
                  path('api/sozduk/', include('sozduk.urls')),
                  path('api/about/', include('about.urls')),
                  path('api/tests/', include('tests.urls')),
                  path('', RedirectView.as_view(url='/api/', permanent=True)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
