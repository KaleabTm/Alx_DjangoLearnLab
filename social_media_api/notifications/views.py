from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all().order_by('-timestamp')
        unread_notifications = notifications.filter(read=False)

        data = {
            "unread_count": unread_notifications.count(),
            "notifications": [
                {
                    "id": n.id,
                    "actor": n.actor.username,
                    "verb": n.verb,
                    "target": str(n.target),
                    "timestamp": n.timestamp,
                    "read": n.read,
                } for n in notifications
            ]
        }

        return Response(data)

    def post(self, request):
        request.user.notifications.update(read=True)
        return Response({"detail": "All notifications marked as read."}, status=status.HTTP_200_OK)
