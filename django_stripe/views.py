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
    
    print("PRODUCT CREATED...")
    print(outpost_product)
    
    # create a basic plan under outpost product
    basic_plan = stripe.Plan.create(
      currency='usd',
      interval='month',
      product=outpost_product.id,
      nickname='Basic Plan',
      amount=799,
    )
    
    print("RECURRING PLAN CREATED (BASIC PLAN)...") 
    print(basic_plan)
    
    # create an executive plan under outpost product 
    executive_plan = stripe.Plan.create(
      currency='usd',
      interval='month',
      product=outpost_product["id"],
      nickname='Executive Plan',
      amount=1199,
    )
    
    print("RECURRING PLAN CREATED (EXECUTIVE PLAN)...")  
    print(executive_plan)
    
    # creates a payment method
    payment_method_response = stripe.PaymentMethod.create(
      type="card",
      card={
        "number": dummy_card,
        "exp_month": 12,
        "exp_year": 2020,
        "cvc": "314",
      },
    )
    
    print("PAYMENT METHOD (CARD) CREATED...") 
    print(payment_method_response)
     
    
    # create a customer
    customer = stripe.Customer.create(
      description="Test Customer through python",
      email="jonsnow@crows.com",
      name="Jon Snow",
      address="Chandigarh, India, 781028",
    )
    
    print("CUSTOMER CREATD...") 
    print(customer)
    
     # attach the payment method to the customer 
    attached_payment_method = stripe.PaymentMethod.attach(
      payment_method_response.id,
      customer=customer.id,
    )
    
    print("ATTACHED PAYMENT METHOD...")
    print(attached_payment_method)
    
    # make the payment method default one
    default_payment_method = stripe.Customer.modify(
      customer.id,
      default_source = payment_method_response.id,
    )
    
    print("CREATED DEFAULT PAYMENT METHOD...")
    print(default_payment_method)
    
    # subscribe to outpost basic plan (recurring)
    subscription = stripe.Subscription.create(
      customer=customer.id,
      default_payment_method=payment_method_response.id, 
      items=[{"plan": basic_plan.id}],
    )
    
    print("SUBSCRIPTION CREATED...")  
    print(subscription)
    
            
    return HttpResponse("Stripe payment subscription...")