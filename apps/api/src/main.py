from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, create_engine, select
from typing import List, Optional
from .models import Todo, User, Priority, TodoStatus
import os

app = FastAPI(title="Evolution of Todo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLite for local testing, Neon for production
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo.db")
engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session

@app.on_event("startup")
def on_startup():
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)

# Mock Auth Dependency (Better Auth integration logic placeholder)
def get_current_user_id():
    return "user_123"

@app.get("/api/v1/todos", response_model=List[Todo])
def read_todos(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    search: Optional[str] = None,
    priority: Optional[Priority] = None,
    status: Optional[TodoStatus] = None,
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user_id)
):
    statement = select(Todo).where(Todo.user_id == user_id)

    if search:
        statement = statement.where(Todo.title.contains(search) | Todo.description.contains(search))
    if priority:
        statement = statement.where(Todo.priority == priority)
    if status:
        statement = statement.where(Todo.status == status)

    statement = statement.offset(offset).limit(limit)
    return session.exec(statement).all()

@app.post("/api/v1/todos", response_model=Todo)
def create_todo(
    todo: Todo,
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user_id)
):
    todo.user_id = user_id
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@app.patch("/api/v1/todos/{todo_id}", response_model=Todo)
def update_todo(
    todo_id: int,
    todo_data: dict,
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user_id)
):
    db_todo = session.get(Todo, todo_id)
    if not db_todo or db_todo.user_id != user_id:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in todo_data.items():
        if hasattr(db_todo, key):
            setattr(db_todo, key, value)

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@app.delete("/api/v1/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user_id)
):
    db_todo = session.get(Todo, todo_id)
    if not db_todo or db_todo.user_id != user_id:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(db_todo)
    session.commit()
    return {"ok": True}
