class LetterWritter():
    def __init__(self) -> None:
        super().__init__()
        self.invited_persons = self.get_invited_names()
        self.base_invitation = self.get_base_invitation()

    def get_invited_names(self) -> str:
        with open("./Input/Names/invited_names.txt", "r") as file:
            return [line.strip() for line in file.read().splitlines()]

    def get_base_invitation(self):
        with open("./Input/Letters/starting_letter.txt", "r") as file:
            return ' '.join(file.readlines())

    def write_invitation(self):
        for person in self.invited_persons:
            with open(f"./Output/ReadyToSend/letter_for_{person}", "w") as file:
                file.write((self.base_invitation.replace("[name]", person)))