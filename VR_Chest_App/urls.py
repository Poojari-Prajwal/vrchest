from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('saveFeedback/',views.saveFeedback, name='saveFeedback'),
    path('book-appointment', views.appointment, name='book-appointment'),
    path('Appointment-confirm', views.appointmentConfirm, name='Appointment-confirm'),
    path('get_available_time_slots', views.get_available_time_slots, name='get_available_time_slots'),
    path('staff', views.staff, name='staff'),
    path('login', views.logins, name='login'),
    path('logout', views.logout, name='logout'),
    path('show-appointments', views.showAppointments, name='show-appointments'),
    # path('handle-requests', views.handleRequests, name='handle-requests'),
    # path('request-accept', views.requestAccept, name='request-accept'),
    # path('request-reject', views.requestReject, name='request-reject'),
    # path('show-accepted-requests', views.showAcceptRequests, name='show-accepted-requests'),
    # path('show-rejected-requests', views.showRejectRequests, name='show-rejected-requests'),
    path('book-appointment-for-Vasunethra-staff', views.bookAppointmentStaffVasu, name='book-ppointment-vasu-staff'),
    path('book-appointment-for-Veni-staff', views.bookAppointmentStaffVeni, name='book-ppointment-veni-staff'),
    path('book-appointment-staff-confirm',views.bookAppointmentStaffConfirm, name='book-appointment-staff-confirm'),
    path('show-gallery-images', views.showGalleryImages, name='show-gallery-iamges'),
    path('delete-gallery-images', views.deleteGalleryImages, name='delete-gallery-iamges'),
    path('add-gallery-images', views.addGalleryImages, name='add-gallery-images'),
    path('add-reviews', views.addReviews, name='add-reviews'),
    path('edit-or-delete-reviews', views.editOrDeleteReviews, name='edit-or-delete-reviews'),
    path('submit-review', views.submitReview, name='submit-review'),
    path('delete-review', views.deleteReview, name='delete-review'),
    path('show-feedback', views.showFeedback, name='show-feedback'),
    path('delete-feedback', views.deleteFeedback, name='delete-feedback'),
    path('edit-review/<review_id>', views.editReview, name='edit-review'),
    path('show-upcoming-appointments', views.showUpcomingAppointments, name='show-upcoming-appointments'),
    path('facilities', views.facilities, name='facilities'),
    path('gallery', views.gallery, name='gallery'),
    path('add-article', views.addArticle, name='add-article'),
    path('edit-or-delete-article',views.editOrDeleteArticle, name='edit-or-delete-article'),
    path('delete-article',views.deleteArticle, name='delete-article'),
    path('edit-article/<article_id>', views.editArticle, name='edit-article'),
    path('submit-article', views.submitArticle, name='submit-article'),
    path('articles',views.articles, name='articles'),
    path('articles/<article_slug>', views.individualArticle, name='individual-article'),
    path('appointments/dr-vasunetra', views.vasuAppointments, name='dr-vasunetra'),
    path('appointments/dr-veni', views.veniAppointments, name='dr-veni'),
    path('show-today-appointments', views.showTodayAppointments, name='show-today-appointments'),
]