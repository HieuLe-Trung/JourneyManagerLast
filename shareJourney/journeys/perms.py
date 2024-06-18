from rest_framework import permissions


class OwnerJourneyAuthenticated(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request,
                                   view) and request.user == obj.user_create


class OwnerPostAuthenticated(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request,
                                   view) and request.user == obj.user
