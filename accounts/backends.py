from .models import User, Artist
from django.db.models import Q

class EmailBackend:
    def authenticate(self, request, user_type, username=None, password=None):
        try:
            if user_type:
                user = Artist.objects.get(Q(email=username) | Q(username=username))
                if user.check_password(password):
                    return user
            else:
                user = User.objects.get(Q(email=username) | Q(username=username))
                if user.check_password(password):
                    return user
        except:
            return None

    def get_user(self, user_id):
        try:
            if Artist.objects.filter(pk=user_id).exists():
                return Artist.objects.get(pk=user_id)
            else:
                return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
            