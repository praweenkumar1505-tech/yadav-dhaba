from flask import Flask, render_template, request

app = Flask(__name__)

menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

customers = {}

@app.route('/', methods=['GET', 'POST'])
def index():

    message = ""
    customer_name = ""
    orders = []
    total_bill = 0

    if request.method == 'POST':

        customer_name = request.form.get('customer_name')

        items = request.form.getlist('items')

        # Agar customer pehle se exist nahi karta
        if customer_name not in customers:

            customers[customer_name] = {
                "orders": [],
                "bill": 0
            }

        # New items add karo
        for item in items:

            if item in menu:

                customers[customer_name]["orders"].append(item)

                customers[customer_name]["bill"] += menu[item]

                message += f"{item} added successfully!<br>"

        # Data fetch karo
        orders = customers[customer_name]["orders"]

        total_bill = customers[customer_name]["bill"]

    return render_template(
        'index.html',
        menu=menu,
        customer_name=customer_name,
        orders=orders,
        total_bill=total_bill,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True)
