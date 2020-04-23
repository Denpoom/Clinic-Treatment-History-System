from rest_framework import serializers

from User_app.models import Congenital_disease

class Congenital_diseaseSerializerWithoutPatient(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=255)

    def create(self, validate_data):
        return Congenital_disease.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class Congenital_diseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Congenital_disease
        fields = ['id', 'name', 'patient_id']
        read_only_fields = ['id']