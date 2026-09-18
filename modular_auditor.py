inventory = 0
error_count = 0
success_count = 0

def valid_input():
    user_input = input("Enter a stock quantity : ")
    if user_input == "quit":
        return "quit"
    if user_input.isdigit() == False:
        print("The quantity entered is not a number! Please try again with integers.")
        return None
    elif int(user_input)< 0:
        print("The quantity entered is negative! Please try again with a non-negative number")
        return None
    else:
        return int(user_input)

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount/10
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Units Processed : " + str(total_units))
    print("Number of Failed/Rejected Entries : " + str(failed_attempts))

while True:
    clean_input = valid_input()
    if clean_input == "quit":
        break
    elif clean_input == None :
        error_count += 1
    else:
        success_count += 1
        inventory = process_delivery(inventory,clean_input)
    if inventory > 500:
        print ("Alert! Product has been overstocked!")
        break
generate_report(inventory,error_count)