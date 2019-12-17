from django.http import HttpResponse
import stripe


def index(request):

    stripe.api_key = 'sk_test_mm3n8XcnrbkJjhJA9G7sLHg700wgNTrKSd'
    

    response = stripe.PaymentIntent.create(
      amount=699,
      currency='usd',
      payment_method_types=['card'],
      receipt_email='ahmad@spiderorb.com',
    )
    
    print(response)
    
    data = "amount : {}, payment_method' : {}".format(response.amount, response.payment_method_types[0])
        
    return HttpResponse(data)