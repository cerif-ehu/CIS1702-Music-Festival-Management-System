"""This code will be used to make the core component vendor managment """

vendor_records = {}
vendor_id = 0

def add_vendors(name, foodtype,pitch, id):
   #adds vendor information to the dictionary (lucas)
   try:
       if id in vendor_records:
           raise ValueError ("Vendor already in record") 
       
       vendor_records[vendor_id] = {
            "Vendor ID": id,
            "Vendor Name": name,
            "Food Type": foodtype,
            "Pitch Location": pitch
            
        }
       print()
       print("Added Vendor")
       print()
       id += 1
       return id 
   except ValueError as error:
       print(error)

def delete_vendors(deleting):
    try:
        if deleting not in vendor_records:
            raise KeyError ("That Vendor is not in the records")
        
        del(vendor_records[deleting])
        
        print()
        print("deleted Vendor")
        print()
    except KeyError as error:
        print(error)

def view_vendor(viewing):
    try:
        if viewing in vendor_records:
            
            output = ""
            for key, value in vendor_records[viewing].items():
                output += (f"{key}: {value}\n")
            return output.rstrip()
      
        raise KeyError ("That Vendor Not in record")
    
    except KeyError as error:
        print(error)
    

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
        try:
            vendor_name = str(input("Enter the Vendor Name: "))
            vendor_foodtype = str(input("Enter the Vendor's Food Type: "))
            vendor_pitch_loction = str(input("Enter the Vendor's Pitch Location: "))
            if not vendor_name or not vendor_foodtype or not vendor_pitch_loction:
                raise ValueError("Make sure all fields have been filled out")
            
            vendor_id = add_vendors(vendor_name, vendor_foodtype, vendor_pitch_loction, vendor_id)
            
            
        except ValueError as empty:
            print(empty)
           
    elif choice == 2:
        for value in vendor_records.keys():
            print(value)
        try:
            deleting = int(input("Choose Which Vendor from their ID to delete: "))
            
        except ValueError:
            print("Please input a whole number")
            
        delete_vendors(deleting)
        
    elif choice == 3:
        viewing = int(input("Choose Vendor ID you want to view: "))
        print(view_vendor(viewing))
    
    elif choice == 4:
        print(vendor_records)
        view_all_vendors()
        
    elif choice == 5:
        update_vendor()
    
    elif choice == 6:
        break