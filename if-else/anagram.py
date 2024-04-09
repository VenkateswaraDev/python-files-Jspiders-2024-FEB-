# check given strings is anagram or not?
# taking strings from the user
str1 = input('Enter first string = ')
str2 = input('Enter secound string = ')
# convert given strings into lower case and re-assign to same variable
str1=str1.lower()
str2=str2.lower()
# perform sorted function so it can give sorted elements in a list including duplicates
if sorted(str1)==sorted(str2):
    print('Given strings is an anagaram')
else:m
    print("Given strings is not an anagaram")