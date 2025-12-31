from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from enum import Enum
import json

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TodoStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"

class UserBase(SQLModel):
    id: str = Field(primary_key=True)
    email: str = Field(index=True, unique=True)
    name: str

class User(UserBase, table=True):
    todos: List["Todo"] = Relationship(back_populates="user")

class TodoBase(SQLModel):
    title: str
    description: Optional[str] = None
    status: TodoStatus = Field(default=TodoStatus.PENDING)
    priority: Priority = Field(default=Priority.MEDIUM)
    due_date: Optional[datetime] = None
    tags: str = Field(default="[]")  # Stored as JSON string

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: User = Relationship(back_populates="todos")

    def get_tags(self) -> List[str]:
        return json.loads(self.tags)

    def set_tags(self, tags: List[str]):
        self.tags = json.dumps(tags)
