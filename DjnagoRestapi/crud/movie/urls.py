#========== i have created urls.py file to create a urls pattern for my api=====
#========== i have used router to cresate ulrs for modelviewset==========
#========= then i register model viwset modelviewset router=======
#========== also used path and include to create and add a url  path=======



from rest_framework.routers import DefaultRouter
from .views import movieset
from django.urls import path, include

router = DefaultRouter()
router.register('movie', movieset)

urlpatterns = [
    path('api/',include(router.urls))
]
