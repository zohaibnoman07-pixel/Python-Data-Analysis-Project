import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\zohai\Desktop\Sample - Superstore.csv", encoding="latin1")
data =data.dropna()
def show_data():
    print("\nfirst five rows of dataset")
    print(data.head())
def show_sales():
    print("\ntotal sales:",data["Sales"].sum())

def average_sales():
    print("\naverage sales:",np.mean(data["Sales"]))
def total_profit():
    print("\ntotal profit:",data["Profit"].sum())
def top_product():
    print("\ntop 5 products: ",data.sort_values(by='Sales', ascending =False).head()) 
def sales_by_category():
    print("\nsales by category")
    print(data.groupby('Category')['Sales'].sum())      
def plot_sales_category():
    category_sale=data.groupby('Category')['Sales'].sum()
    category_sale.plot(kind='bar')
    plt.title("sales by category")
    plt.xlabel('Category')
    plt.ylabel('Sales')
    plt.show()

def plot_sales_distribution():
    plt.hist(data['Sales'],bins=10)
    plt.title("Sales distribution")
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.show()
def plot_profit_region():
    region_profit=data.groupby('Region')['Profit'].sum()
    region_profit.plot(kind='bar')
    plt.title("profit by region")
    
    plt.xlabel('profit by region')
    plt.ylabel('profit')
    plt.show()
show_data()
show_sales()
average_sales()
total_profit()
top_product()
sales_by_category()
plot_sales_category()
plot_sales_distribution()
plot_profit_region()    

while True:
    print("\n===== SUPERSTORE DATA ANALYSIS SYSTEM =====")
    
    print("1. Graph: Sales by Category")
    print("2. Graph: Sales Distribution")
    print("3. Graph: Profit by Region")
   
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '7':
        plot_sales_category()
    elif choice == '8':
        plot_sales_distribution()
    elif choice == '9':
        plot_profit_region()
    elif choice == '10':
        print("Goodbye!")
        

        break
    else:
        print("Invalid choice!")