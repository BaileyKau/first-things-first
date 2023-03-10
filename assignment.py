class Assignment:
    def __init__(self, name, deadline, prio, description):
        self.name = name
        self.deadline = deadline
        self.prio = prio
        self.description = description

    def change_name(self, name):
        self.name = name

    def change_prio(self, prio):
        self.prio = prio

    def change_deadline(self, deadline):
        self.deadline = deadline

    def change_description(self, description):
        self.description = description

    