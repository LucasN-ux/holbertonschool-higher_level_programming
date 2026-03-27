from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    return render_template('items.html', items=data.get('items', []))


def read_json_file(filename):
    """Read products from a JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception:
        return []


def read_csv_file(filename):
    """Read products from a CSV file"""
    products = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        return []

    return products


@app.route('/products')
def products():
    """Display products from JSON or CSV with optional id filter"""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        data = read_json_file('products.json')
        if isinstance(data, dict):
            data = data.get('products', [])
    else:
        data = read_csv_file('products.csv')
        if isinstance(data, dict):
            data = data.get('products', [])

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Product not found")

        filtered = [p for p in data if p['id'] == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found")
        data = filtered

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
