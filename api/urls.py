from django.urls import path
from .views import(
    MyView,add_product,myview,MyViev
)

urlpatterns = [
    path('add/',add_product),
    path('all/',MyView.as_view()),
    path('delete/<int:pk>',myview.as_view()),
    path("name/<name>/",MyView.as_view()),
    path("color/<color>/",MyView.as_view()),
    path('price/<price>/',MyView.as_view()),
    path('gte/<int:pk>',MyView.as_view()),
    path('update/<int:id>',MyViev.as_view()),
    path('models/<str:name>', MyView.as_view())
]
