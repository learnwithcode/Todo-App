from rest_framework import serializers
from .models import Todo



class RepresentationMixin(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        for key in result:
            if result[key] == None:
                result[key] = 'N/A'
        return result


class TodoSerializer(RepresentationMixin):

	class Meta:
		model = Todo
		fields = ['user', 'task']


