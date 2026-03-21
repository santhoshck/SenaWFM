"use client";

import { useEffect, useState } from "react";

export default function HealthCheck() {
  const [status, setStatus] = useState<string>("Loading...");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then((res) => res.json())
      .then((data) => setStatus(`Backend is online: ${data.status}`))
      .catch((err) => setStatus("Backend is offline or unreachable"));
  }, []);

  return (
    <div className="p-10 font-sans">
      <h1 className="text-3xl font-bold">System Status</h1>
      <p className="mt-4 text-xl">{status}</p>
    </div>
  );
}
