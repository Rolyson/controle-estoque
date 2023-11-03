from request.api.serializers import MovementProductSerializer


def move_stock(request_moviment, item, type_movement):
    sector = request_moviment.sector_in
    if type_movement == 2:
        sector = request_moviment.sector_out


    moviment ={
        "request"       : request_moviment.id,
        "product"       : item['id'],
        "sector"        : sector.id,
        "type_movement" : type_movement,
        "quantity"      : item['quantity_calculated'],
    }
    moviment_serializer = MovementProductSerializer(data=moviment)
    moviment_serializer.is_valid(raise_exception=True)
    moviment_serializer.save()
    
  