from landing.models import Leave
from django.contrib import messages
from landing.forms import LeaveForm
from django.shortcuts import render, redirect


def index_view(request):
    leaves = Leave.objects.filter(user=request.user)

    pending = leaves.filter(status="pending")
    rejected = leaves.filter(status="rejected")
    accepted = leaves.filter(status="accepted")

    context = {"pending": pending, "rejected": rejected, "accepted": accepted}
    return render(request, "dashboard/index.html", context)


def request_view(request):
    leaves = Leave.objects.filter(user=request.user)

    context = {"leaves": leaves}
    return render(request, "dashboard/request.html", context)


def leave_view(request):
    if request.method == "POST":
        form = LeaveForm(request.POST)

        if form.is_valid() and form.save():
            messages.success(request, "Leave request created successfully")
        else:
            messages.error(request, "Failed to submit a leave request")
        return redirect("account:leave-view")

    return render(request, "dashboard/leave.html")
