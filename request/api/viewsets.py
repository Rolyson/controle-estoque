from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from request.api.serializers import RequestSerializer, ProductRequestSerializer, MovementProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from request.models import ProductRequest, Request, MovementProduct

class RequestViewSet(ModelViewSet):
    serializer_class       = RequestSerializer
    search_fields          = ["id"]
    filter_backends        = (SearchFilter, OrderingFilter)
    ordering               = ('id')

    def get_queryset(self):
        return Request.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        for item in request.data.get('itens',[]):
            item['request'] = serializer.instance.id
            item_serializer = ProductRequestSerializer(data=item)
            item_serializer.is_valid(raise_exception=True)
            item_serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(methods=["POST"], detail=False)
    def respond_request(self, request):  
        try:
            id_request = request.data.get('id',None)

            request_moviment =  Request.objects.filter(id=id_request).first()

            if not request_moviment:
                raise Exception('Não foi possivel localizar a requisição.')
            
            if request_moviment.status in [2,4,5]:
                raise Exception('Não foi possivel atender uma requisição já finalizada.')
            
            for item in request.data.get('itens',[]):
                if item.get('quantity_calculated', None):
                    product = ProductRequest.objects.filter(id=item.get('id',None)).first()
                    product.quantity_served += item.get('quantity_calculated', 0)
                    # item_serializer = ProductRequestSerializer(data=item)
                    # item_serializer.is_valid(raise_exception=True)

                    
        except KeyError as k_err:
            teste = 1
        except TypeError as typeError:
            teste = 2
        except Exception as error:
            return Response(data={"message": error.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
        

    
class MovementProductViewSet(ModelViewSet):
    serializer_class       = MovementProductSerializer
    search_fields          = ["id"]
    filter_backends        = (SearchFilter, OrderingFilter)
    ordering               = ('id')

    def get_queryset(self):
        return MovementProduct.objects.all()