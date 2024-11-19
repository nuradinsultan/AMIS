class RadiologyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyImage
        fields = ['patient', 'image', 'description', 'date_of_scan']
      
