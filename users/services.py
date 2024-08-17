import stripe
from config.settings import STRIPE_APY_KEY

stripe.api_key = STRIPE_APY_KEY


def create_stripe_product(payment):
    tmp_product = payment.course if payment.course else payment.lesson
    product = stripe.Product.create(name=tmp_product.title)
    return product.id


def create_stripe_price(product_id, payment):
    price = stripe.Price.create(
        product=product_id,
        currency="rub",
        unit_amount=int(payment.payment_amount * 100),
    )
    return price.id


def create_stripe_session(price_id):
    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url
