#Sample Standard deviation calculator
Greatings = input(
  "Hello! Welcome to Compute Sample SD! \n\nType Start to begin. ")
sum_of_x_minus_mean = input(
  "What is the value of your sum of X minus mean squared (X-Xbar)² ?\n ")
number_of_samples = input("How many samples do you have in your study?\n")
#Float Conversion
float_sum_of_x_minus_mean = float(sum_of_x_minus_mean)
float_number_of_samples = float(number_of_samples)
Degrees_of_freedom = float_number_of_samples - 1
#Compute the Variance
Variance = float_sum_of_x_minus_mean / Degrees_of_freedom
import math
#Compute Standard Deviation
Standard_deviation = math.sqrt(Variance)
str_Standard_deviation = str(Standard_deviation)
print("\nCongratulations!!\nThe sandard deviation of your sample is:\n" +
      str_Standard_deviation)
Variance_value = input("\nWould you like to get the value of the variance? Type YES to proceed ")
print(Variance)