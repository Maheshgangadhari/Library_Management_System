from django.urls import include, path
from rest_framework import routers
from BOOKS import views

router = routers.DefaultRouter()
router.register(r'books', views.BooksViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

    # above is api urls

    # here django urls
    # path('showbook/', views.show_view),
    # path('insert/', views.insert_view),
    # path('delete/<int:id>', views.delete_view),
    # path('update/<int:id>', views.update_view), 
    
]

