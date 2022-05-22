from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title= 'Home - Best Deals, Best Bargains'
    return render_template('index.html', title=title)


@app.route('product')
def product(product_id):
    
    
    
    return render_template('product.html')