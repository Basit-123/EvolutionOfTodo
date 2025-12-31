# Phase II Spec: Full-Stack Web Application

## Objective
Transform the CLI app into a multi-user web application with persistent storage, authentication, and intermediate features.

## Functional Requirements
1. **Core Essentials**: Add, Delete, Update, View, Toggle Completion.
2. **Organization**:
    - **Priorities**: High, Medium, Low.
    - **Tags/Categories**: Labels for tasks.
3. **Usability**:
    - **Search**: Filter tasks by title/description keyword.
    - **Filter**: Filter by status, priority, or tags.
    - **Sort**: Reorder by due date, priority, or alphabetical.
4. **Authentication**:
    - Multi-user support via Better Auth.
    - User isolation (users only see their own tasks).
    - JWT-based API security.

## Technical Stack
- **Backend**: FastAPI, SQLModel (ORM), Neon Serverless PostgreSQL.
- **Frontend**: Next.js 16 (App Router), Tailwind CSS, shadcn/ui.
- **Auth**: Better Auth (cross-service JWT).
- **Project Structure**: Monorepo (`apps/api`, `apps/web`).

## Database Schema (Refined)
- **User**: id, email, name.
- **Todo**: id, user_id, title, description, status, priority, tags (JSON), due_date, created_at.

## API Endpoints
- `GET /api/v1/todos`: List todos (with query params for search/filter/sort).
- `POST /api/v1/todos`: Create todo.
- `GET /api/v1/todos/{id}`: Get detail.
- `PATCH /api/v1/todos/{id}`: Update fields.
- `DELETE /api/v1/todos/{id}`: Remove task.
- `POST /api/v1/todos/{id}/toggle`: Toggle status.
- `GET /api/v1/tags`: List unique tags for user.

## UI/UX Requirements
- Responsive Dashboard.
- Clean "Task Cards" or Table view.
- Success/Error Toasts.
- Loading Skeletons.
