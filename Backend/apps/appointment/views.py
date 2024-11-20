from django.core.mail import send_mail

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    def create(self, request, *args, **kwargs):
        send_mail(
            'Appointment Scheduled',
            'Your appointment has been scheduled.',
            'from@example.com',
            [request.user.email],
            fail_silently=False,
        )
        return super().create(request, *args, **kwargs)
