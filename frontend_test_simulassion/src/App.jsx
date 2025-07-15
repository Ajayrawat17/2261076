import CreateURLForm from "./components/CreateURLForm";
import ShowShortResult from "./components/ShowShortResult";
import CheckStats from "./components/CheckStats";
import { useState } from "react";

function App() {
  const [created, setCreated] = useState(null);

  return (
    <div style={{ margin: "30px" }}>
      <h2>🧠 AffordMed Custom URL Shortener</h2>
      <CreateURLForm setResult={setCreated} />
      <ShowShortResult data={created} />
      <hr />
      <CheckStats />
    </div>
  );
}

export default App;
