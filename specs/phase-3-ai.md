# Phase III Spec: AI-Powered Todo Chatbot

## Objective
Enhance the Todo application with a conversational interface using OpenAI Agents SDK and MCP (Model Context Protocol).

## Functional Requirements
1. **Natural Language Management**:
    - "Add a task to buy groceries"
    - "Mark my meeting as done"
    - "Show me all high priority tasks"
2. **Intelligent Rescheduling**:
    - "Move my urgent tasks to tomorrow 2 PM"
3. **Multilingual Support**:
    - Support for English and Urdu (اردو) commands.
4. **Context Awareness**:
    - The bot should know the current date/time to resolve relative dates (e.g., "next Monday").

## Technical Architecture
- **Agent Framework**: OpenAI Agents SDK.
- **Protocol**: Official MCP SDK to expose Todo API as tools.
- **Service**: A new `apps/chatbot` service (Python) that handles Agent logic.
- **Frontend Integration**: Chat sidebar/overlay in the Next.js app.

## Tools (MCP)
- `create_todo(title, description, priority, due_date)`
- `list_todos(search, priority, status)`
- `update_todo(id, title, status, due_date)`
- `delete_todo(id)`

## Urdu Support (System Prompt)
The system prompt will include instructions to detect and respond in Urdu if the user initiates the conversation in Urdu, ensuring grammatical correctness in the context of task management.
