#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv_file():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql_file():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json_file()
        elif source == 'csv':
            data = read_csv_file()
        elif source == 'sql':
            data = read_sql_file()
        else:
            return render_template('product_display.html', error='Wrong source')
    except Exception:
        return render_template('product_display.html', error='Database error')

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error='Product not found')

        filtered_products = []
        for product in data:
            if product['id'] == product_id:
                filtered_products.append(product)

        if not filtered_products:
            return render_template('product_display.html', error='Product not found')

        data = filtered_products

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)