while True:

    from tabulate import tabulate

    stages = open("stages.txt", "r").readlines()
    stage_names = [stage.split(",")[0] for stage in stages]
    stage_capacities = [stage.split(",")[1] for stage in stages]
    stage_locations = [stage.split(",")[2].strip() for stage in stages]

    stages ={
        "name": stage_names,
        "capacity": stage_capacities,
        "location": stage_locations
    }

    def view_stages():
            print(tabulate(stages), headers=["Name", "Capacity", "Location"], tablefmt="orgtbl")
            input("Press any key to return to the main menu.")
    
    try:
        stage_choice = int(input("""
        Please pick an option 1-5:
        1. View Stages
        2. Add a Stage
        3. Update a Stage
        4. Delete a Stage
        5. Exit
        6. Debug
        """))
        if stage_choice == 1:
            view_stages()
        elif stage_choice == 2:
            add_stage()
        elif stage_choice == 3:
            update_stage()
        elif stage_choice == 4:
            delete_stage()
        elif stage_choice == 5:
            print("Exiting the program.")
            break
        elif stage_choice == 6:
            print(stages)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
