#Leonardo
#TP064705


from datetime import datetime as dat
import os

# to get now time = print(dat.now().time())
# to get now date = print(dat.now().date())

#generates admin and customer id number
def generate_id(type):
    with open("id.txt", "r") as f:
        record = f.readline()
        reclist = record.strip().split(":")
        if type == "admin":
            id = "admn"
            oldrecord = reclist[0][4:]
        elif type == "customer":
            id = "cust"
            oldrecord = reclist[1][4:]
        nextrecord = int(oldrecord) + 1
    if len(str(nextrecord)) == 1:
        newid = "0" * 3 + str(nextrecord)
    if len(str(nextrecord)) == 2:
        newid = "0" * 2 + str(nextrecord)
    if len(str(nextrecord)) == 3:
        newid = "0" + str(nextrecord)
    if len(str(nextrecord)) == 4:
        newid = str(nextrecord)
    final_id = id + newid
    if type == "admin":
        reclist[0] = final_id
    elif type == "customer":
        reclist[1] = final_id
    rec = ":".join(reclist)
    with open("id.txt", "w") as f:
        f.write(rec)
    return final_id

#display existing account in data file
def display_account():
    with open("account.txt", "r")as f:
        print("-" * 80)
        print("User ID: ".center(20) + "| User password: ".center(20) + "| User name: ".center(16) + "| acc type: ".center(23) + "| date created: \n")
        for i in f:
            record = i.strip().split(",")
            if record[3] == "1":
                record[3] = "superuser"
            elif record[3] == "2":
                record[3] = "admin"
            elif record[3] == "3":
                record[3] = "customer"
            print(record[0].center(20) , "|" , record[1].center(17) , "|" , record[2].center(18) , "|" , record[3].center(14) , "|" , record[4].center(15))

#func to creates a new admin account
def add_admin():
    user_id = generate_id("admin")
    print("User ID :", user_id)
    while True:
        userpass = input("Create admin password (min 6 characters): ")
        if len(userpass) >= 6:
            break
    print("User Password:",userpass)
    usrname = input("Please enter admin name: ")
    print("Admin name:", usrname)
    print("admin account created")
    acctype = "2"
    with open("account.txt","a") as fh:
        rec = "\n" + user_id + "," + userpass + "," + usrname + "," + acctype + "," + dat.now().date().strftime("%Y-%m-%d")
        fh.write(rec)

#login for all accounts
def login():
    print("*" * 20 + " Banking System " + "*" * 20 )
    print("welcome, \u0001\u0001\u0001")
    print("-" * 80)
    print("Enter 'q' to exit from system")
    user_id = input("Enter your name: ")
    if user_id == "q" or user_id == "Q":
        quit()
    user_password = input("Enter your password: ")
    with open("account.txt", "r") as f:
        record = "no"
        for i in f:
            record_list = i.strip().split(",")
            if record_list[2] == user_id and record_list[1] == user_password:
                record = record_list
                break
        if record == "no":
            print("Incorrect name or password!")
        else:
            print("successful login!!!")
    print("-" * 80)
    return record

#func to creates a new customer account
def add_customer():
    cust_id = generate_id("customer")
    print("User ID: ", cust_id)
    while True:
        password = input("Create customer password (min 6 characters): ")
        if len(password) >= 6:
            break
    print("User password: ", password)
    cust_name = input("please enter customer name: ")
    print("user name: ", cust_name)
    print("C for current, S for saving")
    while True:
        acc_type = input("customer account type: ")
        if acc_type == "c" or acc_type == "C":
            break
        elif acc_type == "s" or acc_type == "S":
            break
        else:
            print("is it current acc or saving acc??")
    if acc_type == "c" or acc_type == "C":
        while True:
            try:
                balance = float(input("inital balance (min 500 RM): "))
                if balance >999:
                    print("wow!!! rich client !!! \U0001F600\U0001F600\U0001F600")
                    break
                elif balance >= 500:
                    break
                else:
                    print("initial balance must be at least 500 RM")
            except:
                print("Invalid input")
    elif acc_type == "s" or acc_type == "S":
        while True:
            try:
                balance = float(input("inital balance (min 100 RM): "))
                if balance >999:
                    print("wow!!! rich client !!! \U0001F600\U0001F600\U0001F600")
                    break
                elif balance >= 100:
                    break
                else:
                    print("initial balance must be at least 100 RM")
            except:
                print("Invalid input")
    with open("customer.txt", "a") as f:
        rec = "\n" + cust_id + "," + cust_name + "," + acc_type + "," + str(balance) + "," + str(dat.now().date())
        f.write(rec)
    with open("history.txt", "a") as x:
        rec = "\n" + cust_id + "," + cust_name + "," + str(balance) + ", +" + str(balance) + "," + str(dat.now().date()) + "," + str(dat.now().time().strftime("%H:%M:%S"))
        x.write(rec)
    print("Customer account created")
    accounttype = "3"
    with open("account.txt", "a") as f:
        rec = "\n" + cust_id+","+password+","+cust_name+","+accounttype +","+ str(dat.now().date())
        f.write(rec)

#to change account password
def change_password(details):
    all = []
    with open("account.txt", "r") as f:
        for i in f:
            allist = i.strip().split(",")
            all.append(allist)
    while True:
        new_password = input("Please enter your new password (min 6 characters): ")
        if len(new_password) >= 6:
            print(f"customer id: {details[0]}")
            print("password changed into: " + new_password + "!!!")
            break
    cnt = -1
    flg = len(all)
    for i in range(0, flg):
        if details[0] == all[i][0]:
            cnt = i
            break
    all[cnt][1] = new_password
    with open("account.txt", "w") as f:
        flg = len(all)
        for i in range(0, flg):
            record = ",".join(all[i])+ "\n"
            f.write(record)

#for admin to change customer password
def change_cust_password():
    while True:
        print("Warning!!! we will log you out in case of invalid id!")
        ans = input("customer id: ")
        if "cust" in ans:
            break
        else:
            print("please enter customer id!!!")
    all = "no"
    with open("account.txt", "r") as f:
        for i in f:
            allist = i.strip().split(",")
            if ans == allist[0]:
                all = allist
    if all == "no":
        print("invalid id")
        print("we will log you out now \U0001F612\U0001F612\U0001F612")
        main()
    return all

#for admin to display account report
def admin_display_report():
    while True:
        print("Warning!!! we will log you out in case of invalid id!")
        ans = input("customer id: ")
        if "cust" in ans:
            break
        else:
            print("please enter customer id!!!")
    all = "no"
    with open("account.txt", "r") as f:
        for i in f:
            allist = i.strip().split(",")
            if ans == allist[0]:
                all = allist
    if all == "no":
        print("invalid id")
        print("we will log you out now \U0001F612\U0001F612\U0001F612")
        main()
    return all

#superuser menu
def superuser():
    while True:
        print("-" * 80)
        print("SUPERUSER")
        print("-" * 80)
        print("1. create admin account\n2. create customer account\n3. display all existing account\n4. logout")
        while True:
            try:
                answer = int(input("Enter choice: "))
                if answer > 4 or answer == 0:
                    print("Please enter a valid number!!!")
                if answer <= 4:
                    break
            except:
                print("please enter a number!!!")
        if answer == 4:
            break
        elif answer == 1:
            add_admin()
        elif answer == 2:
            add_customer()
        elif answer == 3:
            display_account()
        print("-" * 80)

#admin menu
def admin(record):
    while True:
        print("-" * 80)
        print("ADMIN")
        print("-" * 80)
        print("1. create customer account\n2. change password\n3. change customer password\n4. generates customer report\n5. logout")
        while True:
            try:
                answer = int(input("Enter choice: "))
                if answer > 5 or answer == 0:
                    print("Please enter a valid number!!!")
                if answer <= 5:
                    break
            except:
                print("Please enter a number!!!")
        if answer == 5:
            break
        elif answer == 1:
            add_customer()
        elif answer == 2:
            change_password(record)
        elif answer == 3:
            rec = change_cust_password()
            change_password(rec)
        elif answer == 4:
            rec = admin_display_report()
            acc_report(rec)
        print("-" * 80)

def determine_customer_account(rec):
    record = False
    with open("customer.txt", "r") as f:
        for i in f:
            record_list = i.strip().split(",")
            if rec[0] == record_list[0]:
                record = record_list
                break
    return record[2]

#customer menu
def customer(record):
    while True:
        acc_type = determine_customer_account(record)
        print("-" * 80)
        print("Customer")
        print("-" * 80)
        print("1. withdraw\n2. deposit\n3. change password\n4. generates account report\n5. check balance\n6. logout")
        while True:
            try:
                answer = int(input("Enter choice: "))
                if answer > 6 or answer == 0:
                    print("Please enter a valid number!!!")
                if answer <= 6:
                    break
            except:
                print("Please enter a number!!!")
        if answer == 6:
            break
        elif answer == 5:
            check_balance(record)
        elif answer == 3:
            change_password(record)
        elif answer == 4:
            acc_report(record)
        elif acc_type == "s" or acc_type == "S":
            balance_change_saving(record, answer)
        elif acc_type == "c" or acc_type == "C":
            balance_change_current(record, answer)

#for current type customer
def balance_change_current(record, ans):
    print("-" * 80)
    all = []
    with open("customer.txt", "r") as f:
        for i in f:
            allist = i.strip().split(",")
            all.append(allist)
    cnt = -1
    flg = len(all)
    for i in range(0, flg):
        if record[0] == all[i][0]:
            cnt = i
            break
    balance = float(all[cnt][3])
    if ans == 1:
        while True:
            withdraw= float(input("how much do you want to withdraw: "))
            next_balance = balance - withdraw
            if next_balance >= 500:
                print(f"you have withdraw {withdraw}")
                with open("history.txt","a") as fh:
                    rec = "\n" + record[0] + "," + record[2] + "," + str(balance) + ", - " + str(withdraw)  + "," + str(dat.now().date()) + "," + str(dat.now().time().strftime("%H:%M:%S"))
                    fh.write(rec)
                break
            else:
                print("insufficient balance to withdraw")
    if ans == 2:
        while True:
            deposit= float(input("how much do you want to deposit: "))
            next_balance = balance + deposit
            if next_balance >= 500:
                print(f"you have deposit {deposit}")
                with open("history.txt","a") as fh:
                    rec = "\n" + record[0] + "," + record[2] + "," + str(balance) + ", + " + str(deposit)  + "," + str(dat.now().date()) + "," + str(dat.now().time().strftime("%H:%M:%S"))
                    fh.write(rec)
                break
            else:
                print("invalid input")
    cnt = -1
    flg = len(all)
    for i in range(0, flg):
        if record[0] == all[i][0]:
            cnt = i
            break
    all[cnt][3] = str(next_balance)
    with open("customer.txt", "w") as f:
        flg = len(all)
        for i in range(0, flg):
            record = ",".join(all[i])+ "\n"
            f.write(record)

#for saving type customer
def balance_change_saving(record, ans):
    print("-" * 80)
    all = []
    with open("customer.txt", "r") as f:
        for i in f:
            allist = i.strip().split(",")
            all.append(allist)
    cnt = -1
    flg = len(all)
    for i in range(0, flg):
        if record[0] == all[i][0]:
            cnt = i
            break
    balance = float(all[cnt][3])
    if ans == 1:
        while True:
            withdraw= float(input("how much do you want to withdraw: "))
            next_balance = balance - withdraw
            if next_balance >= 100:
                print(f"you have withdraw {withdraw}")
                with open("history.txt","a") as fh:
                    rec = "\n" + record[0] + "," + record[2] + "," + str(balance) + ", - " + str(withdraw)  + "," + str(dat.now().date()) + "," + str(dat.now().time().strftime("%H:%M:%S"))
                    fh.write(rec)
                break
            else:
                print("insufficient balance to withdraw")
    if ans == 2:
        while True:
            deposit= float(input("how much do you want to deposit: "))
            next_balance = balance + deposit
            if next_balance >= 100:
                print(f"you have deposit {deposit}")
                with open("history.txt","a") as fh:
                    rec = "\n" + record[0] + "," + record[2] + "," + str(balance) + ", + " + str(deposit)  + "," + str(dat.now().date()) + "," + str(dat.now().time().strftime("%H:%M:%S"))
                    fh.write(rec)
                break
            else:
                print("invalid input")
    cnt = -1
    flg = len(all)
    for i in range(0, flg):
        if record[0] == all[i][0]:
            cnt = i
            break
    all[cnt][3] = str(next_balance)
    with open("customer.txt", "w") as f:
        flg = len(all)
        for i in range(0, flg):
            record = ",".join(all[i])+ "\n"
            f.write(record)

#for current type customer
def check_balance(record):
    reclist = []
    
    with open("customer.txt", "r") as f:
        for i in f:
            rec = i.strip().split(",")
            if record[0] == rec[0]:
                reclist = rec
    print(f"your balance is : {reclist[3]} RM")

def acc_report(record):
    reclist = []
    with open("history.txt", "r")as f:
        for i in f:
            rec = i.strip().split(",")
            if record[0] == rec[0]:
                reclist.append(rec)
    print("user id: ".center(15)+"| user name:".center(22)+"| prev balance: ".center(23)+"| balance change: ".center(21)+"| date: ".center(12)+"| time: ".center(30))
    print("-" * 120)
    with open("history.txt", "r")as f:
        for i in f:
            rec = i.strip().split(",")
            if record[0] == rec[0]:
                print(rec[0].center(20)+"|"+rec[1].center(20)+"|"+rec[2].center(20)+"|"+rec[3].center(20)+"|"+rec[4].center(20)+"|"+rec[5].center(20))
#Main Logic:
def main():
    while True:
        record = login()
        if record != "no":
            print("welcome", record[2], "\U0001F600\U0001F600\U0001F600 \4\4\4")
            print(f"login successful at {dat.now().date()} time: {dat.now():%H:%M:%S}")
            if record[3] == "1":
                superuser()
            elif record[3] == "2":
                admin(record)
            elif record[3] == "3":
                customer(record)
        else:
            print("login failed")
        try:
            print("-" * 80)
            ans = input("enter any key to try again\nenter 'q' to exit\nchoice: ")
            if ans == "q" or ans == "Q":
                break
        except:
            pass

main()