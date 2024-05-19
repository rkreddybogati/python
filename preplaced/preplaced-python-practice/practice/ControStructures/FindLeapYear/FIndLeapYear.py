
# Write your code here

year = int(input("Enter Year: "))

if year%400==0:
  print('True')
elif year%4==0 and year%100!=0:
  print('True')
else:
  print('False')
  