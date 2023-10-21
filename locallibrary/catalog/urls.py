from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("books/", views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorsListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('testlm/', views.libraryMembersOnly, name="test-lib-members"),
    path('form_add/', views.CustomEnter.as_view(), name="custom_enter"),
    path('edit_list/', views.EditList.as_view(), name="custom_edit"),
    path('edit_list/editing/<int:pk>', views.CustomEditing.as_view(), name="custom-edit-instance"),
    path('edit_list/deletion/<int:pk>', views.CustomDeletion, name="custom-delete-instance")
]
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]