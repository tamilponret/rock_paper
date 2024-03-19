contact = {}
def display_contact():
    print("name\t\tcontact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice = int(input("1. Add new contact \n 2. search contact \n 3.Display contact\n 4. edit contact\n 5. exit\n"))
    if choice == 1:
        name = input("Enter the contact name")
        phone = input("enter the mobile number")
        contact[name] = phone
    elif choice == 2:
        search_name = input("enter the contact name")
    if search_name in contact:
        print(search_name," contact number is", contact[search_name])
    else:
        print("Name is not found in contact book")
    if choice == 3:
        if not contact:
            print("empty contact book")
        else:
             display_contact()
    elif choice == 4:
        edit_contact = input("enter the contact to be edited")
        if edit_conact in contact:
            phone = input("enter moblie number")
            contact[edit_contact]=phone
            print("contact uopdated")
            display_contact()
        else:
            print("name is not found in contact book")
    else:
            break
            
