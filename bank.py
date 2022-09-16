import pymysql
import time

def staff_login(s_id):
db = pymysql.connect(host="localhost", user="root", passwor
d="root", database="school")
cu = db.cursor()
password = int(input("Enter your staff password: "))
query = 'select password from STAFF where id=%s'
cu.execute(query, (s_id))
t_pass = cu.fetchall()[0][0]
db.close()
if t_pass == password:
print("LOGIN SUCCESSFUL!")
return True
else:
print("LOGIN UNSUCCESSFUL")
return False

def register_acc():
db = pymysql.connect(host="localhost", user="root", passwor
d="root", database="school")
cu = db.cursor()
print("Fill these details to register your account")

acc_no = str(int(time.time()))
name = input("Enter your name: ")
password = int(input("Enter a 8 digit password: "))
status = "active"
acc_type = input("Enter account type < saving/current > : ")
age = int(input("Enter your age: "))
gender = input("Enter your sex <M/F> : ")
email = input("enter your email: ")
mob_no = input("Enter your 10 digit contact number: ")
add = input("Enter your address: ")
adh_no = input("Enter your 12 digit aadhar number: ")
bal = float(input("Enter your account balance: "))
t_insert = 'insert into CUSTOMERS values (%s,%s,%s,%s,%s,%s
,%s,%s,%s,%s,%s,%s)'
value = (acc_no, name, password, status, acc_type, age, gend
er, email, mob_no, add, adh_no, bal)
cu.execute(t_insert, value)
print("Your Account no is", acc_no)
print("Thank you for joining us! :D ")
db.commit()
db.close()

def cust_login(account_no):
db = pymysql.connect(host="localhost", user="root", passwor
d="root", database="school")
cu = db.cursor()
password = int(input("Enter your password: "))

query = 'select password from CUSTOMERS where acc_no =%
s '
cu.execute(query, (account_no))
t_pass = cu.fetchall()[0][0]
db.close()
if t_pass == password:
print("LOGIN SUCCESSFUL!")
return True
else:
print("LOGIN UNSUCCESSFUL.Try Again")
return False

def acc_status(account_no):
db = pymysql.connect(host="localhost", user="root", passwor
d="root", database="school")
cu = db.cursor()
query = 'select status, bal from CUSTOMERS where acc_no =
%s '
result = cu.execute(query, (account_no))
result = cu.fetchone()
db.close()
return result

def cust_deposit(account_no, amount):
db = pymysql.connect(host="localhost", user="root", passwor
d="root", database="school")
cu = db.cursor()
result = acc_status(account_no)

if result[0] == "active":
query = 'update CUSTOMERS set bal = bal + %s where acc_
no =%s '
cu.execute(query, (amount, account_no))
print("AMOUNT DEPOSITED")
else:
print("Closed or Suspended account")
db.close()

def cust_withdraw(account_no, amount):
db = pymysql.connect(host="localhost", user="root", passwor
d="root", database="school")
cu = db.cursor()
result = acc_status(account_no)
if result[0] == "active" and int(result[1]) >= int(amount):
query =

' update CUSTOMERS set bal = bal - %s where acc_

no =%s '
cu.execute(query, (amount, account_no))
print("AMOUNT WITHDRAWN ")
else:
print("Closed or Suspended account or Insufficient balance
")
db.close()

def account_details(account_no):
db = pymysql.connect(host="localhost", user="root", passwor
d="root", database="school")
cu = db.cursor()

query =

' select * from CUSTOMERS where acc_no =%s '

cu.execute(query, (account_no))
result = cu.fetchone()
print("||ACCOUNT DETAILS||")
print('-' * 120)
print("Account no. :", result[0])
print("Customer Name :", result[1])
print("Status :", result[3])
print("Account type :", result[4])
print("Age :", result[5])
print("Gender :", result[6])
print("Email ID :", result[7])
print("Mobile no. :", result[8])
print("Address :", result[9])
print("Adhar no. :", result[10])
print("Balance :", result[11])
print('-' * 120)
cu.close()

def modify_account(account_no):
db = pymysql.connect(host="localhost", user="root", passwor
d="root", database="school")
cu = db.cursor()
print("||MODIFICATION OPTIONS||")
print("1. Customer Name")
print("2. Customer Age")
print("3. Customer Email ID")
print("4. Customer Mobile no.")

print("5. Customer Address")
print("6. Customer Password")
print("\n")
choice = input("What do you want to change? : ")
if choice == '1':
new_data = input("Enter correction in name: ")
query = 'update CUSTOMERS set name =%s where acc_no
=%s '
cu.execute(query, (new_data, account_no))
elif choice == '2':
new_data = int(input("Enter correct age: "))
query = 'update CUSTOMERS set age =%s where acc_no =%
s '
cu.execute(query, (new_data, account_no))
elif choice == '3':
new_data = input("Enter correction in Email Id : ")
query = 'update CUSTOMERS set email =%s where acc_no =
%s '
cu.execute(query, (new_data, account_no))
elif choice == '4':
new_data = int(input("Enter correction in Mobile no.: "))
query = 'update CUSTOMERS set mob_no =%s where acc_n
o =%s '
cu.execute(query, (new_data, account_no))
elif choice == '5':
new_data = input("Enter correct address: ")
query = 'update CUSTOMERS set addr =%s where acc_no =
%s '
cu.execute(query, (new_data, account_no))

elif choice == '6':
new_data = input("Enter new password: ")
query = 'update CUSTOMERS set password =%s where acc_
no =%s '
cu.execute(query, (new_data, account_no))
print("Customer Information Modified")
db.commit()
db.close()

def close_account(account_no):
db = pymysql.connect(host="localhost", user="root", passwor
d="root", database="school")
cu = db.cursor()
query =

' update CUSTOMERS set status = "closed" where acc

_no =%s '
cu.execute(query, (account_no))
print("Account Closed")
db.close()

def search_menu():
db = pymysql.connect(host="localhost", user="root", passwor
d="root", database="school")
cu = db.cursor()
while True:
print("||Search Menu||")
print("1. Account No.")
print("2. Aadhar No.")
print("3. Mobile No..")

print('\n')
ch = input("Enter your choice: ")
if ch == '1':
account_no = input("Enter customer's account no.: ")
query = 'select * from CUSTOMERS where acc_no =%s'
cu.execute(query, (account_no))
records = cu.fetchall()
n = len(records)
print("Search Result for account no.", account_no, ":")
print('-' * 80)
for record in records:
print(record)
if n <= 0:
print("Account no.", account_no, "does not exist")
elif ch == '2':
adh_no = input("Enter customer's aadhar no.: ")
query = 'select * from CUSTOMERS where adh_no=%s'
cu.execute(query, (adh_no))
records = cu.fetchall()
n = len(records)
print("Search Result for aadhar no.", adh_no, ":")
print('-' * 80)
for record in records:
print(record)
if n <= 0:
print("Aadhar no.", adh_no, "does not exist")
elif ch == '3':
mob_no = input("Enter customer's mobile no.: ")
query = 'select * from CUSTOMERS where mob_no=%s'

cu.execute(query, (mob_no))
records = cu.fetchall()
n = len(records)
print("Search Result for mobile no.", mob_no, ":")
print('-' * 80)
for record in records:
print(record)
if n <= 0:
print("Mobile no.", mob_no, "does not exist")
else:
break
db.close()

def customer_help():
print("Enter your enquiry and mobile number below")
query = input("Enter the problem / issue you are facing durin
g transaction or otherwise :")
mob_no = int(input("Enter your mobile number: "))
print("Our staff will get in touch with you shortly")
print("Or call at our tollfree number - 1808-180-808")

def transaction_menu(account_no):
while True:
print("||Transaction Menu||")
print("1. Deposit Money")
print("2. Withdraw Money")
print("3. Back to main menu")
print("\n")

choice = input("Enter your choice:")
if choice == '1':
amount = float(input("Enter the amount of money you w
ant to deposit: "))
cust_deposit(account_no, amount)
elif choice == '2':
amount = float(input("Enter the amount of money you w
ant to withdraw: "))
cust_withdraw(account_no, amount)
elif choice == '3':
break
else:
print('INVALID OPTION')

def main_menu_staff():
while True:
print("||MAIN MENU||")
print("1.Display Account Details")
print("2.Modify Account Details")
print("3.Close Account")
print("4.Search Menu")
print("5.Close Application")
print("\n")
ch = input("Enter your choice: ")
if ch == '1':
account_no = int(input("Enter customer's account no.: ")
)
account_details(account_no)

elif ch == '2':
account_no = int(input("Enter customer's account no.: ")
)
modify_account(account_no)
elif ch == '3':
account_no = int(input("Enter customer's account no.: ")
)
close_account(account_no)
elif ch == '4':
search_menu()
elif ch == '5':
break
else:
print("INVALID OPTION")

def main_menu_cust():
while True:
print("||MAIN MENU||")
print("1. Display Account Details")
print("2. Transaction Menu")
print("3. Customer Help")
print("4. Close Application")
print('\n')
ch = input("Enter your choice: ")
if ch == '1':
account_details(account_no)
elif ch == '2':
transaction_menu(account_no)

elif ch == '3':
customer_help()
elif ch == '4':
break
else:
print("INVALID OPTION")

print("*" * 120)
print(" Welcome ")
print("Enter as :")
print("\t1.Customer")
print("\t2.Staff Member")
ch1 = input("Enter your choice <1/2> : ")
if ch1 == '1':
print("Are you an: \n1.New Member\n2.Existing member")
ch2 = input("Enter your choice <1/2> : ")
if ch2 == '1':
register_acc()
main_menu_cust()
elif ch2 == '2':
account_no = int(input("Enter your account number linked
with bank: "))
a = cust_login(account_no)
if a == True:
main_menu_cust()
else:
print("INVALID OPTION")

elif ch1 == '2':
s_id = int(input("Enter your staff ID: "))
a = staff_login(s_id)
if a == True:
main_menu_staff()

print('-' * 120)
print(" THANK YOU ")