class Menu:
    def __init__(self):
        self.title = "Please Select from the following options"
        self.prompt = "Please enter selection: "
        self.invalid_prompt = "Invalid selection, please enter selection: "
        self.options = dict()
        self.case_sensitive = False

    def add_option(self, option, description):
        # Add new option, or update existing option it already exists
        if not self.case_sensitive:
            option = option.lower()
        self.options[option] = description

    def display_menu(self):
        print(self.title)
        for k, v in self.options.items():
            print(f"{k} - {v}")
        selection = input(self.prompt)
        if not self.case_sensitive:
            selection = selection.lower()
        while selection not in self.options.keys():
            selection = input(self.invalid_prompt)
            if not self.case_sensitive:
                selection = selection.lower()
        return selection
