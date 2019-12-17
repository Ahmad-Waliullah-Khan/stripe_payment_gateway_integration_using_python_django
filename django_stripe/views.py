from django.http import HttpResponse
import stripe


def index(request):

    stripe.api_key = 'sk_test_mm3n8XcnrbkJjhJA9G7sLHg700wgNTrKSd'
    

    stripe.PaymentIntent.create(
      amount=599,
      currency='usd',
      payment_method_types=['card'],
      receipt_email='ahmad@spiderorb.com',
    )
    
    return HttpResponse("Stripe Integration")