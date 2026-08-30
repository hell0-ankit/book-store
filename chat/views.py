from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.cache import never_cache
from .models import ChatMessage

User = get_user_model()


def customer_chat_view(request):
    return render(request, "chat/customer_chat.html")


@require_POST
def send_message(request):
    if not request.user.is_authenticated:
        return JsonResponse(
            {"status": "unauthorized", "message": "Please log in first."},
            status=401,
        )

    msg_text = request.POST.get("message", "").strip()
    target_user_id = request.POST.get("user_id")

    if not msg_text:
        return JsonResponse({"status": "error", "message": "Message cannot be empty."}, status=400)

    if request.user.is_staff and target_user_id:
        chat_user = get_object_or_404(User, id=target_user_id)
        is_admin_msg = True
    else:
        chat_user = request.user
        is_admin_msg = False

    msg = ChatMessage.objects.create(
        user=chat_user,
        sender=request.user,
        message=msg_text,
        is_admin=is_admin_msg,
    )

    return JsonResponse({
        "status": "ok",
        "message": msg.message,
        "is_admin": msg.is_admin,
        "timestamp": msg.timestamp.strftime("%I:%M %p"),
    })


@never_cache
@require_GET
def get_messages(request):
    if not request.user.is_authenticated:
        return JsonResponse({"authenticated": False, "messages": []})

    target_user_id = request.GET.get("user_id")

    if request.user.is_staff and target_user_id:
        chat_user = get_object_or_404(User, id=target_user_id)
    else:
        chat_user = request.user

    messages = ChatMessage.objects.filter(user=chat_user).select_related("sender").order_by("timestamp")
    
    data = [
        {
            "id": m.id,
            "sender": m.sender.username,
            "message": m.message,
            "is_admin": m.is_admin,
            "is_me": m.sender_id == request.user.id,
            "timestamp": m.timestamp.strftime("%I:%M %p"),
        }
        for m in messages
    ]

    response = JsonResponse({"authenticated": True, "messages": data})
    response["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    return response


@user_passes_test(lambda u: u.is_staff)
def admin_chat_dashboard(request):
    active_users = User.objects.filter(chat_messages__isnull=False).distinct()
    return render(request, "admin/chat/admin_chat_dashboard.html", {"active_users": active_users})

from django.db.models import Count, Q

@never_cache
@require_GET
def get_admin_unread_counts(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return JsonResponse({"status": "unauthorized"}, status=401)

    # Get active users and their latest message info
    users = User.objects.filter(chat_messages__isnull=False).distinct()
    user_data = []

    for u in users:
        # Get count of messages sent by customer (not admin)
        latest_msg = ChatMessage.objects.filter(user=u).order_by("-timestamp").first()
        customer_msg_count = ChatMessage.objects.filter(user=u, is_admin=False).count()

        user_data.append({
            "id": u.id,
            "username": u.username,
            "latest_message": latest_msg.message if latest_msg else "",
            "latest_timestamp": latest_msg.timestamp.strftime("%I:%M %p") if latest_msg else "",
            "total_messages": customer_msg_count,
        })

    response = JsonResponse({"users": user_data})
    response["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response