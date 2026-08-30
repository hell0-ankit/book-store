from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Count, Max
from .models import ChatMessage

User = get_user_model()


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    # Bypass the standard changelist table and render a custom live dashboard instead
    def changelist_view(self, request, extra_context=None):
        # Enforce the same permission check the default changelist_view would have done.
        # Since we fully override changelist_view, this check is not automatic and must
        # be added explicitly, otherwise any staff user could view this page regardless
        # of whether they have view permission on ChatMessage.
        if not self.has_view_permission(request):
            raise PermissionDenied

        # Get all users who have sent at least one message, annotated with:
        # - message_count: total messages sent (useful for a dashboard summary)
        # - last_message_at: timestamp of their most recent message (for sorting)
        # This replaces a separate query per user with a single annotated query.
        active_users = (
            User.objects.filter(chat_messages__isnull=False)
            .annotate(
                message_count=Count("chat_messages"),
                last_message_at=Max("chat_messages__timestamp"),
            )
            .distinct()
            .order_by("-last_message_at")
        )

        context = {
            **self.admin_site.each_context(request),
            "title": "Live Customer Support Desk",
            "active_users": active_users,
            "opts": self.model._meta,
        }
        return render(request, "admin/chat/admin_chat_dashboard.html", context)