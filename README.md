# Full-Stack Data Analytics Project:  Delivery Trends in Kerala

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

### 3. **Power BI: Interactive Dashboards & Business Insights**

**Objective**: To transform simulated food delivery data into visually engaging, actionable insights using Power BI dashboards. This allowed stakeholders to monitor KPIs, identify trends, and make strategic decisions.

#### **Tools Used**:
- **Power BI** – For data modeling, visualization, and dashboard design
- **DAX** – To create calculated measures, KPIs, and dynamic aggregations
- **Power Query** – For data transformation and cleaning

#### **Deliverables**:
- **5 Professional Dashboards** analyzing:
  - Restaurant performance
  - Order status and delivery trends
  - Menu item popularity
  - Geographic distribution of revenue
  - Customer behavior & satisfaction

#### 📁 [Download Power BI File – Kerala_Eats_Performance.pbix](https://github.com/akhilanm123/Kerala-Food-Delivery-Analytics-with-Python-SQL/blob/main/Kerala%20Eats-Performance%20Tracker%20Dashboard.pbix)

---

### 🖼️ Dashboard 1: Executive Summary  
> *"A bird’s-eye view of key business metrics across Kerala’s food delivery ecosystem."*

![Executive Summary Dashboard](https://github.com/akhilanm123/Kerala-Food-Delivery-Analytics-with-Python-SQL/blob/main/Executive%20Summary.png)

#### 📊 Key Metrics:
- **Total Orders**: 20,000  
- **Total Customers**: 500  
- **Total Revenue**: ₹8.1M  
- **Average Order Value**: ₹475  
- **Average Delivery Delay**: 2.84  
- **Cancellation Rate**: 4.89%

#### 📉 Monthly Trend Highlights:
- Orders peaked in **Feb 2025 (6,817)**, but dropped **66% by April 2025**
- Revenue declined from ₹2.6M (March) to ₹0.9M (April)

#### 🏆 Top Restaurants:
- **Hotel Green Park** – 32K  
- **Hotel Sea Breeze** – 25K  
- **Mountain View Restaurant** – 24K  

#### 🌍 Top Cities by Revenue:
- **Kollam** – ₹0.64M  
- **Idukki**, **Kannur**, **Pathanamthitta** – ₹0.62M  
- **Wayanad** – ₹0.61M

#### 🍽️ Most Popular Dishes:
- **Baklava** – 1.3K orders  
- **Croque Monsieur** – 1.2K  
- **Neyappam** – 1.1K  
- **Chicken Burger** – 1.0K  

---

#### 📌 Root Cause Analysis: April 2025 Revenue Decline

A significant decline in both revenue and order volume in April 2025 suggests underlying issues worth immediate exploration:

- **Seasonal Shift** – Post-festive demand dip  
- **Delivery Delays** – 14.9% delay rate affecting retention  
- **Competitor Activity** – Market share lost to rivals  
- **Economic Dip** – Reduced customer discretionary spending  
- **Platform/Tech Issues** – Potential app bugs or lower visibility  
- **Marketing Drop-off** – Inactive promotions or reduced ad spend

🧠 *This dashboard is a critical business tool to proactively monitor shifts, detect risks, and support timely interventions.*

### 🖼️ Dashboard 2: Restaurant Performance & Sales  
> *"Analyzing restaurant performance, cancellations, and customer preferences to uncover trends in April 2025 revenue decline."*

![Restaurant Performance & Sales Dashboard](https://github.com/akhilanm123/Kerala-Food-Delivery-Analytics-with-Python-SQL/blob/main/Restaurant%20Performance%20%26%20Sales.png)

#### 📊 Key Insights:

**Restaurant Performance Metrics**:
- **Top Performers**:  
  - **Hotel Green Park** – 86 orders  
  - **Hotel Sea Breeze** – 61 orders  
  - **Hotel Kairali** – 59 orders  
- **High Cancellation Rates**:  
  - **Hotel Beach Park Kozhikode** – 20% cancellation rate  
  - Several other restaurants also have cancellation rates above 14%

**Revenue & Value Insights**:
- **Revenue Decline**: All restaurants showed a **dramatic revenue decline** in **April 2025**, continuing the trend observed in Dashboard 1.
- **Peak Revenue**: March 2025 was the peak revenue month for all tracked restaurants.
- **Highest Average Order Value**:  
  - **Hotel Isaac Residency** – ₹613.25
  - **Lowest**: **Heritage Manor Restaurant** – ₹576.06

**Customer Preferences**:
- **Top-Rated Restaurants**:  
  - **Spice Tree Bistro** and **Hotel Royal Manor Malappuram** – both rated **4.7/5**
  - **Tied**: **Hotel Chrysoberyl**, **Hotel Royal Green Kannur**, **Thevally Palace** – rated **4.6/5**
- **Most Popular Dish**:  
  - **Baklava** – Most ordered across multiple districts  
  - **Pathanamthitta**: 24 orders of Baklava (highest for a single dish)

#### 📉 Key Concerns:
- **Revenue Drop**: The **April 2025 decline** is a **market-wide issue**, affecting all restaurants tracked.
- **High Cancellation Rates**: **Hotel Beach Park Kozhikode** and others show significant operational or service issues.
- **Top Restaurants with Low Ratings**: Some high-order-volume restaurants don’t appear on the **top-rated list**, indicating possible **quality vs. quantity trade-offs**.

🧠 *This dashboard provides a deeper dive into the restaurant performance breakdown, revealing both **strengths** (top-rated places) and **weaknesses** (high cancellation rates). It highlights areas for operational improvement while reinforcing the larger **market-wide revenue decline** in April 2025.*
### 🖼️ Dashboard 3: Customer Insights  
> *"Analyzing customer loyalty, demographic patterns, and preferences to identify key engagement and retention opportunities."*

![Customer Insights Dashboard](https://github.com/akhilanm123/Kerala-Food-Delivery-Analytics-with-Python-SQL/blob/main/Customer%20Insights%20Dashboard.png)

#### 📊 Key Insights:

**Customer Loyalty & Value**:
- **Top Customers**:  
  - **Abhinav Ramesh** – 560 orders, ₹265.04K revenue  
  - **Ameena Salim** – 513 orders  
  - **Deepa R** – 499 orders  
  - **Rakhi Menon** – 497 orders
- **Average Order Frequency**:  
  - **Significant decline** from **14 orders per month in March** to just **5 in April 2025**.
- These **loyal customers** represent a substantial portion of revenue, highlighting the importance of retention.

**Demographic Insights**:
- **Customer Gender Distribution**:  
  - **Female**: 56.54%  
  - **Male**: 43.47%
- **City Distribution**:  
  - Fairly consistent customer count across cities (30-39 per city).  
  - **Average Order Value (AOV)** ranges from ₹465 to ₹481, with significant city-level variations.

**Customer Preferences & Feedback**:
- **Top-Rated Restaurants**:  
  - **Hotel Kairali** leads with 17 five-star ratings.  
  - **Heritage View Restaurant**, **Hotel Green Park**, and **Hotel Pearl Regency** follow with 16 five-star ratings each.
- **Top Restaurant for Loyal Customers**:  
  - **14 Avenue Restaurant** stands out, being the most-ordered restaurant for 5 out of 7 top reviewers.
- **Loyalty Indicator**:  
  - Top reviewers show a preference for consistent ordering from the same restaurants, indicating strong **brand loyalty**.

#### 📉 Key Observations:
- **Order Frequency Drop**: The **sharp drop** in **order frequency** from **14 to 5 orders per month** correlates with the revenue decline seen across other dashboards for April 2025.
- **Brand Loyalty**: **14 Avenue Restaurant** emerges as a **customer favorite** but wasn’t featured as a top performer in other dashboards.
- **Gender Distribution**: While **female customers** make up a higher percentage, the **top customers** are fairly balanced between genders.
- **AOV Variation**: City-specific **AOV differences** suggest potential for **targeted promotions** in cities with lower performance.

🧠 *This dashboard underscores the importance of **customer retention** and **loyalty**, where a small group of high-engagement customers drives significant revenue. It highlights actionable insights for targeted marketing and engagement strategies.*
### 🖼️ Dashboard 4: Payments & Revenue  
> *"Analyzing payment patterns, city-level revenue performance, and payment processing metrics to uncover systemic issues in April 2025."*

![Payments & Revenue Dashboard](https://github.com/akhilanm123/Kerala-Food-Delivery-Analytics-with-Python-SQL/blob/main/Payment%20and%20Revenue%20Dashboard.png)

#### 📊 Key Insights:

**Revenue Distribution & Trends**:
- **Total Revenue**: ₹80,80,257.60 across all cities.
- **Top Cities by Revenue**:  
  - **Kollam**: ₹6,36,763.88  
  - **Kasargod**: ₹4,61,425.90
- **Revenue Decline**: A **sharp drop** in **April 2025** revenue, consistent across all cities, dropping to ₹9,23,958.41 from ₹27,59,820.95 in March (66.5% decrease).
- **Peak Revenue**: **March 2025** was the highest revenue month for all cities.

**Payment Method Analysis**:
- **Most Popular Payment Methods**:  
  - **Card & UPI Payments**: ₹2.7M each in revenue  
  - **Cash Payments**: ₹2.6M in revenue  
- **Payment Failures**:  
  - **UPI** has the highest failure rate at **10.4%**  
  - **Cash** follows with a **10.0% failure rate**  
  - **Card Payments**: Most reliable, with a **9.4% failure rate**

**Payment Processing Metrics**:
- **Successful Payments**: 17K transactions processed successfully.
- **Failed Payments**: 2K transactions (10.5% failure rate).
- **Refunded Transactions**: 1K transactions (5.3% of total payments).
- **Payment Issues**: Combined, **15% of all transactions** faced payment processing issues (failed or refunded).

#### 📉 Key Observations:
- **Revenue Drop**: The **April 2025 decline** aligns with the sharp drop seen in earlier dashboards, indicating broader operational or market challenges.
- **Payment Failures**: The **high payment failure rates** across **UPI, cash, and card payments** suggest **technical issues** affecting transaction success, which could contribute to **customer dissatisfaction** and cancellations.
- **Refunds**: The **5.3% refund rate** suggests potential **order fulfillment issues** or dissatisfaction with service quality.
- **Geographic Patterns**: Despite differences in city performance, the **revenue patterns** are similar across all cities, suggesting systemic issues affecting all locations.

🧠 *This dashboard highlights **payment-related challenges** that may be impacting **customer satisfaction**, contributing to the overall revenue decline observed in April 2025. The high failure and refund rates warrant an immediate review of the payment processing system to address potential technical or operational issues.*

### 🖼️ Dashboard 5: Order & Delivery Analytics  
> *"Analyzing order fulfillment, delivery performance, and operational inefficiencies to enhance customer experience and optimize logistics."*

![Order & Delivery Analytics Dashboard](https://github.com/akhilanm123/Kerala-Food-Delivery-Analytics-with-Python-SQL/blob/main/Order%20%26%20Delivery%20Analytics%20Dashboard.png)

#### 📊 Key Insights:

**Order Fulfillment Metrics**:
- **Total Orders**: 20K orders, with **16K successful orders** (80% success rate).
- **Cancellation Rate**: 5% of orders (977 orders) were canceled.
- **Delayed Orders**: The remaining 15% likely represent **delayed orders** that were eventually fulfilled.

**Delivery Performance Issues**:
- **Top Delayed Restaurants**:  
  - **Café Paprika Malappuram** & **Hotel Lake Palace**: Both have the **highest delay rates** at **55.17%** each.
  - **Rapsy Restaurant Munnar**: Concerning **50% delay rate**.
  - **Hotel Green Park**: Has the highest absolute number of delayed orders (24).
- Several other major restaurants report delay rates **over 30%**.

**Delivery Partner Performance**:
- Significant **variation** in delivery times between partners:  
  - **Sreejith** has the fastest delivery time (**2.4 minutes**).
  - **Ajmal (2.5 min)**, **Jithin (2.7 min)**, and **Anas (2.7 min)** provide **faster services**.
  - **Akhil**, **Rahul**, and **Aju** have the **slowest delivery times** (**3.1 minutes**).

**Geographic and Timing Patterns**:
- **Cities**: Delivery delay times vary by location:  
  - **Clt** has the **highest delay** (3.55 mins).
  - **Kgd** has the **lowest delay** (2.06 mins).
- **Peak Order Times**:  
  - **Monday at 10 AM** and **Sunday at 4 PM** each see **23 orders**, indicating potential **staffing and resource optimization opportunities** during peak times.
- **Delivery Partner Cancellation Rates**: Fairly **balanced rates** between partners, ranging from **9.5-12.2%**.

#### 📉 Key Insights:
- **High Delivery Delays**: Restaurants like **Café Paprika** and **Hotel Lake Palace** with **55% delay rates** are likely contributing significantly to **customer dissatisfaction**.
- **Inconsistent Delivery Partner Performance**: A **29% variation** between the **fastest** and **slowest** delivery times suggests room for improvement in logistics and training.
- **Geographic Delays**: Cities like **Clt** with **higher delays** (3.55 mins) could indicate **staffing or infrastructure challenges**, requiring additional focus.
- **Order Peak Optimization**: Understanding that **Monday at 10 AM** and **Sunday at 4 PM** experience peak ordering can help optimize **staffing and delivery resources** to improve service efficiency.

🧠 *This dashboard uncovers **operational inefficiencies** in order fulfillment and delivery processes, which directly affect customer experience. Addressing these issues can improve overall performance and customer satisfaction.*

## 🏁 Final Conclusion

This project demonstrates a **full-stack data analytics** solution, where **Python** was used for **data simulation**, **PostgreSQL** for **data storage**, and **Power BI** for **data visualization**. By generating and analyzing real-world food delivery data, we uncovered valuable insights into **restaurant performance**, **customer behavior**, and **payment trends**.

### Key Findings:
- **Revenue decline** across all cities in April 2025.
- **High cancellation rates** at specific restaurants indicating operational inefficiencies.
- **Customer loyalty** driving significant revenue.

By integrating **Python**, **PostgreSQL**, and **Power BI**, this project showcases how data-driven insights can be leveraged to improve business performance and inform strategic decisions.













