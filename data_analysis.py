



products = [
            "Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream",
            "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices    = [30,25,40,20,20,35,45,50,35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]


# Calculation of total price average
sum = 0
for i in prices:
    sum = sum + i
    
average_price = sum/len(prices)
print('The Average price is GHC {0:,}'.format(round(average_price, 2)))



#We create a new list to handle the new arrangement based on prices less than 30

New_prices = []
for i in prices:
    new_price = i - 5
    New_prices.append(new_price)

print("The New Prices are ", New_prices)


#We create a new variable total to handle the total amount

total = 0
for i in range(len(prices)) :
    total = total + (prices[i] * last_week[i])
    i += 1

print("The Total Amount is GHC {0:,}".format(round(total, 2)))



#We create a new list to handle the new arrangement based on prices less than 30

New_products = []
for i in range(len(New_prices)):
    if New_prices[i] < 30:
        New_products.append(products[i])

print("The New Products less than GHC 30.00 are ",New_products)

