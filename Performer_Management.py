"""
This code is created for the core component: Peformer Management
(Ashleigh)
"""
# Performer Record Dictionary
performer_id = 0

performer_records = {
}

# Performer Record Functions
def add_performer(add_name, add_genre, add_email, performer_id):
    performer_records[performer_id] = {
        "Name": add_name,
        "Genre": add_genre,
        "Email": add_email
    }
    
    print("// New Performer Record List //")
    for performer_id in performer_records:
        print(f"{performer_id}: {performer_records[performer_id]}")

def update_performer(edit_choice):
    
    edit_name = str(input("Enter New Performer Name: "))
    performer_records[edit_choice]["Name"] = edit_name
    
    edit_genre = str(input("Enter New Performer Genre: "))
    performer_records[edit_choice]["Genre"] = edit_genre
    
    edit_email = str(input("Enter New Performer Email: "))
    performer_records[edit_choice]["Email"] = edit_email
    
    print(performer_records[edit_choice])

def delete_performer(delete_choice):
    del performer_records[delete_choice]
    print(f"Performer Record ID: {delete_choice} has been deleted.")

# Main Performer Loop (Ashleigh)
while True:
    try:
        performer_choice = int(input("""
                                    // Performer Management Panel //
                                    
                                    Please choose a numbered option
                                    
                                    1: Add Performer Record
                                    2: View Performer Record
                                    3: Update Performer Record
                                    4: Delete Performer Record
                                    5: Exit
                                    
                                    Choose Numbered Option: """))
        
        # Performer Choice Options
        if performer_choice == 1:
            print("// Chosen: Add Performer Record //")
            
            add_name = str(input("Enter Performer Name: "))
            add_genre = str(input("Enter Performer Genre: "))
            add_email = str(input("Enter Performer Email: "))
            performer_id += 1
            
            add_performer(add_name, add_genre, add_email, performer_id)
        
        elif performer_choice == 2:
            print("// Chosen: View Performer Record //")
            
            view_performer = int(input("Enter Performer ID: "))
            
            if view_performer > 0 and view_performer <= performer_id:
                print(f"{view_performer}: {performer_records[view_performer]}")
            else:
                print("Cannot be viewed: This is not a valid performer ID.")
        
        elif performer_choice == 3:
            print("// Chosen: Update Performer Record //")
            
            print("Below is the list of performer records:")
            
            for performer_id in performer_records:
                print(f"{performer_id}: {performer_records[performer_id]}")
            
            edit_choice = int(input("Enter Performer ID To Edit: "))
            
            if edit_choice > 0 and edit_choice <= performer_id:
                update_performer(edit_choice)
                print(f"New Version: {edit_choice}: {performer_records[edit_choice]}")
            else:
                print("Cannot be edited: This is not a valid performer ID.")
        
        elif performer_choice == 4:
            print("// Chosen: Delete Performer Record //")

            delete_choice = int(input("Enter Performer ID To Edit: "))
            
            if delete_choice > 0 and delete_choice <= performer_id:
                delete_performer(delete_choice)
            else:
                print("Cannot be deleted: This is not a valid performer ID.")
        
        elif performer_choice == 5:
            print("// Chosen: Exit //")
            print("The Performer Management Panel has been closed.")
            break
        
        else:
            print("Error: Option outside numerical range, please choose an option (1-4)")

    except ValueError:
        print("Error: This is not a valid number.")
