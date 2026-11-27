"""A store gives discounts based on the total price: 
1-Under $50 (No discount), 
2-$50 to $100 (10% discount), 
3-and Over $100 (20% discount). 
4-If the user is a "Member," they get an additional 5% off the final calculated price. 
• Example Input: Price: 100, Member: Yes • Example Output: Final Total: $85.5 
(Note: 100 - 10% = 90; then 90 - 5% = 85.5) """

total_price = 0 
total_price = float(input("Enter total Amount? "))
is_member = input("are you Member? y or n: ")
final_price = 0
if total_price < 50:
    print("No Discount")
    final_price = total_price
if(total_price >= 50 and  total_price <= 100):
    print("10 percent discount")
    final_price = total_price * 0.90
if(total_price > 100):
    print("20 percent discount")
    final_price = total_price * 0.80
if(is_member == "y"):
    print("another 5 percent discount")
    final_price = final_price * 0.95

print(final_price)