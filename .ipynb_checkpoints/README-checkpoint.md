# Customer Lifetime Value Prediction & Segmentation

This project analyzes e-commerce transaction data to understand customer behavior and predict future customer value using machine learning techniques.

The project combines **RFM analysis, customer segmentation, and predictive modeling** to help businesses identify high-value customers and design targeted marketing strategies.

---

# Project Objectives

• Analyze customer purchasing behavior  
• Segment customers using RFM analysis and K-Means clustering  
• Predict future customer revenue using machine learning models  
• Provide business insights for customer retention and marketing strategies  

---

# Dataset

Dataset used: **Online Retail Dataset**

The dataset contains transactional records of an online retail store including:

- Invoice Number
- Stock Code
- Product Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

---

# Project Workflow

### 1. Exploratory Data Analysis
Understanding dataset structure, missing values, and purchase patterns.

### 2. Data Preprocessing
Cleaning invalid transactions and preparing the dataset for analysis.

### 3. RFM Feature Engineering
Calculating customer behavior metrics:

Recency – Days since last purchase  
Frequency – Number of transactions  
Monetary – Total spending amount  

### 4. Customer Segmentation
Customers are grouped into segments using **K-Means clustering** based on RFM features.

### 5. CLV Estimation
Customer Lifetime Value is estimated using behavioral metrics.

### 6. Future CLV Prediction
Machine learning models are trained to predict **future customer revenue**.

Models used:

- Linear Regression
- Random Forest
- Gradient Boosting
- XGBoost

---

# Key Findings

Feature importance analysis shows the following ranking:

**Monetary > Recency > Frequency**

Interpretation:

- Customers who historically spend more tend to generate higher revenue in the future.
- Recently active customers have a higher probability of making new purchases.
- Purchase frequency contributes to predictions but is less influential compared to spending behavior.

These insights help businesses focus on **high-value and recently active customers** for targeted marketing campaigns.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Matplotlib
- Jupyter Notebook
- Power BI

---

# Project Structure

customer-lifetime-value-prediction/
│
├── data/
│   ├── raw/
│   │   └── Online Retail.csv
│   │  
│   ├── processed/
│   │   ├── processed_online_retail.csv  
│   │   ├── rfm_data.csv
│   │   ├── rfm_with_clv.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_data_preprocess.ipynb
│   ├── 03_rfm_feature_engineering.ipynb
│   ├── 04_customer_segmentation_kmeans.ipynb
│   ├── 05_clv_estimation.ipynb
│   ├── 06_future_clv_prediction.ipynb
│   ├── 07_business_insights_strategy.ipynb
│
├── src/
│   ├── rfm.py
│   ├── clustering.py
│
├── dashboards/
│   └── clv_powerbi_dashboard.pbix
│
├── results/
│   ├── customer_distribution_segment.png
│   ├── feature_importance.png
│   ├── model_comparison_results.csv
│   ├── future_revenue_distribution.png
│   ├── revenue_by_segment.png
│
├── README.md
└── requirements.txt

---

# Dashboard

A Power BI dashboard is included to visualize customer segments and revenue insights.

---

# Future Improvements

• Improve prediction accuracy with additional behavioral features  
• Deploy model as a web application  
• Build automated customer segmentation pipeline  

---