"""This code will be used to make the core component vendor managment """

def add_vendors():
    pass

def delete_vendors():
    pass

def view_vendor():
    pass

def view_all_vendors():
    pass

def update_vendor():
    pass

while True:
    print("""
                        
                                    Choose an option
                                    
                                1: add vendor
                                2: delete vendor
                                3: view a vendor
                                4: view all vendor
                                5: update a vendor
                                6: exit
                                    
                        """)
        
    try:
        choice = int(input("choice: "))
        
    except ValueError:
        print("Enter a (1-6)")
        continue 

    if choice == 1:
        add_vendors()
    
    elif choice == 2:
        delete_vendors()
        
    elif choice == 3:
        view_vendor()
    
    elif choice == 4:
        view_all_vendors()
        
    elif choice == 5:
        update_vendor()
    
    elif choice == 6:
        break