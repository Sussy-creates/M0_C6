# M0_C6 - Security System

# Write your code here.
# Define any variables or functions you need.
# The tests are testing your program's output.

# Defining list of users for the security sytem
users = {
        'mhenderson': 'out',
        'jjabrams': 'out',
        'sbrown': 'out',
        'enterocc': 'out',
        'zzdawg': 'out'
        }

def get_input():
    """Obtains input for the systems security system"""
    x = input('Input: ')
    global username
    global status
    msg = x.split(" ")
    if len(msg) != 2:
        username = 'Error'
        status = 'Error'
    else:
        username = msg[0]
        status = msg[1]
    return username
    return status

def process_input(username, status):
    """Processes input for security sytem, which will either check a user in or out, or sound the alarm"""
    if username not in users or status not in ['in', 'out'] or users[username] == status:
        print('  ALARM SOUNDED')
    else:
        users[username] = status
        print(f'  {username} is checked {status}')

# The main code which runs constantly as a security system
if __name__ == '__main__':
    while True:
       get_input()
       process_input(username,status)
