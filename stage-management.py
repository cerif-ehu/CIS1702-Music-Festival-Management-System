with open("stages.txt", "r") as stage_file:
    stages = [line.strip().split(",") for line in stage_file]

stage_names = stages[1]
stage_capacities = stages[4]
stage_locations = stages[7]

def assemble(): ## i used a for loop here to assemble each dictionary. it's a function so it can be called again after changes (ceri)
     global stage_data
     stage_data = {"stages": {}}
     for stage, capacity, location in zip(stage_names, stage_capacities, stage_locations):
          stage_data["stages"][stage] = {
            "capacity": capacity,
            "location": location
          }
## TODO make the system use dictionaries instead of list indexes like a chud (ceri)

def view_stages(input):
    stage = 0
    index = 0
    if input in stage_names: ## if the user types the stage name directly (ceri)
        stage = stage_names.index(input)
    elif int(input) in list(range(len(stage_names) + 1)): ## if user types the list number (ceri)
        stage = (int(input) - 1)
    else:
        input("Invalid choice. Press any key to return to menu")
        return
    return(f'''
                Stage Name:  {stage_names[stage]}
                Capacity:    {stage_capacities[stage]}
                Location:    {stage_locations[stage]}
                ''')
while True:
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
        print(f"\n// Available Stages ({len(stage_names)}):\n")
        stgcount = 0
        for i in stage_names:
            stgcount += 1
            print(f"{stgcount}. {i}")
        view_choice = input("\nEnter the stage number or the stage name to view its details: ")
        print(view_stages(view_choice))
        input("Press any key to return to menu ")
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
        print(stage_data)