from django.urls import path

from category import views

urlpatterns = [
    path('create_category/', views.CategoryCreateView.as_view(),
         name='create-category'),
    path('list_of_category/', views.CategoryListView.as_view(),
         name='list-of-category'),
    path('update_category/<int:pk>', views.CategoryUpdateView.as_view(),
         name='update-category'),
    path('delete_category/<int:pk>', views.CategoryDeleteView.as_view(),
         name='delete-category'),
    path('details_category/<int:pk>', views.CategoryDetailView.as_view(),
         name='details-category'),
]
