import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta


fake = Faker('en_IN')

kerala_name_gender = [
    ("Aswin Kumar", "Male"), ("Arya S Nair", "Female"), ("Neeraj Menon", "Male"), ("Devika Mohan", "Female"), ("Siddharth S", "Male"),
    ("Anagha Raj", "Female"), ("Jithin Joseph", "Male"), ("Krishna Lekshmi", "Female"), ("Adarsh Pillai", "Male"), ("Sneha Nandan", "Female"),
    ("Reshma K", "Female"), ("Vishak R", "Male"), ("Rakhi Menon", "Female"), ("Anoop S", "Male"), ("Gopika Sunil", "Female"),
    ("Rahul Dev", "Male"), ("Keerthana M", "Female"), ("Abhinav Ramesh", "Male"), ("Meghna Das", "Female"), ("Ramesh Krishnan", "Male"),
    ("Soumya Menon", "Female"), ("Nikhil S", "Male"), ("Saranya P", "Female"), ("Deepa R", "Female"), ("Rohit Nair", "Male"),
    ("Sreelakshmi K", "Female"), ("Faisal Rahman", "Male"), ("Saniya Ameer", "Female"), ("Rinu Paul", "Female"), ("Merin Mathew", "Female"),
    ("Sreenath B", "Male"), ("Anu Mol", "Female"), ("Aravind Raj", "Male"), ("Shafna N", "Female"), ("Sujith Kumar", "Male"),
    ("Liji Jose", "Female"), ("Tintu Thomas", "Female"), ("Rahul John", "Male"), ("Rinu Sebastian", "Female"), ("Athulya S", "Female"),
    ("Nived R", "Male"), ("Sibin George", "Male"), ("Joyal Mathew", "Male"), ("Neethu Varghese", "Female"), ("Ajmal Hussain", "Male"),
    ("Ameena Salim", "Female"), ("Feba Elsa", "Female"), ("Devu Reji", "Female"), ("Jishnu R", "Male"), ("Sreevidya V", "Female")
]

kerala_cities = [
    'Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Thrissur', 'Kannur',
    'Kollam', 'Alappuzha', 'Kottayam', 'Palakkad', 'Malappuram',
    'Pathanamthitta', 'Wayanad', 'Idukki', 'Kasargod'
]

def generate_customers(num_customers=500):
    customers = []
    used_name_city_pairs = set()

    for i in range(1, num_customers + 1):
        while True:
            name, gender = random.choice(kerala_name_gender)
            city = random.choice(kerala_cities)
            if (name, city) not in used_name_city_pairs:
                used_name_city_pairs.add((name, city))
                break

        age = random.randint(18, 65)
        email = fake.email()
        phone = str(random.randint(7000000000, 9999999999))  # Ensures exactly 10 digits
        join_date = fake.date_between(start_date='-3y', end_date='today')

        customers.append({
            'customer_id': i,
            'name': name,
            'gender': gender,
            'age': age,
            'city': city,
            'email': email,
            'phone': phone,
            'join_date': join_date
        })

    return pd.DataFrame(customers)

# Generate and save CSV
df_customers = generate_customers()
df_customers.to_csv("customers.csv", index=False)
print("✅ customers.csv generated with valid 10-digit phone numbers!")





# ------------------------------------------
# RESTAURANT DATA GENERATION (Step 1.2)
# ------------------------------------------

df_hotels = pd.read_excel( r"E:\Python\foodpulse project files\Hotel_List_Updated_Final.xlsx"
)

# ✅ Generate synthetic restaurant data from Excel
def generate_restaurants_from_excel(df_hotels):
    restaurants = []

    for i, row in df_hotels.iterrows():
        name = row['Name']
        district = row['District']
        type_ = random.choice(['Veg', 'Non-Veg', 'Mixed'])
        contact = fake.msisdn()[0:10]  # Generates valid 10-digit Indian mobile number
        address = f"{fake.street_address()}, {district}, Kerala"
        opening_year = random.randint(2000, 2023)
        avg_rating = round(random.uniform(3.5, 5.0), 1)

        restaurants.append({
            'restaurant_id': i + 1,
            'restaurant_name': name,
            'district': district,
            'type': type_,
            'contact': contact,
            'address': address,
            'opening_year': opening_year,
            'avg_rating': avg_rating
        })

    return pd.DataFrame(restaurants)

# ✅ Generate and save to CSV
df_restaurants = generate_restaurants_from_excel(df_hotels)
df_restaurants.to_csv("restaurants.csv", index=False)

print("✅ restaurants.csv generated using Excel hotel list!")

#-----------------------------------------------
# MENU ITEMS
#-----------------------------------------------

# Load restaurants (already generated)
df_restaurants = pd.read_csv("restaurants.csv")

# Load food items list
df_food_items = pd.read_excel(r"E:\Python\foodpulse project files\Food_Item List.xlsx")
df_food_items.columns = df_food_items.columns.str.strip()

# Define price ranges per category
category_price_ranges = {
    'Continental': (250, 450),
    'Pizza': (150, 500),
    'Salads': (90, 280),
    'Desserts': (50, 240),
    'Traditional': (40, 300)
}

def generate_menu_items(df_restaurants, df_food_items, min_items=5, max_items=10):
    menu = []
    menu_item_id = 1

    for _, rest in df_restaurants.iterrows():
        num_items = random.randint(min_items, max_items)
        sampled_items = df_food_items.sample(n=num_items)

        for _, item in sampled_items.iterrows():
            category = item['Category']
            min_price, max_price = category_price_ranges.get(category, (100, 300))  # Default if unknown category
            price = round(random.uniform(min_price, max_price), 2)

            menu.append({
                'menu_item_id': menu_item_id,
                'restaurant_id': rest['restaurant_id'],
                'dish_name': item['Item_Name'],
                'category': category,
                'price': price,
                'available': random.choice(['Yes', 'No'])
            })
            menu_item_id += 1

    return pd.DataFrame(menu)

# ✅ Generate menu items
df_menu_items = generate_menu_items(df_restaurants, df_food_items)

# ✅ Save to CSV
df_menu_items.to_csv("menu_items.csv", index=False)
print("✅ menu_items.csv generated!")

# ------------------------------------------
# ORDER DATA GENERATION (Step 1.3)
# ------------------------------------------

def generate_orders(df_customers, df_restaurants, num_orders=20000, starting_order_id=1):
    orders = []
    status_choices = ['Delivered'] * 6 + ['Cancelled'] * 2 + ['Pending'] * 2  # 60% Delivered

    for i in range(num_orders):
        order_id = starting_order_id + i
        customer = df_customers.sample(1).iloc[0]
        restaurant = df_restaurants.sample(1).iloc[0]
        order_time = datetime.now() - timedelta(days=random.randint(1, 90), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        status = random.choice(status_choices)
        total_amount = round(random.uniform(150, 800), 2)

        orders.append({
            'order_id': order_id,
            'customer_id': customer['customer_id'],
            'restaurant_id': restaurant['restaurant_id'],
            'order_datetime': order_time.strftime("%Y-%m-%d %H:%M:%S"),
            'order_status': status,
            'total_amount': total_amount
        })

    return pd.DataFrame(orders)

# ✅ Generate and save
df_orders = generate_orders(df_customers, df_restaurants)
df_orders.to_csv("orders.csv", index=False)
print("✅ orders.csv generated")


#-------------------------------------------------------
# ORDER ITEMS
#-------------------------------------------------------

def generate_order_items(df_orders, df_menu_items, min_items=1, max_items=4):
    order_items = []
    order_item_id = 1

    for _, order in df_orders.iterrows():
        num_items = random.randint(min_items, max_items)
        selected_items = df_menu_items.sample(n=num_items)

        for _, item in selected_items.iterrows():
            quantity = random.randint(1, 10)
            item_price = item['price']
            total_price = round(quantity * item_price, 2)

            order_items.append({
                'order_item_id': order_item_id,
                'order_id': order['order_id'],
                'menu_item_id': item['menu_item_id'],
                'quantity': quantity,
                'item_price': item_price,
                'total_price': total_price
            })

            order_item_id += 1

    return pd.DataFrame(order_items)

# ✅ Generate order items
df_order_items = generate_order_items(df_orders, df_menu_items)

# ✅ Save to CSV
df_order_items.to_csv("order_items.csv", index=False)
print("✅ order_items.csv generated!")

# ------------------------------------------
# REVIEWS DATA GENERATION (Step 1.4)
# ------------------------------------------

review_texts = [
    "Amazing food!", "Tasty and fresh.", "Good portion size.",
    "Could be better.", "Not satisfied.", "Will order again.",
    "Loved the packaging!", "Too spicy for me.", "Fast delivery!", "Average taste."
]

def generate_reviews(df_orders):
    reviews = []
    review_id = 1

    for _, order in df_orders.iterrows():
        if order['order_status'] != 'Delivered':
            continue

        rating = random.choices([5, 4, 3, 2, 1], weights=[40, 30, 15, 10, 5])[0]
        review = random.choice(review_texts)
        review_time = datetime.strptime(order['order_datetime'], "%Y-%m-%d %H:%M:%S") + timedelta(minutes=random.randint(30, 1440))

        reviews.append({
            'review_id': review_id,
            'order_id': order['order_id'],
            'customer_id': order['customer_id'],
            'restaurant_id': order['restaurant_id'],
            'rating': rating,
            'review_text': review,
            'review_time': review_time.strftime("%Y-%m-%d %H:%M:%S")
        })

        review_id += 1

    return pd.DataFrame(reviews)
df_reviews = generate_reviews(df_orders)
df_reviews.to_csv("reviews.csv", index=False)
print("✅ reviews.csv generated!")


#------------------------------------------
# PAYMENTS
#------------------------------------------

def generate_payments(df_orders):
    payment_methods = ['UPI', 'Card', 'Cash']
    payment_statuses = ['Paid', 'Failed', 'Refunded']

    payments = []
    payment_id = 1

    for _, order in df_orders.iterrows():
        # FIX: order['order_datetime'] instead of 'order_time'
        order_time = pd.to_datetime(order['order_datetime'])
        method = random.choice(payment_methods)
        status = random.choices(payment_statuses, weights=[0.85, 0.10, 0.05])[0]
        amount = order['total_amount']
        payment_time = order_time + timedelta(minutes=random.randint(1, 30))

        payments.append({
            'payment_id': payment_id,
            'order_id': order['order_id'],
            'payment_method': method,
            'payment_status': status,
            'amount_paid': amount if status == 'Paid' else 0.0,
            'payment_time': payment_time.strftime("%Y-%m-%d %H:%M:%S")
        })
        payment_id += 1

    return pd.DataFrame(payments)
df_payments = generate_payments(df_orders)
df_payments.to_csv("payments.csv", index=False)
print("✅ payments.csv generated!")





#------------------------------------------
# DELIVERY DATA GENERATION (Step 1.5)
# ------------------------------------------

delivery_partners = ["Anas", "Rahul", "Jithin", "Nandhu", "Aju", "Firoz", "Sreejith", "Ajmal", "Akhil"]

def generate_delivery_data():
    delivery_data = []
    for index, row in df_orders.iterrows():
        estimated_time = random.randint(20, 50)  # in minutes
        actual_time = estimated_time + random.randint(-10, 20)  # may be faster/slower
        delay = actual_time - estimated_time
        status = "Delivered"
        if delay > 15:
            status = "Delayed"
        if random.random() < 0.05:  # 5% cancelled
            status = "Cancelled"
            actual_time = None

        delivery_data.append({
            'delivery_id': index + 1,
            'order_id': row['order_id'],
            'restaurant_id': row['restaurant_id'],
            'customer_id': row['customer_id'],
            'delivery_partner': random.choice(delivery_partners),
            'estimated_delivery_time': estimated_time,
            'actual_delivery_time': actual_time,
            'status': status
        })
    return pd.DataFrame(delivery_data)

# Generate and save CSV
df_delivery = generate_delivery_data()
df_delivery.to_csv("delivery.csv", index=False)
print("✅ delivery.csv generated!")


