#Name: Vinita Devi
# College: Lovely Professional University Phagwara Punjab
# Passing Year: 2023
# Phone No: 6392280899
# email: vinitasinghraj1999@gmail.com



# # "products" is a dictionary data type which is a built in data structure in python 
# "products" is a dict which contains keys as the product name
# and values as a list with first element as Unit prices in rupees
# second element as GST and last quantity 
basket = {
    'Leather':[1100,18,1],
    'Umbrella': [900,12,2],
    'Cigarette': [200,28,3],
    'Honey':[100,0,4]

}
tax_lst=[]
# printing the total amount to be paid by the shopkeeper and maximum GST paid
total_price = 0
for i in basket.values():
    item_price = i[0]*i[2]
    tax_lst.append(i[1])
   
   
    if i[0] >= 500:
        item_price = item_price - (0.05 * item_price)
    item_price = item_price + (i[1]*item_price)
    item_price += item_price
max_tax=max(tax_lst)    
print("Total Amount  to be  paid to the shopkeeper is: {}".format(total_price))
print("The  maximum tax  is {}".formate(max_tax))