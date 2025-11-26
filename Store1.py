products = {
    100     :   {'name': 'blouse', 'price': 20, 'color': 'blue'},
    101     :   {'name': 'belt', 'price': 10, 'color': 'black'},
    102     :   {'name': 'boots', 'price': 29, 'color': 'black'},
    103     :   {'name': 'cap', 'price': 7, 'color': 'red and blue'},
    104     :   {'name': 'cap', 'price': 7, 'color': 'yellow and blue'},
    105     :   {'name': 'coat', 'price':60, 'color': 'brown'},
    106     :   {'name': 'dress', 'price': 45, 'color': 'red'},
    107     :   {'name': 'dress', 'price': 45, 'color': 'blue'},
    108     :   {'name': 'gloves', 'price': 15, 'color': 'black'},
    109     :   {'name': 'hat', 'price': 20, 'color': 'yellow'},
    110     :   {'name': 'hoodie', 'price': 35, 'color': 'white'},
    111     :   {'name': 'hoodie', 'price': 35, 'color': 'blue'},
    112     :   {'name': 'sweater', 'price':65, 'color': 'black'},
    113     :   {'name': 'jacket', 'price': 65, 'color': 'white'},
    114     :   {'name': 'jeans', 'price': 55, 'color': 'blue'},
    115     :   {'name': 'jeans', 'price': 55, 'color': 'black'},
    116     :   {'name': 'pants', 'price': 40, 'color': 'grey'},
    117     :   {'name': 'scarf', 'price': 20, 'color': 'red'},
    118     :   {'name': 'shirt', 'price':35, 'color': 'stripe'},
    119     :   {'name': 'leather shoes', 'price': 150, 'color': 'brown'},
    120     :   {'name': 'skirt', 'price': 25, 'color': 'black'},
    121     :   {'name': 'short', 'price': 15, 'color': 'hawaiian'},
    122     :   {'name': 'socks', 'price': 8, 'color': 'black'},
    123     :   {'name': 'socks', 'price': 8, 'color': 'white'},
    124     :   {'name': 'suit', 'price':200, 'color': 'black'},
    125     :   {'name': 'suit', 'price':200, 'color': 'grey'},
    126     :   {'name': 'T-shirt', 'price': 35, 'color': 'blue'},
    127     :   {'name': 'T-shirt', 'price': 35, 'color': 'orange'},
    128     :   {'name': 'tie', 'price': 12, 'color': 'navy blue'},
    129     :   {'name': 'nike sneakers', 'price': 95, 'color': 'red and white'},
    130     :   {'name': 'nike sneakers', 'price': 95, 'color': 'blue and white'},
    131     :   {'name': 'adidas sneakers', 'price': 120, 'color': 'yellow and red'},
    132     :   {'name': 'sunglasses', 'price':20, 'color': 'black'},
    133     :   {'name': 'vest', 'price': 40, 'color': 'navy blue'},
    134     :   {'name': 'polo shirt', 'price': 45, 'color': 'orange'},
    135     :   {'name': 'polo shirt', 'price': 45, 'color': 'cream'},
}

print('\n                    Welcome to the ( Fashion Heaven )\n')
print('Hello\n')
while True:
    first_name = input('enter your first name: ')
    if first_name.isdigit():
        print('please enter valid name')
        continue
    last_name = input('enter your last name: ')
    if last_name.isdigit():
        continue
        print('please enter valid name')
    else:
        print('your name has been registered')
        break
import random
discount_give = random.randint(12345,99998)
print('10% off \n')
print(f' your discount code is {discount_give}')


def show_products():
    print('-'*71)
    print(f'|{"Code":^10}|{"Name":^25}|{"color":^20}|${"Price":^10}|')
    print('-'*71)
    for code in products:
        print(f'|{code:^10}|{products[code]["name"]:^25}|{products[code]["color"]:^20}|${products[code]["price"]:^10}|')
    print('-'*71)


print('')

while True:
    show = input('enter "guide" to help you how to use or "q" to quit and enter "show"\n to see the products:')
    if show == 'show':
        show_products()
        print('')
        break
    if show == 'guide':
        print('\nguide:')
        print('\nchoose one of products\n')
        print('enter code of your selected product to add product in shopping cart')
        print('enter add or sub after that enter products code to add or remove product.\n')
        continue
    if show == 'q':
        break
        
    else:
        print('enter your option only\n')

    
def show_products2():
    total_price = 0
    print('-' * 70)
    print(f'|{"Code":^10}|{"Name":^20}|{"Color":^15}|{"Quantity":^10}|{"Price":^9}|')
    print('-' * 70)
    total_price = 0
    for code, quantity in cart.items():
        product = products[code]
        price = product["price"] * quantity
        total_price += price  
        print(f'|{code:^10}|{product["name"]:^20}|{product["color"]:^15}|{quantity:^10}|${price:^8}|')

    print('-' * 70)
    print(f'|{"Total Price":^58}|${total_price:^8}|')
    print('-' * 70)


cart = {}

def shopping_cart():
    while True:
        action = input('enter "add" to add or "sub" to remove and enter "show" to \nsee cart or "q" to quit:')
        action = action.strip().lower()
        if action == 'add':
            code = input('enter product code:')
            if code.isdigit():
                code = int(code)
                if code in products:
                    cart[code] = cart.get(code, 0) + 1
                    print(f'{products[code]} added to cart')
                else:
                    print('invalid product code')
            else:
                print('enter numbers only')  

        elif action == 'sub':
            code = input('enter product code: ')
            if code.isdigit():
                code = int(code)
                if code in cart:
                    cart[code] -= 1
                    if cart[code] == 0:
                        cart.pop(code)
                    print(f'{products[code]} removed from cart')
                else:
                    print('product not in cart')
            else:
                print('enter numbers only') 
                
        elif action == 'show':
            show_products2()
            
        elif action == 'q':
            break

        else:
            print('invalid command')

if not show == 'q':
    
    import random
    invoices_number = random.randint(123456789, 1123456789+1)

    shopping_cart()
    while True:
        com = input('\nenter "complete" to complete the  purchase or "continue"\nto continue your shopping:')
        if com == 'complete':
            print('\nyour invoice:\n')
            print(f'your invoices number is  {invoices_number} \n')
            show_products2()
            break
        elif com == 'continue':
            shopping_cart()
            break
        else:
            print('enter your option only')

    while True:
        com2 = input('enter "invoice" to see invoice or "buy" to add in your shoping cart again or enter  "finish"\n to final purchase:')
        if com2 == 'invoice':
            print(f'\n your invoices number is  {invoices_number} \n')
            show_products2()

        elif com2 == 'buy':
            shopping_cart()


        elif com2 == 'finish':
            print('it is your invoices:')
            print(f'\n your invoices number is  {invoices_number} \n')
            show_products2()
            break
        
        else:
            print('enter your options only \n')
            
    print('How would you like your order delivered?\n')
    print('courier -> 35$ \npost -> 20$\n')

    while True:
        send = input('enter "courier" to send you by courier or enter "post" to send you by post:')
        shipping_price = 0  
        if send == 'courier':
            shopping_price = 35
            break
        elif send == 'post':
            shopping_price = 20
            break
        else:
            print('enter your option only')

    print('\nhow many days will the product reach you?\n')
    print('your choice should be between 2 and 7 days.\n ')

    while True:
        days = input('enter the days between 2 and 7 :')
        if days.isdigit():
            days = int(days)
            if 1 < days <= 7:
                break
            else:
                print('\nenter the days between 2 and 7 only.')
        else:
            print('\nenter numbers only.')

    print('\nDelivery Method:\n')
    print(f'the products will send you by "{send}"')

    if send == 'courier':
        print(f'the price of this send is ${shopping_price}')
    if send == 'post':
        print(f'the price of this send is ${shopping_price}\n')


    total_price = 0

    for code, quantity in cart.items():
        product = products[code]
        price = product["price"] * quantity
        total_price += price


    final_price = total_price + shopping_price
    final_price_discount = 0
    
    
    while True:
        discount = input('if you have a discount code enter "off" to apply or \nenter "q" to quit: ')
        if discount == 'off':
            while True:
                discount_code = input('enter your discount code:')
                if discount_code.isdigit() and len(discount_code) == 5:
                    discount_code = int(discount_code)
                    if discount_code == discount_give:
                        final_price_discount = final_price * 0.1
                        print('discount applied')
                        break
                    else:
                        print('invalid discount code')
                else:
                    print('discount code must be 5 digit')
            break
                
        if discount == 'q':
            break
        
        else:
            print('enter your options only')
            
    print(f'\n your invoices number is  {invoices_number} \n')

    final_price_discount = round(final_price_discount)
    
    print('-' * 70)
    print(f'|{"Code":^10}|{"Name":^20}|{"Color":^15}|{"Quantity":^10}|{"Price":^9}|')
    print('-' * 70)
    total_price = 0
    for code, quantity in cart.items():
        product = products[code]
        price = product["price"] * quantity
        total_price += price  
        print(f'|{code:^10}|{product["name"]:^20}|{product["color"]:^15}|{quantity:^10}|${price:^8}|')
        
    print('-' * 70)
    print(f'|{"Delivery price":^58}|${shopping_price:^8}|')
    print('-' * 70)
    print(f'|{"discount":^58}|${final_price_discount:^8}|')
    print('-' * 70)
    print(f'|{"Total Price":^58}|${final_price - final_price_discount:^8}|')
    print('-' * 70)



    print('')

    while True:
        address = input('enter your address:')
        if address.isdigit():
            print('enter your address correctly')
        else:
            print('your address has been registered\n')
            break

    while True:
        email = input('enter your e-mail address:')
        if len(email) >= 16:
            if email.endswith('@gmail.com') and email.count('@') == 1: 
                print('your e-mail address has been registered')
                break
            else:
                print('enter your e-mail address correctly')
        else:
            print('e-mail address must have at least 6 characters')
            
            

    import random
    pay_at_home = random.randint(12345678, 100000000)



    while True:
        pay = input('enter "online" to pay online or enter "home" to pay at home: ')
        if pay == 'home':
            print('\n receive code:\n')
            print(pay_at_home,'\n')
            print('You must give the receiving code to the courier or postman to receive the product.')
            print('\nto find out the status of your package, enter the receive code on the www.fashion haven.ir  \nand find out the status of your package.')
            break

        if pay == 'online':
             print('online payment:\n')
             print(f'your amount is ${final_price}\n')
             print(f'payer: {first_name} {last_name}')
             print('recipient: Fashion Heaven\n')
             print('card information:\n')
             break
             
        else:
            print('enter your option only')
    if pay == 'online':
        while True:         
            card_number = input('enter your card number: ')
            if card_number.isdigit():
                if len(card_number) == 16:
                    print(f'your cart number has been registered -> {card_number}\n')
                    break
                else:
                    print('the number must be 16 digit')
            else:
                print('enter numbers only')
                 
                    
        if pay == 'online':
            while True:
                cvv2 = input('enter your cvv2: ')
                if cvv2.isdigit():
                    if 3 <= len(cvv2) <5:
                        print(f'your cvv2 has been registered -> {cvv2}\n')
                        break
                    else:
                        print('the number must be 3 or 4 digit')
                else:
                    print('enter numbers only')

            while True:
                expiration_year = input("enter the expiration year: ")
                if expiration_year.isdigit() and len(expiration_year) == 4:
                    break
                else:
                    print('year must be 4 digit')

            while True:
                expiration_month = input('enter the expiration month: ')
                if expiration_month.isdigit() and 1 <= int(expiration_month) <= 12:
                    break
                else:
                    print('month must be number between 1 and 12')


            while True:
                import random
                security_code = random.randint(1, 100)
                security_code1 = random.randint(1, 100)

                print('\n security code:\n')
                print(f'{security_code} + {security_code1} = ?')
                security = input('enter answer of security code: ')
                if security.isdigit():
                    security = int(security)
                    if security_code + security_code1 == security:
                        print('the security code is True')
                        break
                    else:
                        print('the security code is False, try again')
                else:
                    print('enter number only')

            import random
            password = random.randint(1234567, 9999998)

            while True:
                
                dynamic_password = input('enter "password" to get the dynamic password: ')
                if dynamic_password == 'password':
                    print(f'\nyour dynamic_password is {password} ')
                    break
                else:
                    print('enter your option')

            while True:
                confirmation = input('enter dynamic password to payment: ')
                if confirmation.isdigit():
                    if len(confirmation) == 7:
                        confirmation = int(confirmation)
                        if confirmation == password:
                            print('payment has been made successful')
                            break
                        else:
                            print('dynamic password is wrong')
                    else:
                        print('dynamic password must be 7 digit')
                else:
                    print('please enter numbers only')
            import random
            follow_up = random.randint(12345678, 100000000)
            shop = 'Fashion Heaven'
            destination = 'paid'
            print('\nyour receipt:\n')
            print()

            print('-' * 73)
            print(f'|{"price":^50}|${final_price:^19}|')
            print('-' * 73)
            print(f'|{"origin card number":^50}|{card_number:^20}|')
            print('-' * 73)
            print(f'|{"destination":^50}|{shop:^20}|')
            print('-' * 73)
            print(f'|{"status":^50}|{destination:^20}|')
            print('-' * 73)
            
            print(f'\nyour follow up code: {follow_up}')
            print('\nto find out the status of your package, enter the receive code on the www.fashion haven.ir')
            print('and find out the status of your package.')

        else:
            print('Payment has been made successfully. The purchase receipt has been sent to you \n')
            print(f'thank you for your purchase Mr/Mrs {first_name} {last_name}\n .')
            print('we hope you have a good experience. we will see you again soon.\n')
            print('thank you for your cooperation.')


        print('Payment has been made successfully. The purchase receipt has been sent to you \n')
        print(f'thank you for your purchase Mr/Mrs {first_name} {last_name}.\n')
        print('we hope you have a good experience. we will see you again soon.\n')
        print('thank you for your cooperation.')
        
    else:
        print(f'thank you for your purchase Mr/Mrs {first_name} {last_name}.\n')
        print('we hope you have a good experience. we will see you again soon.\n')
        print('thank you for your cooperation.')

    while True:
        contact_us = input('enter "contact" to contact us or "q" to quit:')
        if contact_us == 'contact':
            while True:
                feedback_and_suggestions = input('enter "feedback" or "suggestions" and write your feedback and suggestions \nafter that enter q to quit:')
                if feedback_and_suggestions == 'feedback':
                    feedback = input('enter your feedback:')
                    print('\nyour feedback has been submitted and will be reviewed as soon as possible')
                
                elif feedback_and_suggestions == 'suggestions':
                    suggestions = input('enter your suggestions:')
                    print('\nthank you for your suggestions, your ideas help us improve our services')

                elif feedback_and_suggestions == "q":
                    break
            
                else:
                    print('enter your options only')
            break
        if contact_us == 'q':
            break
        else:
            print('enter your options only')

    while True:
        call = input('enter "call" to contact our support or enter "q" to quit:')
        if call == 'call':
            phone_number = input('enter your phone number:')
            if len(phone_number) == 11:
                print('our experts will call you in 24 hours')
                break
            else:
                print('invalid phone number, your phone number must be 11 digits')
                continue
        if call == 'q':
            break
        else:
            print('enter your options only')

        
    print('Goodbye')
        
else:
    print('Goodbye')




