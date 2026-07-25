from django.urls import path
from . import views


urlpatterns = [

    path(
        'create/',
        views.create_ticket,
        name='create_ticket'
    ),

    path(
        '<int:ticket_id>/',
        views.ticket_detail,
        name='ticket_detail'
    ),

    path(
        '<int:ticket_id>/resolve/',
        views.resolve_ticket,
        name='resolve_ticket'
    ),

    path(
        '<int:ticket_id>/update/',
        views.update_ticket,
        name='update_ticket'
    ),

    path(
        '<int:ticket_id>/delete/',
        views.delete_ticket,
        name='delete_ticket'
    ),

]