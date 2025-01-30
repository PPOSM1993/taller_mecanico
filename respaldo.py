"""
    def get_permissions(self):
        self.permission_classes = [AllowAny]

        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]

        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
        return Response(serializer.data)
"""



"""
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.order_by('pk')
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]

    pagination_class = PageNumberPagination
    pagination_class.page_size = 9
    pagination_class.page_query_param = 'pagenum'
    pagination_class.page_size_query_param ='size'
    pagination_class.max_page_size = 10

    def get_permissions(self):
        self.permission_classes = [AllowAny]

        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]

        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


    @action(detail=False, methods=['GET'], permission_classes = [AllowAny])
    def list_brands(self, request):
        list_brands = Brand.objects.all()

        serializer = self.get_serializer(list_brands, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST', 'DELETE', 'PUT', 'PATCH'], url_path='create_brand', permission_classes = [IsAuthenticated])
    def create_brand(self, request, *args, **kwargs):
        return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.order_by('pk')
    serializer_class = CarSerializer
    permission_classes = [AllowAny]

    pagination_class = PageNumberPagination
    pagination_class.page_size = 9
    pagination_class.page_query_param = 'pagenum'
    pagination_class.page_size_query_param ='size'
    pagination_class.max_page_size = 10

    def get_permissions(self):
        self.permission_classes = [AllowAny]

        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]

        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


    @action(detail=False, methods=['GET'], permission_classes = [AllowAny])
    def list_car(self, request):
        list_car = Car.objects.all()

        serializer = self.get_serializer(list_car, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST', 'DELETE', 'PUT', 'PATCH'], url_path='create_car', permission_classes = [IsAuthenticated])
    def create_car(self, request, *args, **kwargs):
        return Response(serializer.data)
"""