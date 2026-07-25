from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket


@login_required
def dashboard(request):

    # Admin sees all tickets
    if request.user.is_staff:

        tickets = Ticket.objects.all()

    else:

        # Employee sees tickets they created OR tickets assigned to them
        tickets = Ticket.objects.filter(
            user=request.user
        ) | Ticket.objects.filter(
            assigned_to=request.user
        )

    # Remove duplicate tickets
    tickets = tickets.distinct()

    # Search
    search = request.GET.get("search", "")

    if search:

        tickets = tickets.filter(
            title__icontains=search
        ) | tickets.filter(
            description__icontains=search
        )

        tickets = tickets.distinct()

    # Status filter
    selected_status = request.GET.get("status", "")

    if selected_status:

        tickets = tickets.filter(
            status=selected_status
        )

    # Priority filter
    selected_priority = request.GET.get("priority", "")

    if selected_priority:

        tickets = tickets.filter(
            priority=selected_priority
        )

    tickets = tickets.order_by("-created_at")

    # Tickets assigned to logged-in user
    assigned_tickets = Ticket.objects.filter(
        assigned_to=request.user
    ).order_by("-created_at")

    context = {

        "tickets": tickets,

        "assigned_tickets": assigned_tickets,

        "search": search,

        "selected_status": selected_status,

        "selected_priority": selected_priority,

        "total_tickets": tickets.count(),

        "open_tickets": tickets.filter(
            status="Open"
        ).count(),

        "in_progress_tickets": tickets.filter(
            status="In Progress"
        ).count(),

        "resolved_tickets": tickets.filter(
            status="Resolved"
        ).count(),

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )