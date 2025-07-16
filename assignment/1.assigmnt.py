# Collecting Formula 1 Car Product Details

# 1. Product ID
product_id = int(input("Enter Product ID : "))

# 2. Product Name
product_name = input("Enter Product Name : ")

# 3. Price
price = float(input("Enter Price : "))

# 4. Categories
categories_input = input("Enter Categories separated by commas : ")
categories = [cat.strip() for cat in categories_input.split(",")]

# 5. Stock Details
stock_available = int(input("Enter Available Stock : "))
stock_sold = int(input("Enter Sold Items : "))
stock_details = (stock_available, stock_sold)

# 6. Discount Percentage
discount = float(input("Enter Discount Percentage : "))

# 7. Product Features
features_input = input("Enter Product Features separated by commas : ")
product_features = {feature.strip() for feature in features_input.split(",")}

# 8. Supplier Details
supplier_name = input("Enter Supplier Name : ")
supplier_contact = input("Enter Supplier Contact Number : ")
supplier_location = input("Enter Supplier Location : ")
supplier_details = {"Name": supplier_name,"Contact": supplier_contact,"Location": supplier_location}



# Displaying the collected product information
print("\n Formula 1 Car Product Information:")
print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Price: ₹{price:,.2f}")
print(f"Categories: {categories}")
print(f"Stock Details (Available, Sold): {stock_details}")
print(f"Discount: {discount}%")
print(f"Features: {product_features}")
print(f"Supplier Info: {supplier_details}")
