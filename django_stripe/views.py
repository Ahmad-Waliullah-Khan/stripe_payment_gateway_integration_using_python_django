from django.http import HttpResponse
import stripe
import json

def index(request):
    
    client_secrect_key = 'sk_test_mm3n8XcnrbkJjhJA9G7sLHg700wgNTrKSd'
    stripe.api_key = client_secrect_key
    dummy_card = "4242424242424242"
    
    product_id = 'outpost_test'
    plan_one_id = 'basic'
    plan_two_id = 'executive'
    
    # Create a product 
    outpost_product = stripe.Product.create(
      name="OUTPOST TEST",
      type="service",
      id="outpost_test"
    )
      
    print("PRODUCT CREATED...")
    print(outpost_product)
      
    # create a basic plan under outpost product
    basic_plan = stripe.Plan.create(
      currency='usd',
      interval='month',
      product=outpost_product.id,
      nickname='Basic Plan',
      id='basic',
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
      id='executive',
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
     
    address = {
        "line1": "TDI, Chandigarh",
        "country": "India",
    } 
    
    # create a customer
    customer = stripe.Customer.create(
      description="Test Customer through python",
      email="jonsnow@crows.com",
      name="Jon Snow",
      address=address,
      payment_method=payment_method_response.id,
    )
    
    print("CUSTOMER CREATED...") 
    print(customer)
    
    
    # make the payment method default one
#     default_payment_method = stripe.Customer.modify(
#       customer.id,
#       default_source = payment_method_response.id,
#     )
     
#     print("CREATED DEFAULT PAYMENT METHOD...")
#     print(default_payment_method)
    
    
    # get product and plan
    product = stripe.Product.retrieve(product_id)
    plan = stripe.Plan.retrieve(plan_one_id)
    
    print("PLAN RETRIEVED...") 
    print(plan)
    
    
    # get customer payment method
    customer_payment_method = stripe.PaymentMethod.list(
      customer=customer.id,
      type="card",
    )
    
    print("CUSTOMER PAYMENT METHOD RETRIEVED...") 
    print(customer_payment_method)
    
    
    
    # subscribe to outpost basic plan (recurring)
    subscription = stripe.Subscription.create(
      customer=customer.id,
      default_payment_method=payment_method_response.id, 
      items=[{"plan": plan_one_id}],
    )
    
    print("SUBSCRIPTION CREATED...")  
    print(subscription)
    
            
    return HttpResponse("Stripe payment subscription...")