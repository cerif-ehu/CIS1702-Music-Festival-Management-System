"""
This code is created for the core component: Peformer Management
(Ashleigh)
"""

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
            
            # TODO: Add Performer Record Code
        
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