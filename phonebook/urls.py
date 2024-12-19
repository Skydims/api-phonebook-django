
# phonebook/urls.py
from rest_framework.routers import DefaultRouter  # Pastikan ini ada
from .views import ContactViewSet

router = DefaultRouter()
router.register('contacts', ContactViewSet, basename='contact')

urlpatterns = router.urls
