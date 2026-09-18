inventory = 0
error_count = 0
while True:
   user_input = input("Enter a stock quantity : ")
   if user_input == "quit":
       break
   if user_input.isdigit() == False:
       print("The quantity entered is not a number! Please try again with integers.")
       error_count += 1
       continue
   elif int(user_input)< 0:
       print("The quantity entered is negative! Please try again with a non-negative number")
       err1 += 1
   inventory += int(user_input)
   if inventory > 500:
       print ("Alert! Product has been overstocked!")
       break
print("Total Units Processed : " + str(inventory))
print("Number of Failed/Rejected Entries : " + str(error_count))