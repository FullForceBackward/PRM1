"""
By Winston, ID:16216, G2Y1, NO PLAGIARISING DOGs. 
"""
#Initiallisation
ticket_counting = 0 #total in and out
empty_carports = 100 #avalible carports
used_hours = 0 #total hour used by users
total_taking = 0.0 #total revenue
average_taking = 0.0 #average revenue
average_hour = 0 #average hour per user
data_storage = {} #a dictionary for all tickets and time enter, refresh each day

def time_valid(time):
    if time[0:2] > 24:
        return False
    elif time[2:4] > 60:
        return False
    else:
        return True

def integer_check(num):
    try: 
        num = int(num)
    except:
        return False
    return True

def user_interface():
    if ticket_counting == 0 and empty_carports == 100 and used_hours == 0 and total_taking == 0.0 and average_taking == 0.0 and average_hour == 0:
        print("Initialisation completed")
    if empty_carports == 0:
        print("Sorry, carports full")
    else:
        print("Welcome\n" + "Empty carports left: " + empty_carports)
        type_in = ("Please enter'enter' for entrance, 'exit' for exit")
        if type_in == "enter":
            enter_state()
        elif type_in == "exit":
            exit_state()
        else:
            print("Invalid type in, please type in 'enter' or 'exit'")
            user_interface()
    if empty_carports == 0:
        end_day()
   
def enter_state():
    time_in = input("Please enter current time in form 'xxxx' in 24-hour system")
    if integer_check(time_in) == True and len(time_in) == 3:
        while time_valid(time_in) == False:
            print("invalid time, please check")
            enter_state()
        time_in = int(time_in)
        data_storage[ticket_counting] = [time_in]
        print("Your ticket number is" + ticket_counting + "\n" + "Your time in:" + time_in, end = " ")
        ticket_counting = ticket_counting + 1
        empty_carports = empty_carports - 1
        user_interface()
    else:
        print("Unvalid time input. Please check")
        enter_state()
        
def exit_state():
    global used_hours
    global total_taking
    global empty_carports
    if empty_carports == 100:
        print("no car yet")
    if ticket_counting == 0:
        print("No data stored yet, please go enter.")
    else:
        ticket_number = input("Please enter your ticket number")
        while integer_check(ticket_number) == False or int(ticket_number) not in data_storage:
            print("Invalid ticket number, please check.")
            ticket_number = input("Please enter your ticket number")
        ticket_number = int(ticket_number)
        time_in = data_storage[ticket_number]
        time_out = input("Please enter current time in form 'xxxx' in 24-hour system")
        while integer_check(time_out) == False or len(time_out) != 3 or time_valid(time_out) == False:
            print("Time input not valid, please check.")
            time_out = input("Please enter current time in form 'xxxx' in 24-hour system")
        hours = int(time_out[0:2]) - int(time_in[0:2])
        if time_out[2:4] > time_in[2:4]:
            hours = hours + 1
        used_hours = used_hours + hours
        taking = 1.5 * hours
        total_taking = total_taking + taking
        del data_storage[ticket_number]
        empty_carports = empty_carports + 1
        user_interface()

def end_day():
    global used_hours
    global total_taking
    global ticket_counting
    global empty_carports
    global average_hour
    global average_taking
    global data_storage
    average_hour = used_hours/ticket_counting
    average_taking = total_taking/ticket_counting
    print("Total revenue for today is" + total_taking + "$" + "\n" + "Number of cars used this park is" + ticket_counting + "\n" + "Average charge per car is" + average_taking + "$" + "\n" + "Average length of stay per car is" + average_hour + "hours", end = " ")
    data_storage.clear
    ticket_counting = 0
    empty_carports = 100
    used_hours = 0
    total_taking = 0.0
    average_taking = 0.0
    average_hour = 0

# main programme
user_interface()



        
        
        