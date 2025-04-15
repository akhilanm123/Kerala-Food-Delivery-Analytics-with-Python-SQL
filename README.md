# Full-Stack Data Analytics Project: Food Delivery Trends in Kerala

This project simulates and analyzes food delivery trends in Kerala, India, by generating realistic datasets, designing a relational database, and building an interactive Power BI dashboard for insights. It demonstrates skills in Python, PostgreSQL, and Power BI and showcases how they integrate to solve real-world data analytics problems.

## 🚀 **Tech Stack**

- **Python**: For data simulation and CSV generation using Pandas, Faker, random, numpy, and datetime.
- **PostgreSQL**: For creating and querying a relational database to store simulated data.
- **Power BI**: For designing interactive dashboards to visualize business insights.
- **SQL**: For generating business insights using joins, aggregations, and date functions.
- **Git & GitHub**: For version control and project documentation.
- **DAX**: For creating calculated measures, KPIs, and business logic in Power BI.

---

## 🛠️ **Project Sections**

This project is split into three main sections:

---

### 1. **Python: Data Simulation**

**Objective**: To generate realistic data representing customers, restaurants, orders, menu items, payments, reviews, and deliveries. This simulated data mimics the structure and dynamics of a food delivery business in Kerala.

#### **Tools Used**:
- **Pandas**: Used for manipulating and structuring the generated data.
- **Faker**: Used to generate realistic fake data such as customer names, addresses, restaurants, and more.
- **random & numpy**: Used to simulate random and probabilistic data like order statuses and payment amounts.
- **datetime**: Used to generate random dates for orders, reviews, and deliveries.

#### **Key Features**:
- **Interlinked Tables**: 
  - Generated 8 CSV files representing key entities: 
    - `customers.csv`, `restaurants.csv`, `menu_items.csv`, `orders.csv`, `order_items.csv`, `reviews.csv`, `payments.csv`, and `delivery.csv`.
- **Randomized Data**: Data for customers, restaurants, and orders is randomized to reflect real-world variation (e.g., random order amounts, status updates, customer reviews).
- **Probabilistic Behaviors**: 
  - Generated customer reviews based on certain probabilities (e.g., a higher chance for customers to leave 5-star reviews).
  - Randomly assigned order statuses (e.g., "Delivered", "Pending", "Cancelled").

#### **Output**:
- **CSV Files**: The Python script generates CSV files containing the simulated data, which can be used for further analysis in PostgreSQL and Power BI.

#### **Challenges**:
- Ensuring that the data generated is realistic and maintains relationships across tables (e.g., linking customers to orders, restaurants to menu items).
- Generating data for larger datasets without introducing biases or anomalies that would affect analysis.


### 📜 View the Full Python Code:
👉 [generate_data.py](https://github.com/akhilanm123/food-delivery-simulation/blob/main/generate_data.py)



### 2. 🛢️ PostgreSQL: Database Design & Querying

**Objective**  
To design a **relational database schema** for the simulated food delivery business and perform **SQL queries** to extract meaningful insights.

---

#### 🛠️ Tools Used
- **PostgreSQL** – For relational database creation, data import, and querying  
- **pgAdmin** *(optional)* – For visual schema management and running SQL queries  
- **SQL** – For joins, filtering, aggregations, subqueries, and window functions  

---

#### 🧱 Database Schema Design
- Imported the 8 simulated CSVs into PostgreSQL as tables:  
  `customers`, `restaurants`, `menu_items`, `orders`, `order_items`, `reviews`, `payments`, and `delivery`
- Established relationships using **primary and foreign keys**
- Ensured **data integrity** with appropriate data types and constraints

---

#### 🧠 Key Features
- **Normalized Schema** – Eliminated redundancy by separating entities into related tables  
- **Efficient Joins** – Enabled analysis by joining across customers, orders, payments, and reviews  
- **Custom Views & Indexes** – Created reusable views for KPIs and added indexes to improve performance  

---

#### 📊 Sample Insights Extracted
- Top 10 restaurants by number of orders  
- Most popular dishes by district  
- Customer with the highest number of 5-star reviews  
- Month-wise revenue trend and average order value  
- Payment method analysis (e.g., failure rates, usage trends)  
- City-wise customer count and average order frequency  

---

#### 📤 Output
- A fully functional **PostgreSQL database** ready for advanced analytics and BI reporting  
- Clean, optimized **SQL queries** for insight generation and Power BI integration  

---

#### 📁 SQL Queries (Word Document)  
👉 [View SQL Queries](https://github.com/akhilanm123/Kerala-Food-Delivery-Analytics-with-Python-SQL/blob/main/SQL%20Queries.docx)



---

## 📊 3. Power BI: Dashboard Design

- **Page 1: Overview**
  - KPIs (Total Orders, Revenue, Cancellations, AOV)
  - Slicers by City, Category, Month
  - Key visuals in clean card layout

- **Page 2: Restaurant Sales & Performance**
  - Top restaurants by orders & revenue
  - Most popular dishes by district
  - Monthly revenue trends
  - Best-rated and most cancelled restaurants

- **Page 3: Customer Behavior & Loyalty**
  - Top loyal and high-spending customers
  - City and gender breakdowns
  - 5-star reviewers and their favorite restaurants

- **Page 4: Payments & Revenue Insights**
  - Revenue by payment method
  - Payment failures, inconsistencies
  - YoY trends and monthly comparison

📸 _Screenshots or .gif preview of dashboards go here!_

---

## 🔍 Key Insights

- Over **20,000 orders** simulated with delivery, payment, and feedback flow  
- Identified **top 10 restaurants** and **most loved dishes per region**  
- Revealed **5-star loyalty patterns** and **payment issues**  
- Created a **visually intuitive dashboard** with slicers and filters

---

## 📂 How to Use

1. Clone the repo
2. Import `data/*.csv` into PostgreSQL using provided schema
3. Open the Power BI `.pbix` file and connect to PostgreSQL
4. Refresh the visuals and explore

---

## 👨‍💻 Author

- [Your Name] – Aspiring Data Analyst  
- 🌐 [Portfolio](https://your-portfolio-link.com)  
- 🔗 [LinkedIn](https://linkedin.com/in/yourprofile)

---

## ⭐️ If you found this project interesting, feel free to star it!
