"""This code will be used to make the core component vendor managment """

vendor_records = {} #dictionary storing all vendor information 
vendor_id = 0 #the vendor id for the nex vendor to be added 

def add_vendors(name, foodtype,pitch, id):
   """adds vendor information to the dictionary and detects key and value errors (lucas)"""
   try:
       #checks that any parameter is not empty and retuns value error if it is (lucas)
       if not name or not foodtype or not pitch:
                raise ValueError("Make sure all fields have been filled out")
                       
       if id in vendor_records:
           raise ValueError ("Vendor already in record") 
       
       vendor_records[id] = {
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
       raise

def delete_vendors(deleting):
    """this function is used to delete a vendor from the dictionary and detects key and value errors (lucas)"""
    try:
        
        deleting = int(deleting)
        
        if deleting not in vendor_records:
            raise KeyError ("That Vendor is not in the records")
        
        del(vendor_records[deleting])
        
        print()
        print("deleted Vendor")
        print()
    except KeyError as error:
        print(error)
        raise
    except ValueError:
        print("Please input a whole number")
        raise 

def view_vendor(viewing):
    """function to view a specific chosen vendor and detects value and key errors (lucas)"""
    try:
        #checks if entered ID is an intger and if it is runs through loop and if not Value Error occurs (lucas)
        viewing = int(viewing)
        
        if viewing in vendor_records:
            
            output = ""
            for key, value in vendor_records[viewing].items():
                output += (f"{key}: {value}\n")
            return output
      
        raise KeyError ("That Vendor Not in record")
    
    except KeyError as error:
        print(error)
        raise
    
    except ValueError:
        print("Please enter a Whole Number")
        raise
    
def view_all_vendors():
    pass

def update_vendor(update, name, foodtype, pitch_location):
    """this function updates vendor information and dectes KeyErrors (lucas)"""
   
    try: #checks that ID for vendor being updated in dictioanry as if not KeyError caused
        if update not in vendor_records:
            raise KeyError


    except KeyError:
            print("That key is not in records")
            raise
    
    vendor_records[update] = {
                "Vendor ID": update,
                "Vendor Name": name,
                "Food Type": foodtype,
                "Pitch Location": pitch_location
            }
    
    

"""TO DO:
add file handling system to the code so that everything is saved onto a file"""

def main(vendor_id):
    """this function is main repeating block that runs until user chooses to exit and lets 
    users choose what operation to preform (lucas)"""
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
            #user enters details of vendors then gets passed into function and if any empty thrn ValueError (lucas)
            print()
        
            vendor_name = str(input("Enter the Vendor Name: "))
            vendor_foodtype = str(input("Enter the Vendor's Food Type: "))
            vendor_pitch_loction = str(input("Enter the Vendor's Pitch Location: "))
            
            vendor_id = add_vendors(vendor_name, vendor_foodtype, vendor_pitch_loction, vendor_id)
            
        elif choice == 2:
            for keys in vendor_records.keys():
                print(keys)
        
            deleting = int(input("Choose Which Vendor from their ID to delete: "))
        
            delete_vendors(deleting)
            
        elif choice == 3:
                viewing = int(input("Choose Vendor ID you want to view: "))
                
                print(view_vendor(viewing))
                
        elif choice == 4:
            print(vendor_records)
            view_all_vendors()
            
        elif choice == 5:
            for keys in vendor_records.keys():
                print(keys)
                
            update = int(input("Choose a vendor to update: "))
            new_name = str(input("Enter Vendor Name: "))
            new_food_type = str(input("Enter Vendor Food Type: "))
            new_pitch_location = str(input("Enter Pitch Location for Vendor: "))
                    
            update_vendor(update, new_name, new_food_type, new_pitch_location)
        
        elif choice == 6:
            break

if __name__ == ("__main__"): #runs code when program is started (lucas)
    main(vendor_id)