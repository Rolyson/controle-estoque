from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField, CharField
from request.models import Request,ProductRequest, MovementProduct

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

    itens = SerializerMethodField()

    def get_itens(self, instance):
        return [ ProductRequestSerializer(item).data for item in instance.productrequest_set.all()]

class ProductRequestSerializer(ModelSerializer):
    class Meta:
        model = ProductRequest
        fields = '__all__'

    def validate(self, attrs):      
        errors = {}

        # pending_quantity = attrs.get('quantity',0) - attrs.get('quantity_served',0)
        
        # if float(attrs.get('quantity_calculated',0)) > pending_quantity:
        #     errors["quantity"] = "A quantidade apurada é maior que a quantidade em aberto"

        if len(errors.keys()) > 0:
            raise ValidationError(errors)

        return super().validate(attrs)

class MovementProductSerializer(ModelSerializer):
    class Meta:
        model = MovementProduct
        fields = '__all__'