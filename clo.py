
arr = []

def duty(price, capacity):
    tax = 0
    if capacity > 2000:
        tax = 1.186
    else:
        tax = 1.031

    nettoPrice = price * tax
    roundedNettoPrice = round(nettoPrice)

    arr.append(roundedNettoPrice)
    print(arr)

duty(10000, 1600)
duty(17500, 2600)
    
    