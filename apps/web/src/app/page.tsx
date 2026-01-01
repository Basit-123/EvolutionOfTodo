"use client";

import { useState, useEffect } from "react";

interface Todo {
  id: number;
  title: string;
  description: string;
  status: string;
  priority: string;
  tags: string;
}

export default function Dashboard() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
    fetch(`${apiUrl}/api/v1/todos`)
      .then((res) => res.json())
      .then((data) => {
        setTodos(data);
        setLoading(false);
      });
  }, []);

  return (
    <div className="max-w-4xl mx-auto p-8">
      <header className="mb-8">
        <h1 className="text-4xl font-bold text-slate-900">My Evolvable Todo List</h1>
        <p className="text-slate-500">Phase II: Full-Stack Web App</p>
      </header>

      {loading ? (
        <div className="space-y-4">
          {[1, 2, 3].map((i) => (
            <div key={i} className="h-24 bg-slate-200 animate-pulse rounded-lg"></div>
          ))}
        </div>
      ) : (
        <div className="grid gap-4">
          {todos.map((todo) => (
            <div key={todo.id} className="bg-white p-6 rounded-lg shadow-sm border border-slate-200 flex justify-between items-center">
              <div>
                <h3 className="text-xl font-semibold">{todo.title}</h3>
                <p className="text-slate-600">{todo.description}</p>
                <div className="mt-2 flex gap-2">
                  <span className={`px-2 py-1 rounded text-xs ${
                    todo.priority === 'high' ? 'bg-red-100 text-red-700' :
                    todo.priority === 'medium' ? 'bg-yellow-100 text-yellow-700' :
                    'bg-green-100 text-green-700'
                  }`}>
                    {todo.priority}
                  </span>
                  <span className="bg-slate-100 text-slate-700 px-2 py-1 rounded text-xs">
                    {todo.status}
                  </span>
                </div>
              </div>
              <button className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition">
                Toggle Completion
              </button>
            </div>
          ))}
          {todos.length === 0 && <p className="text-center text-slate-400">No tasks found. Add your first one!</p>}
        </div>
      )}
    </div>
  );
}
