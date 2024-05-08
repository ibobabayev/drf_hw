from rest_framework import serializers
from materials.models import Course,Subject,Subscription
from materials.validators import LinkValidator

class SubjectSerializer(serializers.ModelSerializer):
    validators = [LinkValidator(field='link')]
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    subject_count = serializers.SerializerMethodField()
    subject = SubjectSerializer(source='subject_set',many=True)
    subscription = serializers.SerializerMethodField()
    def get_subject_count(self,obj):
        return obj.subject_set.count()

    def get_subscription(self,obj):
        if Subscription.objects.filter(course=obj.id, user= self.request.user):
            return Subscription.objects.filter(course=obj.id, user=self.request.user)
        else:
            return "Нету информации о подписке"
    class Meta:
        model = Course
        fields = ('name','description','preview','owner','subscription','subject','subject_count',)


class SubscriptionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Subscription
            fields = '__all__'

