from django.urls import path
from cv.views import *

urlpatterns = [
	path('', main_view)
]
