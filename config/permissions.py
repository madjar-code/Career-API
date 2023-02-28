from rest_framework import permissions

SECRET_CODE = '1234'


class IsCodeOwner(permissions.BasePermission):
	"""
	Custom permission to grant access
    to those who have the code.
	"""

	def has_object_permission(self, request, view, obj):
		print(request)
		if 'HTTP_CODE' in request.META:
			if request.META['HTTP_CODE'] == SECRET_CODE:
				return False
		return True
