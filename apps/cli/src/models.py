from dataclasses import dataclass

@dataclass
class Todo:
    id: int
    title: str
    description: str = ""
    is_completed: bool = False

    def toggle(self):
        self.is_completed = not self.is_completed
