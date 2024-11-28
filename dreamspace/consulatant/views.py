from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ConsultationRequestForm
# from .models import Consulatant
# Create your views here.


def book_consultation(request):
    if request.method == "POST":
        form = ConsultationRequestForm(request.POST)
        if form.is_valid():
            consultation = form.save()
            
            # Send email to the backend team
            send_mail(
                subject="New Consultation Request",
                message=f"Name: {consultation.name}\n"
                        f"Email: {consultation.email}\n"
                        f"Contact Number: {consultation.contact_number}\n"
                        f"Date: {consultation.date}\n"
                        f"Time Slot: {consultation.time_slot}",
                from_email="aishwarya.solkar55@gmail.com",
                recipient_list=["artilachure@gmail.com"],
                fail_silently=False,
            )
            messages.success(request, "Your consultation has been booked!")
            return redirect('book_consultation')
    else:
        form = ConsultationRequestForm()
    
    return render(request, 'book_consultation.html', {'form': form})