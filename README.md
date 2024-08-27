# **Supply Chain Inventory Optimization**

Welcome to the **Supply Chain Inventory Optimization** project repository! This project is designed to help businesses manage their inventory levels efficiently by calculating critical inventory metrics such as Lead Time Demand, Safety Stock, and Reorder Points. These calculations aim to minimize stockouts and overstocking, ensuring smooth supply chain operations.

## **Project Overview**

Effective inventory management is a critical component of supply chain success. This project addresses common challenges in inventory management, such as when to reorder stock and how much safety stock to keep on hand. By calculating key metrics based on historical data, this project helps businesses optimize their inventory levels and maintain operational efficiency.

---

## **How the Project Was Developed**

The **Supply Chain Inventory Optimization** project was built using **Python**, leveraging libraries like **Pandas** for data manipulation and **NumPy** for statistical calculations. Here’s an overview of the steps followed during the development:

1. **Data Loading and Cleaning**:
   - I started by importing the dataset, which contains information on product types, SKUs, stock levels, lead times, and the number of products sold.
   - The data was cleaned to ensure there were no missing values, and exploratory data analysis (EDA) was conducted to understand the data distributions.

2. **Lead Time Demand Calculation**:
   - **Lead Time Demand** was calculated as:  
     ``` 
     Lead Time Demand = (Lead Time) x (Number of Products Sold) / (Stock Levels)
     ```  
     This metric estimates the demand during the lead time based on historical sales and stock availability.

3. **Safety Stock Calculation**:
   - I used a 95% service level (Z = 1.65) to compute **Safety Stock** to account for fluctuations in demand and lead time variability. The formula for calculating safety stock is:  
     ``` 
     Safety Stock = Z * sqrt(variance in Lead Times * variance in Number of Products Sold)
     ```  
     This ensures that there is a buffer to prevent stockouts due to unpredictable factors.

4. **Reorder Point Calculation**:
   - The **Reorder Point** is the point at which a new order should be placed to avoid running out of stock. It is calculated as:  
     ``` 
     Reorder Point = Lead Time Demand + Safety Stock
     ```  
     This ensures orders are placed in time to replenish stock before it runs out.

5. **Data Testing and Validation**:
   - After computing these metrics, I ran tests to validate the accuracy of the calculations and to ensure that the results were realistic and useful for practical applications.

---

## **How It Works**

The project performs the following tasks:

1. **Input Data**: 
   - The dataset contains information on product SKUs, stock levels, lead times, and sales data.

2. **Lead Time Demand Calculation**: 
   - Using historical sales and lead times, the project calculates the number of units that will be needed during the lead time for each product.

3. **Safety Stock Calculation**: 
   - It calculates the amount of safety stock needed to prevent stockouts due to variations in demand and lead time.

4. **Reorder Point Calculation**: 
   - Finally, it determines the reorder point, which is the stock level at which a new order should be placed to avoid running out of stock.

By automating these calculations, the project helps businesses optimize their inventory management processes.

---

## **Results and Outcomes**

The main outcome of this project is the **Reorder Point** for each product type and SKU, helping businesses to optimize inventory levels. The key results include:

1. **Optimized Reorder Points**:
   - The project generates precise reorder points for each SKU, allowing businesses to know exactly when to place new orders.

2. **Improved Inventory Management**:
   - By calculating lead time demand and safety stock, businesses can avoid both overstocking and stockouts.

3. **Increased Operational Efficiency**:
   - By having an optimized reorder point, the supply chain operates more efficiently, ensuring that inventory levels are balanced.

Here’s a sample output from the project:

```
   Product type    SKU  Reorder Point
0      haircare   SKU0     182.03
1      skincare   SKU1     501.84
2      haircare   SKU2     165.24
3      skincare   SKU3     132.15
...
```

This table shows the calculated reorder points for different product SKUs, which can be used by businesses to maintain optimal inventory levels.

---

## **Conclusion**

The **Supply Chain Inventory Optimization** project provides a data-driven solution for businesses looking to improve their inventory management processes. By automating the calculation of critical metrics like Lead Time Demand, Safety Stock, and Reorder Points, the project helps businesses maintain the right inventory levels, reduce costs, and improve overall efficiency.

---

## **Technologies Used**

- **Python**
- **Pandas**
- **NumPy**
- **Jupyter Notebook**

---

## **How to Run the Project**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/supply-chain-inventory-optimization.git
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook to calculate reorder points and safety stock:
   ```bash
   jupyter notebook inventory_optimization.ipynb
   ```

---

Feel free to explore and contribute to this project. If you have any questions or feedback, please reach out!

---

### **Contact**

- **Author**: Mandal Manikantan P
- **Email**: manikantan9944@gmail.com
- **GitHub**: [https://github.com/manikantancodes](https://github.com/manikantancodes)