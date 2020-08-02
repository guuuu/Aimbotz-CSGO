import os
import pymysql as sql
import sys
import datetime
from datetime import date

def clear(): return os.system('cls')

clear()

def connect():
    clear()
    try:
        #print("Connecting...")
        conn = sql.connect(host="localhost", user="root", passwd="", database="aimbotz", autocommit=True)
        cursor = conn.cursor()

        #if conn:
            #print("Connection sucessfull...")

        return {"connection": conn, "cursor": cursor}
    except Exception as ex:
        input(f"There was an error connecting to the database\n{ex}")
        qquit()

def insert():
    bd = connect()
    aux = 0
    avg = 0
    best = 999999
    worst = 0
    total_times = ""

    print("Note: Insert the times in seconds only")
    while True:
        try:
            qt = int(input("How many times have you played - "))

            if isinstance(qt, int) and qt > 0:
                break
            else:
                continue
        except:
            pass

    for i in range(qt):
        while True:
            try:
                new_time = int(input(f"Time for round number {i + 1} - "))
                if new_time > 0:
                    break
                else:
                    continue
            except:
                pass

        aux += int(new_time)
        total_times += str(new_time) + "/"
        best = new_time if new_time < best else best
        worst = new_time if new_time > worst else worst
    avg = round(aux / qt, 0)
    total_times = total_times[:-1]

    query = f"INSERT INTO times(d, t, a, bt, wt) VALUES('{date.today()}', '{str(total_times)}', '{str(avg)}', '{str(best)}', '{str(worst)}')"

    if bd["connection"].open:
        print("Still connected to the database...")
        print("Trying to insert the data...")
    else:
        print("Connection to the database lost...")
        print("Data not inserted...")
        qquit()

    cursor = bd["cursor"]
    cursor.execute(str(query))
    cursor.close()
    bd["connection"].commit()
    bd["connection"].close()

    print("Data inserted sucessfully")
    input("Press any key to go back to the menu...")
    menu()

def global_status():
    bd = connect()
    total_times = 0
    ba = 0
    wa = 0
    bt = 0
    wt = 0
    day_of_ba = None
    day_of_bt = None
    day_of_wa = None
    day_of_wt = None
    times = []

    query = "SELECT d, a FROM times ORDER BY a ASC LIMIT 1"

    bd["cursor"].execute(str(query))
    results = bd["cursor"].fetchall()

    for r in results:
        ba = r[1]
        day_of_ba = r[0]

    query = "SELECT d, a FROM times ORDER BY a DESC LIMIT 1"

    bd["cursor"].execute(str(query))
    results = bd["cursor"].fetchall()

    for r in results:
        wa = r[1]
        day_of_wa = r[0]     

    query = "SELECT d, bt FROM times ORDER BY bt ASC LIMIT 1"

    bd["cursor"].execute(str(query))
    results = bd["cursor"].fetchall()

    for r in results:
        bt = r[1]
        day_of_bt = r[0]

    query = "SELECT d, wt FROM times ORDER BY wt DESC LIMIT 1"

    bd["cursor"].execute(str(query))
    results = bd["cursor"].fetchall()

    for r in results:
        wt = r[1]
        day_of_wt = r[0]

    query = "SELECT t FROM times"

    bd["cursor"].execute(str(query))
    results = bd["cursor"].fetchall()

    for r in results:
        for i in r[0].split("/"):
            times.append(int(i))

    print(
        f"<==========Global status==========>\n"
        +f"You've played a total of {len(times)} rounds\n"
        +f"Your best time is => {bt} in {day_of_bt}\n"
        +f"Your worst time is => {wt} in {day_of_wt}\n"
        +f"Your best average is => {ba} in {day_of_ba}\n"
        +f"Your worst average is => {wa} in {day_of_wa}\n"
        +f"You spent {round(((sum(times) / 60) / 60), 2)} hours of your life playing AimBotz"
    )
    
    bd["connection"].commit()
    bd["cursor"].close()
    bd["connection"].close()

    input("Press any key to go back to the menu...")
    menu()    

def best_time():
    __bt = 0
    __day_of_bt = None
    bd = connect()
    query = "SELECT d, bt FROM times ORDER BY bt ASC LIMIT 1"

    bd["cursor"].execute(str(query))
    results = bd["cursor"].fetchall()

    for r in results:
        __bt = r[1]
        __day_of_bt = r[0]

    print(f"Your best time is => {__bt} in {__day_of_bt}")
    input("Press any key to go back to the menu...")
    menu()    

def best_average_time():
    __a = 0
    __day_of_a = None
    bd = connect()
    query = "SELECT d, a FROM times ORDER BY a ASC LIMIT 1"

    bd["cursor"].execute(str(query))
    results = bd["cursor"].fetchall()

    for r in results:
        __a = r[1]
        __day_of_a = r[0]

    print(f"Your best average time is => {__a} in {__day_of_a}")
    input("Press any key to go back to the menu...")
    menu()    

def worst_time():
    __wt = 0
    __day_of_wt = None
    bd = connect()
    query = "SELECT d, wt FROM times ORDER BY wt DESC LIMIT 1"

    bd["cursor"].execute(str(query))
    results = bd["cursor"].fetchall()

    for r in results:
        __wt = r[1]
        __day_of_wt = r[0]

    print(f"Your worst time is => {__wt} in {__day_of_wt}")
    input("Press any key to go back to the menu...")
    menu()    

def worst_average_time():
    __a = 0
    __day_of_a = None
    bd = connect()
    query = "SELECT d, a FROM times ORDER BY a DESC LIMIT 1"

    bd["cursor"].execute(str(query))
    results = bd["cursor"].fetchall()

    for r in results:
        __a = r[1]
        __day_of_a = r[0]

    print(f"Your worst average time is => {__a} in {__day_of_a}")
    input("Press any key to go back to the menu...")
    menu()    

def times_of_day():
    bd = connect()
    date = None
    times = []
    a = 0
    bt = 0
    wt = 0

    while True:
        try:
            date = datetime.datetime.strptime(input("Wich day you want to check - "), '%Y-%m-%d')
            break
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    query = f"SELECT * FROM times WHERE d = '{str(date)}'"
    #query = f"SELECT * FROM times WHERE d = '2020-08-01'"

    bd["cursor"].execute(str(query))
    results = bd["cursor"].fetchall()

    for row in results:
        for time in row[2].split('/'):
            times.append(time)
        a = row[3]
        bt = row[4]
        wt = row[5]

    print(f"Times played {len(times)}")

    for i in range(len(times)):
        print(f"Round {i+1} => {times[i]}")

    print(f"Average => {a}")
    print(f"Best time => {bt}")
    print(f"Worst time => {wt}")


    bd["connection"].commit()
    bd["cursor"].close()
    bd["connection"].close()

    input("Press any key to go back to the menu...")
    menu()    

def qquit():
    sys.exit(0)

def menu():
    clear()

    options ={
        1: insert,
        2: global_status,
        3: best_time,
        4: best_average_time,
        5: worst_time,
        6: worst_average_time,
        7: times_of_day,
        0: qquit
    }

    print("1 - Insert times")
    print("2 - Global stats")
    print("3 - Best time")
    print("4 - Best average time")
    print("5 - Worst time")
    print("6 - Worst average time")
    print("7 - Times of certain day")
    print("0 - Quit")

    while True:
        op = input("Choose an option from the menu - ")
        try:
            if int(op) >= 0 and int(op) <= 7:
                break
            else:
                continue
        except Exception as ex:
            pass

    options[int(op)]()

menu()