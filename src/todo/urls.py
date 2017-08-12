from django.conf.urls import url, include
from todo import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
# trailing_slash = False means http://localhost/todos  and http://localhost/todos/15
# trailing_slash = True  means http://localhost/todos/ and http://localhost/todos/15/
router = DefaultRouter(trailing_slash=False)
# Register the view class that we previously created
router.register(r'todos', views.TodoItemViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
]

