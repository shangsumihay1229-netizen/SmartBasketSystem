coke=25
shampoo=7
noodles=13
cart=[]
stocks=['coke','shampoo','noodles']

# login system
print("=== SMART CART LOGIN ===")
username_input = input("Enter username: ")
password_input = input("Enter password: ")

# predefined login credentials
correct_username = "client"
correct_password = "1234"
# Exit
if username_input != correct_username or password_input != correct_password:
    print("Login failed! Incorrect username or password.")
    exit()
else:
    print("Login successful! Welcome to Smart Cart.\n")
    
input('Hi! welcome to smart cart heres available stocks:\n         Please press enter to go menu')
#the display menu
print('================================================\n                    STOCKS')
print('🥤 coke: 25 each')
print('🧴 shampoo: 7 each')
print("🍜 noodles: 13 each")
print('================================================')
# the shopping loop
while True:
    want=str(input('What would you like to buy? (Type done if youre finished.):')).lower()
    if want=='done':
        print('\n🙏Thank you for your purchase! Have a great day🥺.')
        break
    if want in stocks:
        print('================================================\n                    STOCKS')
        print('🥤 coke: 25 each')
        print('🧴 shampoo: 7 each')
        print("🍜 noodles: 13 each")
        print('================================================')
        cart.append(want)
        print(f"cart:{cart}")    
        count_coke=cart.count("coke")
        count_shampoo=cart.count('shampoo')
        count_noodles=cart.count("noodles")
        print(f'coke pieces:{count_coke}')
        print(f'shampoo pieces:{count_shampoo}')
        print(f'noodles pieces:{count_noodles}')
        total_coke=count_coke*25
        total_shampoo=count_shampoo*7
        total_noodles=count_noodles*13
        print('total price:',total_coke+total_shampoo+total_noodles)
    else:
        print('Dont order 2 or more product at the same time or that product was currently unavailable')
        continue
    