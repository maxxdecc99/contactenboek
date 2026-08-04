from contact import Contact


contacts = []


c1 = Contact("Jan Jansen", "0612345678", "jan@mail.com")
contacts.append(c1)
c2 = Contact("Marie de Vries", "0687654321", "marie@mail.com")
contacts.append(c2)


while True:
    choice = input("choose an option: ")
    if choice == "add contact":
        name_input = input("add name: ")
        number_input = input("add number: ")
        email_input = input("add email: ")
        new_contact = Contact(name_input, number_input, email_input)
        contacts.append(new_contact)
    elif choice == "show all contacts":
        for contact in contacts:
            print(contact)
    elif choice == "stop":
        break
    else:
        print("wrong input, try again")
