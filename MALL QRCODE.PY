import qrcode

def mall(a,b):
    result = a*b
    if b > 1 :
        x=(f"You bought {str(b)}{item}s which is equal to #{str(result)}.00k")
        print(x)
        generate_qrcode(x)
    else:
        x=(f"You bought {str(b)}{item}s which is equal to #{str(result)}.00k")
        print(x)
        generate_qrcode(x)


def generate_qrcode(txt):
    qr= qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 12,
        border = 4
    )

    qr.add_data(txt)
    qr.make(fit = True)

    img = qr.make_image(fill_color = "red", back_color = "white")
    img.save("MALL.png")

while True:
    print("\n\n🌷"*2, 'YOU ARE WELCOME TO NURUL HAYAT MALL',"🌷"*2,"\n")
    print("🌷"*3,"List of the Items","🌷"*3,"\n")
    print("Apple", "Bread")
    print("Cherry", "Donuts")
    print("Eggplant", "Fish")
    print("Graps", "Honey")
    print("Ice cream", "Jam")
    print("Ketchup","Lettuce")
    print("Milk", "Nunu")
    print("Onion", "Pasta")
    print("Quinoa", "Roll on")
    print("Shampoo","Tomatoes")
    print("unsalted", "Vanilla")
    print("Water bottle", "Xantha Gum")
    print("yogurt", "Zucch")

    item = input("Name of Item you purchace: ")
    if item.upper() == "Qu":
        print("Thanks for your patronage, see you next time, Bye for now ✋🏼✋🏼")
        break
    elif item.title() == "Apple":
        print("An Apple cost #1000")
        a = 1000
        b = int(input("Number of items: "))
        mall(a,b)

    elif item.title() == "Bread":
        print("A Bread cost #100")
        a = 100
        b = int(input("Number of items: "))
        mall(a,b)
        
    elif item.title() == "Cherry":
        print("A Cherry cost #300")
        a = 300
        b = int(input("Number of items: "))
        mall(a,b)
   
    elif item.title() == "Donuts":
        print("An  cost #900")
        a = 900
        b = int(input("Number of items: "))
        mall(a,b)
    
    elif item.title() == "Eggplant":
        print("An Eggplant cost #109")
        a = 109
        b = int(input("Number of items: "))
        mall(a,b)

    elif item.title() == "Fish":
        print("A Fish cost #1200")
        a = 1200
        b = int(input("Number of items: "))
        mall(a,b)

    elif item.title() == "Grapes":
        print("A Grapes cost #2000")
        a = 2000
        b = int(input("Number of items: "))
        mall(a,b)

    elif item.title() == "Honey":
        print("A bottle of Honey cost #10000")
        a = 10000
        b = int(input("Number of items: "))
        mall(a,b)

    elif item.title() == "Ice Cream":
        print("Ice cream #1700")
        a = 17000
        b = int(input("Number of items: "))
        mall(a,b)

    elif item.title() == "Jam":
        print("A bottle of #1800")
        a = 1800
        b = int(input("Number of items: "))
        mall(a,b)

    elif item.title() == "Ketchup":
        print("ketchup is #900")
        a = 900
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Lettuce":
        print("lettuce #700")
        a = 700
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Milk":
        print("A tin of Milk cost #1100")
        a = 1100
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Nunu":
        print("A bottle of Nunu cost #5600")
        a = 5600
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Onion":
        print("Onion is #500")
        a = 500
        b = int(input("Number of item(s): "))
        mall(a,b)
    elif item.title() == "Pasta":
        print("Pasta cost #1500")
        a = 1500
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Quinoa":
        print("Quinoa cost #3000")
        a = 3000
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Roll on":
        print("Roll on cost #5500")
        a = 5500
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Shampoo":
        print("Shampoo cost #900")
        a = 900
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Tomatoes":
        print("Tomatoes cost #600")
        a = 600
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Unsalted":
        print("unsalted cost #1100")
        a = 1100
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Vanilla":
        print("Vanilla cost #1500")
        a = 1500
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Water bottle":
        print("Water bottle cost #1000")
        a = 1000
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Xantha Gum":
        print("Xantha Gum cost #600")
        a = 600
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "Yogurt":
        print("yogurt cost #500")
        a = 500
        b = int(input("Number of items: "))
        mall(a,b)
    elif item.title() == "yogurt":
        print("Zucch #500")
        a = 500
        b = int(input("Number of items: "))
        mall(a,b)

    else:
        print(f"Thanks for your request, we cant fufill your request now but we will try to do so next time")
    
