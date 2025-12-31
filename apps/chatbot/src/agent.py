from openai import OpenAI
from .tools import create_todo, list_todos, toggle_todo, delete_todo
import json

client = OpenAI()

SYSTEM_PROMPT = """
You are 'Evolution AI', a smart todo manager.
You help users manage their tasks via natural language.
You are polite, efficient, and support both English and Urdu (اردو).
If the user speaks in Urdu, reply in Urdu.
Use the provided tools to manage todos.
"""

def handle_query(user_input: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    # This is a simplified agent loop for demonstration of the SDD approach
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "create_todo",
                    "description": "Create a new todo task",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "description": {"type": "string"},
                            "priority": {"type": "string", "enum": ["low", "medium", "high"]}
                        },
                        "required": ["title"]
                    }
                }
            }
        ]
    )

    # Logic to handle tool calls and Urdu response would go here in full implementation
    return response.choices[0].message.content
