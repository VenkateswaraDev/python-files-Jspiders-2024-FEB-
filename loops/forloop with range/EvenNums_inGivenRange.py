# Find even number in between the given range
# Taking starting and ending range values from the user by using input 
start_range = int(input("Enter a starting range number = "))
end_range = int(input("Enter a ending range number = "))
for i in range(start_range,end_range+1):
    if i%2==0:
        print(i)
