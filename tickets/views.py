from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Ticket, Comment, TicketActivity
from .forms import TicketForm, CommentForm


@login_required
def create_ticket(request):

    if request.method == "POST":

        form = TicketForm(request.POST)

        if form.is_valid():

            ticket = form.save(
                commit=False
            )

            ticket.user = request.user

            ticket.save()

            TicketActivity.objects.create(
                ticket=ticket,
                user=request.user,
                action="Ticket created"
            )

            return redirect(
                "ticket_detail",
                ticket_id=ticket.id
            )

    else:

        form = TicketForm()

    return render(
        request,
        "tickets/create_ticket.html",
        {
            "form": form
        }
    )


@login_required
def ticket_detail(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(
                commit=False
            )

            comment.ticket = ticket

            comment.user = request.user

            comment.save()

            TicketActivity.objects.create(
                ticket=ticket,
                user=request.user,
                action="Comment added"
            )

            return redirect(
                "ticket_detail",
                ticket_id=ticket.id
            )

    else:

        form = CommentForm()

    return render(
        request,
        "tickets/ticket_detail.html",
        {
            "ticket": ticket,
            "form": form
        }
    )


@login_required
def resolve_ticket(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    ticket.status = "Resolved"

    ticket.save()

    return redirect(
        "dashboard"
    )


@login_required
def update_ticket(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    # Only admin or the assigned employee can update the ticket
    if not request.user.is_staff and ticket.assigned_to != request.user:

        return redirect(
            "ticket_detail",
            ticket_id=ticket.id
        )

    if request.method == "POST":

        ticket.priority = request.POST.get(
            "priority"
        )

        ticket.status = request.POST.get(
            "status"
        )

        ticket.save()

        return redirect(
            "ticket_detail",
            ticket_id=ticket.id
        )

    return render(
        request,
        "tickets/update_ticket.html",
        {
            "ticket": ticket
        }
    )


@login_required
def delete_ticket(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    if request.method == "POST":

        ticket.delete()

        return redirect(
            "dashboard"
        )

    return render(
        request,
        "tickets/delete_ticket.html",
        {
            "ticket": ticket
        }
    )