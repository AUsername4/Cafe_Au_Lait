import time #for time.sleep's, to make it easier to follow than just all the text being thrown out at once
python_file = open("Daily Summary.py", "w")
P = 'E'
while P == 'E':
    neworsum = input("Would you like to place an order (1)? or view the daily summary? (2): ")
    if neworsum == 1:
        print("""Today's coffee choices are:
1: Cappuccino:   $3.00  
2: Espresso:     $2.25
3: Latte:        $2.50
4: Iced Coffee:  $2.50
""")
        cofdict = {1: 3,  2: 2.25, 3: 2.5, 4: 2.5} #prices of the coffee
        feedict = {1: 0.1, 2: 0.05} #the discount percentages
        quantdict = {} #quanty of each coffee
        pricedict = {} #price of each coffee
        totaldict = {} #total price (gst + base) of each coffee
        gstdict = {} #gst for each coffee
        time.sleep(1)
        order = raw_input("Would you like to order (y) yes or (n) no?: ")
        while order.lower() == 'y':
            time.sleep(0.5)
            coffee = input("What coffee would you like to order?: ")
            time.sleep(0.5)
            amount = int(input("How many would you like to order: "))
            time.sleep(0.5)
            if coffee == 1:

                price = cofdict[1]*amount
                sgst = feedict[1]*cofdict[1]
                tgst = sgst*amount
                tgst = round(tgst, 3)
                quantdict['Cappuccino'] = amount
                pricedict['Cappuccino'] = price
                gstdict['Cappuccino'] = tgst
                total = pricedict['Cappuccino']+tgst
                totaldict['Cappuccino'] = total
                print('\n'.join("{}: ${}".format(g, v) for g, v in totaldict.items()))
            elif coffee == 2:

                price = cofdict[2]*amount
                sgst = feedict[1]*cofdict[1]
                tgst = sgst*amount
                tgst = round(tgst, 3)
                quantdict['Espresso'] = amount
                pricedict['Espresso'] = price
                gstdict['Espresso'] = tgst
                total = pricedict['Espresso']+tgst
                totaldict['Espresso'] = total
                print('\n'.join("{}: ${}".format(g, v) for g, v in totaldict.items()))
            elif coffee == 3:

                price = cofdict[3]*amount
                sgst = feedict[1]*cofdict[1]
                tgst = sgst*amount
                tgst = round(tgst, 3)
                quantdict['Latte'] = amount
                pricedict['Latte'] = price
                gstdict['Latte'] = tgst
                total = pricedict['Latte']+tgst
                totaldict['Latte'] = total
                print('\n'.join("{}: ${}".format(g, v) for g, v in totaldict.items()))
            elif coffee == 4:

                price = cofdict[4]*amount
                sgst = feedict[1]*cofdict[1]
                tgst = sgst*amount
                tgst = round(tgst, 3)
                quantdict['Iced Coffee'] = amount
                pricedict['Iced Coffee'] = price
                gstdict['Iced Coffee'] = tgst
                total = pricedict['Iced Coffee']+tgst
                totaldict['Iced Coffee'] = total
                print('\n'.join("{}: ${}".format(g, v) for g, v in totaldict.items()))
            else:
                print("That is not a valid ")
            time.sleep(0.5)
            order = raw_input("Would you like to order anything else? (y) yes or (n) no?: ")
            if order == 'n':
                numtotal = 0
                for item in totaldict:
                    numtotal = numtotal + totaldict[item]
                time.sleep(0.5)
                dineortake = input("""Would you like to dine in?(1) or take away?(2) 
[Take away will incur an aditional 5% surcharge]: """)
                if dineortake == 2:
                    gsttotal = feedict[2]*numtotal
                    truetotal = gsttotal+numtotal
                    time.sleep(0.5)
                    gsttotal = round(gsttotal, 3)
                    truetotal = round(truetotal, 3)
                    print("Your total with surcharge is ${}".format(truetotal))
                elif dineortake == 1:
                    truetotal = numtotal

                else:
                    print("That is not a valid input.")
                time.sleep(0.5)
                print("Thank you for eating with us, find your receipt bellow:")
                time.sleep(0.5)
                print("Here is your receipt:")
                print('\n'.join("You ordered {}: {}".format(g, v) for g, v in quantdict.items()))
                time.sleep(1)
                print('\n'.join("Price at {}: ${} ex. gst".format(g, v) for g, v in pricedict.items()))
                time.sleep(1)
                print('\n'.join("gst added {}: ${}".format(g, v) for g, v in gstdict.items()))
                time.sleep(1)
                if dineortake == 2:
                    print("Take away surcharge added $ {}".format(gsttotal))
                    time.sleep(1)
                else:
                    print("")
                print("Your total price, including gst is: ${}".format(truetotal))
                time.sleep(1)
                print("Thank you for your purchase.")
        else:
            time.sleep(1)
            print("Have a great day :D")
            time.sleep(5)
    elif neworsum == 2:
        print("Daily Summary")

        python_file.write('print("Hello World!")')
        python_file.close()
    else:
        print("This is not a valid input.")
else:
    quit()
