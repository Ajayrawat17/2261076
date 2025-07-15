import { useState } from "react";
import { customRequest } from "../api";

const CreateURLForm = ({ setResult }) => {
  const [form, setForm] = useState({
    url: '',
    validity: 30,
    shortcode: ''
  });

  const sendData = async () => {
    const out = await customRequest("/shorturls/", form);
    if (out.shortLink) {
      setResult(out);
    } else {
      alert("Error: " + (out.error || "Unknown"));
    }
  };

  return (
    <div>
      <input placeholder="Target URL"
             onChange={(e) => setForm({ ...form, url: e.target.value })} />
      <input placeholder="Validity (min)"
             type="number"
             defaultValue={30}
             onChange={(e) => setForm({ ...form, validity: +e.target.value })} />
      <input placeholder="Custom Code (opt)"
             onChange={(e) => setForm({ ...form, shortcode: e.target.value })} />
      <button onClick={sendData}>Generate</button>
    </div>
  );
};

export default CreateURLForm;
