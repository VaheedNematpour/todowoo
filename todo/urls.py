from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('todo', views.TodoViewSet, basename='todos')

todo_router = routers.NestedDefaultRouter(router, 'todo', lookup='todos')
todo_router.register('completed', views.CompletedTodoViewSet,
                     basename='completed-todo')

urlpatterns = router.urls + todo_router.urls
