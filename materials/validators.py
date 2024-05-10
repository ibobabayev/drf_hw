from rest_framework.serializers import ValidationError

class LinkValidator:
    def __init__(self,field):
        self.field = field

    def __call__(self, link):
        youtube = 'https://youtube.com/'

        if link:
            if youtube not in link:
                raise ValidationError('You should use youtube link')
        else:
            return None
