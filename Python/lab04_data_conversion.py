
print("===================================")
print("      DATA CONVERSION UTILITY      ")
print("===================================")
product_name = input("Enter Product Name : ")


price = float(input("Enter Price        : "))


quantity = int(input("Enter Quantity     : "))


total_price = price * quantity


amount_str = str(total_price)



print("\n===================================")
print("        TYPE CASTING SUMMARY       ")
print("===================================")
print(f"{'Variable':<14} {'Value':<15} {'Python Type'}")
print("-----------------------------------")
print(f"{'product_name':<14} {product_name:<15} {type(product_name)}")
print(f"{'price':<14} {price:<15} {type(price)}")
print(f"{'quantity':<14} {quantity:<15} {type(quantity)}")
print(f"{'total_price':<14} {total_price:<15} {type(total_price)}")
print(f"{'amount_str':<14} {amount_str:<15} {type(amount_str)}")
print("===================================")



print("\n===================================")
print("            TAX INVOICE            ")
print("===================================")
print(f"Product Name  : {product_name}")
print(f"Price per Unit: Rs. {price:.2f}")
print(f"Quantity      : {quantity}")
print("-----------------------------------")
print(f"Invoice Total : Rs. {amount_str}")
print("===================================")