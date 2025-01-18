from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/item_input')
def item_input():
    return "Item Input"

if __name__ == '__main__':
    app.run(debug=True)