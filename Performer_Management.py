"""
This code is created for the core component: Peformer Management
(Ashleigh)
"""
# Performer Record Dictionary
performer_id = 0

performer_records = {
    performer_id: {
        "Name": add_name,
        "Genre": add_genre,
        "Email": add_email 
    }
}

# Performer Record Functions
def add_performer(add_name, add_genre, add_email, performer_id):
    performer_records[performer_id] = {
        "Name": add_name,
        "Genre": add_genre,
        "Email": add_email
    }

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
            
            add_performer(add_name, add_genre, add_email)
            
            # TODO: Fix Add Performer Record Code
        
        elif performer_choice == 2:
            print("// Chosen: View Performer Record //")
            
            # TODO: View Performer Record Code
        
        elif performer_choice == 3:
            print("// Chosen: Update Performer Record //")
            
            # TODO: Update Performer Record Code
        
        elif performer_choice == 4:
            print("// Chosen: Delete Performer Record //")
            
            # TODO: Delete Performer Record Code
        
        elif performer_choice == 5:
            print("// Chosen: Exit //")
            print("The Performer Management Panel has been closed.")
            break
        
        else:
            print("Error: Option outside numerical range, please choose an option (1-4)")
            continue

    except ValueError:
        print("Error: This is not a valid number, please choose an option (1-4)")
