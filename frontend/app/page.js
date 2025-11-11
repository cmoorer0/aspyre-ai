"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [health, setHealth] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchHealth() {
      try {
        const res = await fetch("http://localhost:8000/health");
        if (!res.ok) {
          throw new Error(`Status ${res.status}`);
        }
        const data = await res.json();
        setHealth(data);
      } catch (err) {
        setError(err.message);
      }
    }

    fetchHealth();
  }, []);

  return (
    <main className="min-h-screen flex items-center justify-center bg-slate-900 text-slate-100">
      <div className="p-6 rounded-xl bg-slate-800 shadow-lg max-w-md w-full">
        <h1 className="text-2xl font-bold mb-4">Aspyre AI – MVP Health Check</h1>
        {error && (
          <p className="text-red-400">
            Could not reach backend: <span className="font-mono">{error}</span>
          </p>
        )}
        {health && (
          <div className="space-y-1">
            <p>
              <span className="font-semibold">Status:</span>{" "}
              <span className="font-mono">{health.status}</span>
            </p>
            <p>
              <span className="font-semibold">Service:</span>{" "}
              <span className="font-mono">{health.service}</span>
            </p>
          </div>
        )}
        {!health && !error && <p>Checking backend health…</p>}
      </div>
    </main>
  );
}
