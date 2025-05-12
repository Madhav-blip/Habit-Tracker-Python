from datetime import datetime, timedelta

habits = []

while True:
    print('''
      Enter 1 for adding a new habit.
      Enter 2 for viewing all your habits.
      Enter 3 to exit the program.
      Enter 4 to mark a habit as done for today.
      ''')
    a = input("Enter you choice here: ")

    if a == '1':
        habitname = input("Enter your habit: ")
        habitdur = input("Enter the duration: ")
        habits.append({
            "Habit Name": habitname,
            "Duration of habit": habitdur,
            "Last Done": "",
            "Streak": 0
        })

    elif a == '2':
        print("Here is a list of all your habits:")
        print(habits)

    elif a == '3':
        print("Program has been exitted.")
        break

    elif a == '4':
        if not habits:
            print("No habits to mark.")
            continue

        print("Which habit did you complete today?")
        i = 1
        for h in habits:
            print(i, h["Habit Name"])
            i += 1

        choice = int(input("Enter habit number: ")) - 1

        if 0 <= choice < len(habits):
            today = datetime.today().date()
            last_done = habits[choice]["Last Done"]

            if last_done == "":
                habits[choice]["Streak"] = 1
                habits[choice]["Last Done"] = str(today)
                print("Marked as done. Streak started.")
            else:
                c = datetime.strptime(last_done, "%Y-%m-%d").date()

                if c == today:
                    print("Already marked as done today.")
                elif c == today - timedelta(days=1):
                    habits[choice]["Streak"] += 1
                    habits[choice]["Last Done"] = str(today)
                    print("Well done! Streak continued.")
                else:
                    habits[choice]["Streak"] = 1
                    habits[choice]["Last Done"] = str(today)
                    print("Marked as done. Streak restarted.")
        else:
            print("Invalid selection.")
