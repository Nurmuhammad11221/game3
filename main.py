MENU = {
    'expresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
            'sugar': 2,
        },
        'narx': 1.5,
    },

    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
            'sugar': 2,

        },
        'narx': 3.5
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
            'sugar': 2,
        },
        'narx': 3.0
    }
}

foyda = 0

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'sugar': 10,
}

def is_resource_sufficient(order_ingredients):
    """Agar mahsulotlar yetarli bo'lsa True, yetarli bo'lmasa False qaytaradi"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Uzur mahsulotimiz tugab qoldi {item}.")
            return False
    return True

def proccess_coins():
    """ Kiritilgan tanglarni hisoblovchi funksiya  """
    print("Iltimos tangalarni kiriting.")
    total = int(input("0.25$ sentlik puldan qancha? ")) * 0.25
    total += int(input("0.1$ sentlik puldan qancha? ")) * 0.1
    total += int(input("0.05$ sentlik puldan qancha? ")) * 0.05
    total += int(input("0.01$ sentlik puldan qancha? ")) * 0.01
    return total

def is_transuction_successful(money_received, drink_cost):
    """ Agar pul qabul qilinsa True, qabul qilinmasa False qaytaruvchi funksiya """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"{change}")
        global foyda
        foyda += drink_cost
        return True
    else:
        print("Uzur mablag' yetarli emas.")
        return False

def make_coffee(drink_name, order_ingredients):
    """ Kofe tayyorlovchi va masaliqlarni tekshiruvchi funksiya """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Sizning {drink_name} ☕️ kofeyingiz tayyor. Yoqimli ishtaha!")


is_on = True

while is_on:
    e_narx = MENU['expresso']['narx']
    l_narx = MENU['latte']['narx']
    c_narx = MENU['expresso']['narx']

    print(f"expressoning narxi: {e_narx} \nlattening narx narxi: {l_narx} \ncappuccinoning narx: {c_narx}")

    

    tanlash = input("Qaysi kofe turini tanlaysiz? (expresso/latte/cappuccino): ")

    if tanlash == "o'chirish":
        is_on = False
    elif tanlash == 'hisobot': # report
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Sugar: {resources['sugar']}ta")
        print(f"Pul: {foyda}$")
    else:
        drink = MENU[tanlash]
        if is_resource_sufficient(drink["ingredients"]):
            payment = proccess_coins()
            if is_transuction_successful(payment, drink["narx"]):
                make_coffee(tanlash, drink['ingredients'])