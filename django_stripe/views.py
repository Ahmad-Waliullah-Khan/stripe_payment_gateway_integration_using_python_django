from django.http import HttpResponse
import stripe
import json

def index(request):
    
    client_secrect_key = 'sk_test_mm3n8XcnrbkJjhJA9G7sLHg700wgNTrKSd'
    stripe.api_key = client_secrect_key
    dummy_card = "4242424242424242"
    
    outpost_monthly_basic_plan = "plan_GNNxTEfOmkHe19"
    
    # Create a product 
    outpost_product = stripe.Product.create(
      name="OUTPOST Subscription",
      type="service",
    )
    
    print(outpost_product.id)
    
    # create a basic plan under outpost product
    basic_plan = stripe.Plan.create(
      currency='usd',
      interval='month',
      product=outpost_product.id,
      nickname='Basic Plan',
      amount=799,
    )
     
    print(basic_plan)
    
    # create an executive plan under outpost product 
    executive_plan = stripe.Plan.create(
      currency='usd',
      interval='month',
      product=outpost_product["id"],
      nickname='Executive Plan',
      amount=1199,
    )
     
    print(executive_plan)
          
    return HttpResponse("Stripe api ...")