bill_amount = float(input('The Total Bill Amount:$'))
level_of_service = (input('Level Of Service :'))
tip_amount = float()

if (level_of_service == 'good'):
    tip_amount = bill_amount * .2
    print('Tip Amount : ' ,tip_amount)
elif( level_of_service =='fair'):
    tip_amount = bill_amount * .15
    print('Tip Amount : ', tip_amount)
elif(level_of_service == 'bad'):
    tip_amount = bill_amount *.10
    print('Tip Amount : ' ,tip_amount)
else:
    print('')
total_amount = float(bill_amount + tip_amount)
print('Total Amount:' ,total_amount)
