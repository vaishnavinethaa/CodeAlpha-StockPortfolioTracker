print("Welcome to Stock Portfolio Tracker")

stocks = {
    "TCS": 3500,
    "INFY": 1600,
    "RELIANCE": 1450,
    "HDFCBANK": 1800,
    "WIPRO": 270
}

grand_total = 0

while True:

    print("\nAvailable Stocks:")

    for stock in stocks:
        print(stock, ":", stocks[stock])

    stock_name = input("\nEnter Stock Name: ").upper()

    if stock_name in stocks:

        quantity = int(input("Enter Quantity: "))

        total = stocks[stock_name] * quantity

        grand_total = grand_total + total

        print("\nPortfolio Summary")
        print("Stock :", stock_name)
        print("Price :", stocks[stock_name])
        print("Quantity :", quantity)
        print("Total Investment : ₹", total)

    else:
        print("Stock Not Available")

    choice = input("\nDo you want to buy another stock? (yes/no): ").lower()

    if choice == "no":
        break

print("\nTotal Portfolio Value : ₹", grand_total)

print("\nThank You for Using Stock Portfolio Tracker!")