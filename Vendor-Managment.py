"""This code will be used to make the core component vendor managment """

vendor_records = {}
vendor_id = 0

def add_vendors(name, foodtype,pitch, id):
    #adds vendor information to the dictionary (lucas)
    vendor_records[vendor_id] = {
        "Vendor ID": id,
        "Vendor Name": name,
        "Food Type": foodtype,
        "Pitch Location": pitch
        
    }
    
    id += 1
    return id

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
        print()
        vendor_name = str(input("Enter the Vendor Name: "))
        vendor_foodtype = str(input("Enter the Vendor's Food Type: "))
        vendor_pitch_loction = str(input("Enter the Vendor's Pitch Location: "))
        vendor_id = add_vendors(vendor_name, vendor_foodtype, vendor_pitch_loction, vendor_id)
    
    elif choice == 2:
        delete_vendors()
        
    elif choice == 3:
        view_vendor()
    
    elif choice == 4:
        print(vendor_records)
        view_all_vendors()
        
    elif choice == 5:
        update_vendor()
    
    elif choice == 6:
        break