# Florentia Teye
# florentia.teye@azubiafrica.org
# Group 8

import pandas as pd


#Step 1: Create a DataFrame from the list of dictionaries below:


data = [
    {'product_id':23, 'name':'computer', 'wholesale_price': 500, 'retail_price':1000, 'sales':100}, 
    {'product_id':96, 'name':'Python Workout', 'wholesale_price': 35,'retail_price':75, 'sales':1000},
    {'product_id':97, 'name':'Pandas Workout', 'wholesale_price': 35, 'retail_price':75, 'sales':500},
    {'product_id':15, 'name':'banana', 'wholesale_price': 0.5,'retail_price':1, 'sales':200},
    {'product_id':87, 'name':'sandwich', 'wholesale_price': 3,'retail_price':5, 'sales':300}
]



data_frame = pd.DataFrame(data)




#Step 2:  Calculate the Total Profit for each product using the formula 
""" net_revenue_per_product = (retail_price - wholesale price) * sales"""

list_of_net_revenue = []
for i in range(0, len(data_frame)):
    wholesale = data_frame.loc[i][2]
    retail = data_frame.loc[i][3]
    sales = data_frame.loc[i][4]
    net_revenue_per_product = (retail - wholesale)*sales
    list_of_net_revenue.append(net_revenue_per_product)


print('Step 1: The Net Revenue For Each Product is as follows:\n Computer: {0}\n Python Workout: {1}\n Pandas Workout: {2}\n Banana: {3}\n Sandwich: {4}'.
format(list_of_net_revenue[0],list_of_net_revenue[1],list_of_net_revenue[2],list_of_net_revenue[3],list_of_net_revenue[4]))



# Step 3: Determine the following
# - How much total net revenue you received from all of these sales?
sum = 0
for i in range(0, len(data_frame)):
    wholesale = data_frame.loc[i][2]
    retail = data_frame.loc[i][3]
    sales = data_frame.loc[i][4]
    net_revenue_per_product = (retail - wholesale)*sales
    sum = sum + net_revenue_per_product

print('\nThe Total Net Revenue from all the Sales is ',sum)

# - What product is product retail price retail_price more than twice the wholesale price
list_of_retail_greater_than_wholesale = []
for i in range(0, len(data_frame)):
    wholesale = data_frame.loc[i][2]
    retail = data_frame.loc[i][3]
    sales = data_frame.loc[i][4]
    if retail > (2*wholesale):
        list_of_retail_greater_than_wholesale.append( data_frame.loc[i][1])

print('\n Products where retail price more than twice the wholesale price is as follows:\n  {0}\n   {1}'.
format(list_of_retail_greater_than_wholesale[0], list_of_retail_greater_than_wholesale[1]))

# - How much did the store make from food vs. computers vs. books?
food_sum = 0
books_sum = 0
computer_sum = 0
for i in range(0, len(data_frame)):
    wholesale = data_frame.loc[i][2]
    retail = data_frame.loc[i][3]
    sales = data_frame.loc[i][4]

    if data_frame.loc[i][1] == 'computer':
        net_revenue_per_product_computer = (retail - wholesale)*sales
        computer_sum = computer_sum + net_revenue_per_product_computer
    elif data_frame.loc[i][1] == 'Pandas Workout' or data_frame.loc[i][1] == 'Python Workout':
        net_revenue_per_product_book = (retail - wholesale)*sales
        books_sum = books_sum + net_revenue_per_product_book
    if data_frame.loc[i][1] == 'computer':
        net_revenue_per_product_food = (retail - wholesale)*sales
        food_sum = food_sum + net_revenue_per_product_food

print('\n The Store made {1} for food, {2} for computers, {0} for books.'.format(books_sum, food_sum, computer_sum))



# - Because your store is doing so well, you’re able to negotiate a 30% discount on the wholesale price of goods. Calculate the new net revenue
new_sum = 0
for i in range(0, len(data_frame)):
    wholesale = data_frame.loc[i][2] - (0.3*data_frame.loc[i][2])
    retail = data_frame.loc[i][3]
    sales = data_frame.loc[i][4]
    net_revenue_per_product = (retail - wholesale)*sales
    new_sum = new_sum + net_revenue_per_product

print('\n The New sum with 30% discount on wholesale price is ',new_sum,'\n')