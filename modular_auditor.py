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

while True:
    clean_input = valid_input()
    if clean_input == "quit":
        break
    elif clean_input == None :
        error_count += 1
    else:
        success_count += 1
        inventory += int(clean_input)
    if inventory > 500:
        print ("Alert! Product has been overstocked!")
        break
print("Total Units Processed : " + str(inventory))
print("Number of Failed/Rejected Entries : " + str(error_count))