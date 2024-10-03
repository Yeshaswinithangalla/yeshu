from ..product.inventory import items
def order():
    product_name=input("Enter the product")
    if product_name in items:
        if items[product_name]["stock"]>0:
            n=int(input("Enter how many products do you want"))
            if n<=items[product_name]["stock"]:
                pay=n*items[product_name]["price"]
                print("Total amt",pay)
                amt=int(input("Enter the amount"))
                if amt==pay:
                    items[product_name]["stock"]-=n
                    print("Your order has confirmed")
                else:
                    print("CANT YOU SEE THE AMT")
        else:
            print("Outoff Stock")
    else:
        print("PRODUCT NOT AVAILABLE")
