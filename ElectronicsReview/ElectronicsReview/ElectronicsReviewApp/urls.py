""" https://stackoverflow.com/questions/14286292/reference-a-url-with-an-id-by-name-in-django """

from django.urls import path, reverse
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import user_profile, edit_review, delete_review, ReviewDetailView, contact_us_view, contact_us_success_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('products', views.products, name='products'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('products/<int:product_id>/view_reviews/', views.view_reviews, name='view_reviews'),
    path('products/<int:product_id>/leave_reviews/', views.leave_reviews, name='leave_reviews'),
    path('profiles/<int:user_profile_id>/', user_profile, name='user_profile'),
    path('<int:product_id>/edit_review/<int:review_id>/', edit_review, name='edit_review'),
    path('<int:product_id>/delete_review/<int:review_id>/', delete_review, name='delete_review'),
    path('products/<int:product_id>/reviews/<int:review_id>/', ReviewDetailView.as_view(), name='review_detail'),
    path('contact_us/', contact_us_view, name='contact_us'),
    path('contact_us/success/', contact_us_success_view, name='contact_us_success'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    ]

"""  https://stackoverflow.com/questions/38379084/django-not-serving-media-files-if-i-check-for-settings-debug """
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
