annual_salary = float(input("Enter your annual salary as an integer: "))

portion_saved = float(input("Enter the percent of your salary to save, in decimal form (ie 10% = .10): "))

total_cost = float(input("Enter the cost of the home you want to buy: "))

portion_down_payment = float(input("Enter percent downpayment needed in decimal form (ie 25% = .25): ") or .25)

r = float(input("Enter the expected annual rate of return as a decimal (ie 4% = .04): ") or .04)


current_savings = 0
amount_needed = total_cost * portion_down_payment
months_needed = 0

while current_savings < amount_needed:
    current_savings += (annual_salary / 12 * portion_saved) + (current_savings * (r/12))
    months_needed += 1

print ("it will take you", months_needed, "months to save your down payment")

