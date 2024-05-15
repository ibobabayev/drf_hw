import stripe
from config import settings
stripe.api_key = settings.STRIPE_API
# def create_stripe(payment):
#     stripe_product = stripe.Product.create(name=payment.course_paid)
#     stripe_price = stripe.Price.create(
#         currency="rub",
#         unit_amount=int(payment.payment_amount) * 100,
#         recurring={"interval": "month"},
#         product_data={"name": stripe_product.id},
#     )
#     stripe_session = stripe.checkout.Session.create(
#         success_url="http://http://127.0.0.1:8000/",
#         line_items=[{"price": stripe_price.id, "quantity": 1}],
#         mode="payment",
#     )
#     return stripe_session

def create_product(product):
    stripe_product = stripe.Product.create(name=product.course_paid)
    return stripe_product

def create_price(price):
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=int(price.payment_amount) * 100,
        recurring={"interval": "month"},
        product_data={"name": price.id},
    )
    return stripe_price

def create_session(session):
    stripe_session = stripe.checkout.Session.create(
        success_url="http://http://127.0.0.1:8000/",
        line_items=[{"price": session.id, "quantity": 1}],
        mode="payment",
    )
    return stripe_session