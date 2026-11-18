from db_config import connect
def create_account():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    balance=float(input("Enter initial balance: "))
    db=connect()
    cursor=db.cursor()
    sql='INSERT INTO accounts (name, email, balance) VALUES (%s,%s,%s)'
    values=(name,email,balance)
    cursor.execute(sql,values)
    db.commit()
    print("Account created successfully.")
    db.close()


def view_accounts():
    db=connect()
    cursor=db.cursor()
    cursor.execute("SELECT * FROM accounts")
    accounts=cursor.fetchall()
    print("\nAccount Details:")
    for account in accounts:
        print(f"Account ID: {account[0]}, Name: {account[1]}, Email: {account[2]}, Balance: {account[3]}")
    db.close()


def deposit_money():
    acc_id = int(input("Enter account ID:"))
    db = connect()
    cursor = db.cursor()

   
    cursor.execute("SELECT id FROM accounts WHERE id=%s", (acc_id,))
    result = cursor.fetchone()

    if result is None:
        print("Account ID does not exist!")

    else:
        amount = float(input("Enter amount to deposit:"))

        if amount <= 0:
            print("Please enter a valid amount.")

        else:
            cursor.execute(
                "UPDATE accounts SET balance = balance + %s WHERE id = %s",
                (amount, acc_id)
            )

            db.commit()
            print("Amount deposited successfully.")

    cursor.close()
    db.close()



def withdraw_money():
    acc_id = int(input("Enter account ID:"))

    db = connect()
    cursor = db.cursor()

    
    cursor.execute("SELECT balance FROM accounts WHERE id=%s", (acc_id,))
    result = cursor.fetchone()

    if result is None:
        print("Account ID does not exist!")

    else:
       
        balance = result[0]

        
        amount = float(input("Enter amount to withdraw:"))

        if amount <= 0:
            print("Please enter a valid amount.")

        elif balance >= amount:
            cursor.execute(
                "UPDATE accounts SET balance = balance - %s WHERE id = %s",
                (amount, acc_id)
            )
            db.commit()
            print("Amount withdrawn successfully.")

        else:
            print("Insufficient balance.")

    cursor.close()
    db.close()



def check_balance():
    acc_id=int(input("Enter account ID:"))
    db=connect()
    cursor=db.cursor()
    cursor.execute("SELECT name, balance FROM accounts WHERE id=%s",(acc_id,))
    balance = cursor.fetchone()
    if balance:
        print(f"Account Holder: {balance[0]}, Current Balance: {balance[1]}")
    else:
        print("Account not found.")
    db.close()
