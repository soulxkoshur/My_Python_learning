def main():
    history = []

    while True:
        action = input("Action: ")
        if action.title() == "Undo":
            undone = history.pop() ## pop() is the function that lets you delete last item in your list!
            print(f"Undone: {undone}")
        elif action.title() == "Restart":
            history.clear()
        else:
            history.append(action)
            print(history)
main()
