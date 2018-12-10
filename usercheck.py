names = {'sandeep': 'sandeep mendiratta', 'manni': 'Manav Mendiratta', 'ro': 'Rohan Mendiratta'}
while True:
    check_name = input('Check the name if exists')
    if check_name in names:
        print(names[check_name] + 'is the username of ' + check_name)
    else:
        fullname = input("Enter full name")
        print('I do not have this name in dict')
        names['check_name'] = fullname
        print(names)
