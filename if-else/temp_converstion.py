# temp convertion

print('''
      ------Temparature converter--------
        1. convert temparature in F.heat
        2. convert temparature in C 
      '''
      )
option = int(input("Select any option from above = "))
if option == 1:
    ctemp = int(input("Enter temparature = "))
    ftemp = (((9/5)*ctemp)+32)
    print(f"converted temparature in F.heat is {ftemp}")
else:
    fa_temp = int(input("Enter temparature = "))
    c_temp = ((5/9)*(fa_temp-32))
    print(f"converted temparature in C is {c_temp}")