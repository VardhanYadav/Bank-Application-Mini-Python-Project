users = ['vardhan', 'priya', 'selvaraj'] pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0 print('*****************************************') print("WELCOME TO THE BANK FACILITY OF AXIS BANK")
print('*****************************************') while True:
user = input('\nENTER USER NAME: ') user = user.lower()
if user in users:
if user == users[0]: count = 0
elif user == users[1]: count = 1
else:
count = 2 break
else:
print('INVALID USERNAME')

while count < 3:
pin = input('PLEASE ENTER PIN: ')
if pin.isdigit():
if user == 'vardhan': if pin == pins[0]:
break else:
count += 1 print('INVALID PIN')

if user == 'priya': if pin == pins[1]:
break else:
count += 1 print('INVALID PIN')

if user == 'selvaraj': if pin == pins[2]:
break else:
count += 1 print('INVALID PIN')
else:
 
print('PIN CONSISTS OF 4 DIGITS')
count += 1

if count == 3:
print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING') print('!!!!!YOUR ACCESS HAS BEEN DETAINED!!!!!')
exit()

print('LOGIN SUCCESFUL, CONTINUE')
print(str.capitalize(users[count]), 'WELCOME TO THE AXIS BANK')

while True:
response = input('SELECT FROM FOLLOWING OPTIONS: \n1. Statement (S) \n2. Withdraw AMOUNT (W)	\n3. DEPOSIT AMOUNT (D)\n4. APPLY FOR LOAN (L)\n5. APPLY FOR CREDIT/DEBIT CARD	(A)\n6. CHANGE ATM PIN (P) \n7.
QUIT (Q)\nType The Letter Of Your Choices: ').lower() valid_responses = ['s', 'w','d','l','a','p', 'q'] response = response.lower()
if response == 's': print(str.capitalize(users[count]), 'YOU HAVE ',
amounts[count],'RUPEES ON YOUR ACCOUNT.')

elif response == 'w':
cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
if cash_out%100 != 0:
print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 100 RUPEES
 
NOTES')
 

elif cash_out > amounts[count]: print('YOU HAVE INSUFFICIENT BALANCE')
else:
amounts[count] = amounts[count] - cash_out
print('YOUR NEW BALANCE IS: ', amounts[count], 'RUPEES')
 
elif response =='d':
cash_in=int(input("ENTER THE AMOUNT FOR THE DEPOSIT:")) if cash_in%5!=0:
print('AMOUNT SHOULD BE GREATER FOR THE DEPOSITS OR TO MATCH WITH
10 RUPEE NOTES')
else:
amounts[count]=amounts[count]+cash_in
print('YOUR NEW BALANCE IS:',amounts[count],'RUPEES') elif response=='l':
print("CURRENT LOAN FACILITY FOR THE MONTHLY BASED WITH A RATE OF 5%") loan=input("DO YOU WANT TO APPLY FOR THE LOAN: Y/N: ")
valid_back=['y','n'] loan=loan.lower()
if loan=='n':
print("THANK FOR SHOWING INTEREST")
else:
rate=2
 

"))
 
time=int(input("ENTER FOR HOW MANY MONTHS DO YOU WANT TO APPLY:

EMI=(amounts[count])*(rate)*((1+rate)**time/(1+rate)**time-1) amounts[count]=amounts[count]+EMI
print("YOUR EMI ON YOUR LOAN WITH INTEREST WILL
 
BE",amounts[count],"RUPEE") elif response=='a':
print('PLEASE PRESS' ,"'c'",'TO APPLY CREDIT CARD\n') print('PLEASE PRESS', "'d",'TO APPLY FOR DEBIT CARD') op=input("ENTER YOUR CHOICE: ")
options=['c','d'] op=op.lower()
if op=='c':
p=input("ENTER THE CREDENTIALS FOR APPLICATION") f=input("ENTER YOUR NAME: ")
g=input("ENTER YOUR ACCOUNT NUMBER: ") h=input("ENTER YOUR BRANCH NAME: ")
print("YOUR NAME IS",f,"AND YOUR ACCOUNT NUMBER IS",g,"AND YOUR BRANCH NAME IS",h)
j=input("DO YOU WANT TO MAKE ANY CHANGES (Y/N): ")
op2=['y','n'] j=j.lower() if(j=='y'):
q=input("ENTER YOUR NAME: ") w=input("ENTER YOUR ACCOUNT NUMBER: ") e=input("ENTER YOUR BRANCH NAME: ")
print("YOUR NAME IS",q,"AND YOUR ACCOUNT NUMBER IS",w,"AND YOUR BRANCH NAME IS",e)
print("YOUR CREDIT CARD APPLICATION HAS BEEN SUBMITTED") print("THANK YOU")
else:
print("YOUR CREDIT CARD APPLICATION HAS BEEN SUBMITTED") print("THANK YOU")
else:
p=input("ENTER THE CREDENTIALS FOR APPLICATION") r=input("ENTER YOUR NAME: ")
t=input("ENTER YOUR ACCOUNT NUMBER: ") y=input("ENTER YOUR BRANCH NAME: ")
print("YOUR NAME IS",r,"AND YOUR ACCOUNT NUMBER IS",t,"AND YOUR BRANCH NAME IS",y)
u=input("DO YOU WANT TO MAKE ANY CHANGES (Y/N): ")
op3=['y','n'] op=op.lower() if(op3=='y'):
v=input("ENTER YOUR NAME: ") b=input("ENTER YOUR ACCOUNT NUMBER: ") n=input("ENTER YOUR BRANCH NAME: ")
print("YOUR NAME IS",v,"AND YOUR ACCOUNT NUMBER IS",b,"AND YOUR BRANCH NAME IS",n)
print("YOUR DEBIT CARD APPLICATION HAS BEEN SUBMITTED")
print("THANK YOU")
else:
print("YOUR DEBIT CARD APPLICATION HAS BEEN SUBMITTED") print("THANK YOU")

elif response == 'p':
new_pin = input('ENTER A NEW PIN: ') if(len(new_pin) != 4):
print("YOUR NEW PIN MUST BE OF 4 DIGITS")
new_ppin = int(input('ENTER A NEW PIN: ')) new_pppin=int(input('CONFIRM YOUR PIN: ')) if (new_pppin != new_ppin):
print('PIN MISMATCH')
else:
pins[count]=new_ppin print('NEW PIN SAVED')
elif(len(new_pin)==4): pin2=input("CONFIRM YOUR PIN: ")
if(new_pin==pin2): pins[count] = new_pin print('NEW PIN SAVED')
else:
print('PIN MISMATCHED')
else:
print('ERROR OCCURANCE')
elif response == 'q': print('Thank You')
else:
print('RESPONSE NOT VALID')
break

 
 
 
