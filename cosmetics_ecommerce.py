from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# 1. Custom Database for your unique cosmetics inventory
cosmetics_inventory = [
    {"id": 1, "name": "Radiant Foundation", "price": 14.99, "desc": "Glossy hydration with organic aloevera extract."},
    {"id": 2, "name": "Velvet Matte Blush Blush", "price": 18.50, "desc": "Lightweight, blendable cheek tint."},
    {"id": 3, "name": "Vitamin C Glow Serum", "price": 24.00, "desc": "Brightening base formula for daily use."}
]

# Simple in-memory shopping cart list
shopping_cart = []

# 2. Combined Frontend Web Layout (HTML/CSS)
HTML_LAYOUT = """
<!DOCTYPE html>
<html>
<head>
    <title>Aura Cosmetics</title>
    <style>
        body { font-family: sans-serif; margin: 20px; background-color: #fff5f5; color: #333; }
        .header { text-align: center; padding: 20px; background-color: #ffd6d6; border-radius: 8px; }
        .product-card { background: white; padding: 15px; margin: 15px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .btn { background-color: #ff85a2; color: white; border: none; padding: 8px 12px; border-radius: 4px; cursor: pointer; }
        .cart-box { background: #ffe3e3; padding: 15px; border-radius: 8px; margin-top: 30px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>✨ Glow & Co. Premium Cosmetics ✨</h1>
        <p>Your portal submission storefront project.</p>
    </div>

    <h2>Our Product Catalog</h2>
    {% for item in products %}
    <div class="product-card">
        <h3>{{ item.name }} - ${{ item.price }}</h3>
        <p>{{ item.desc }}</p>
        <form action="/add/{{ item.id }}" method="POST">
            <button type="submit" class="btn">Add to Cart</button>
        </form>
    </div>
    {% endfor %}

    <div class="cart-box">
        <h2>Your Shopping Cart Items</h2>
        {% if cart|length == 0 %}
            <p>Your shopping cart is currently empty.</p>
        {% else %}
            <ul>
            {% for cart_item in cart %}
                <li><strong>{{ cart_item.name }}</strong> - ${{ cart_item.price }}</li>
            {% endfor %}
            </ul>
            <p><strong>Status:</strong> Processing Order Active</p>
        {% endif %}
    </div>
</body>
</html>
"""

# 3. App Routing Paths
@app.route('/')
def home_page():
    return render_template_string(HTML_LAYOUT, products=cosmetics_inventory, cart=shopping_cart)

@app.route('/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    for item in cosmetics_inventory:
        if item['id'] == product_id:
            shopping_cart.append(item)
            break
    return redirect(url_for('home_page'))

if __name__ == '__main__':
    # Run server locally on your mobile device
    app.run(debug=True, port=5000)
