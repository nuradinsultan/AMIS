class RadiologyImageViewSet(viewsets.ModelViewSet):
    queryset = RadiologyImage.objects.all()
    serializer_class = RadiologyImageSerializer
  
