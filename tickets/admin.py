from django.contrib import admin
from .models import Ticket, Comment, TicketActivity


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'user',
        'assigned_to',
        'priority',
        'status',
        'created_at',
    )

    list_display_links = (
        'id',
        'title',
    )

    list_editable = (
        'assigned_to',
    )

    list_filter = (
        'status',
        'priority',
        'assigned_to',
    )

    search_fields = (
        'title',
        'description',
        'user__username',
        'assigned_to__username',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'ticket',
        'user',
        'created_at',
    )

    search_fields = (
        'text',
        'user__username',
    )


@admin.register(TicketActivity)
class TicketActivityAdmin(admin.ModelAdmin):

    list_display = (
        'ticket',
        'user',
        'action',
        'created_at',
    )

    list_filter = (
        'action',
        'created_at',
    )

    search_fields = (
        'ticket__title',
        'user__username',
        'action',
    )