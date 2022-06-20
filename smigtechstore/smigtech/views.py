from flask import Blueprint, redirect, render_template, request, url_for
import stripe 


views = Blueprint('views', __name__)

# Stripe test API key from docs 
stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'


@views.route('/')
def store_home():
    """Returns basic store home page"""

    return render_template('index.html')


@views.route('/book', methods=['POST'])
def book_session():
    """uses stripe to create checkout session"""

    try: 
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    "price": 20,
                    'quantity': 1,
                },
            ],
            mode = 'payment',
            success_url = url_for('views.success'),
            cancel_url = url_for('views.cancel'),
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


@views.route('/checkout')
def success():
    """Method for checking out """

    return render_template('success.html')


@views.route('/cancel')
def cancel():
    """Cancel the order"""

    return render_template('cancel.html')