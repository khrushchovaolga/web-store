from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('<slug:cat_slug>/', get_category, name='category'),
    path('<slug:cat_slug>/<slug:subcat_slug>/', get_subcategory, name='subcategory'),
    path('<slug:cat_slug>/<slug:subcat_slug>/<int:product_pk>/', product, name='product'),
    path('newfeedback/<int:product_pk>/', get_feedback, name='feedback'),
    path('newquestion/<int:product_pk>/', get_question, name='question'),
]