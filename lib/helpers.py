def print_menu(menu_title, options):
    print("\n" + menu_title)
    for key, value in options.items():
        print(f"{key}: {value}")
    print()

def get_input(prompt, valid_options=None):
    while True:
        response = input(prompt).strip()
        if valid_options and response not in valid_options:
            print(f"Invalid choice, please select from {', '.join(valid_options)}.")
        else:
            return response
