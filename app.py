from datetime import date
import json

def load_habits(filename="habits.json"):
    """Loads habits from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_habits(habits, filename="habits.json"):
    """Saves habits to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(habits, f, indent=4)

def add_habit(habits):
    """Adds a new habit to the tracker."""
    habit_name = input("Enter the name of the habit: ").strip().lower()
    if habit_name in habits:
        print(f"Habit '{habit_name}' already exists.")
    else:
        habits[habit_name] = []
        print(f"Habit '{habit_name}' added.")
    return habits

def record_completion(habits):
    """Records the completion of a habit for the current date."""
    habit_name = input("Enter the name of the habit to record completion for: ").strip().lower()
    if habit_name not in habits:
        print(f"Habit '{habit_name}' not found.")
    else:
        today = str(date.today())
        if today not in habits[habit_name]:
            habits[habit_name].append(today)
            print(f"Completion for '{habit_name}' recorded for {today}.")
        else:
            print(f"Completion for '{habit_name}' already recorded for {today}.")
    return habits

def view_habits(habits):
    """Displays all tracked habits and their completion dates."""
    if not habits:
        print("No habits currently being tracked.")
        return

    print("\n--- Your Habits ---")
    for habit, completions in habits.items():
        print(f"Habit: {habit.capitalize()}")
        if completions:
            print("  Completions:", ", ".join(completions))
        else:
            print("  No completions recorded yet.")
    print("-------------------\n")

def main():
    habits = load_habits()

    while True:
        print("1. Add a new habit")
        print("2. Record habit completion")
        print("3. View all habits")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            habits = add_habit(habits)
            save_habits(habits)
        elif choice == '2':
            habits = record_completion(habits)
            save_habits(habits)
        elif choice == '3':
            view_habits(habits)
        elif choice == '4':
            print("Exiting habit tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
