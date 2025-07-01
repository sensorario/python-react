import "./App.css";
import AddContactForm from "./components/AddContactForm";
import ContactList from "./components/ContactList"; // src/components/ContactList.jsx
import { useEffect, useState } from "react";

function App() {
  const [contacts, setContacts] = useState([]);
  const [error, setError] = useState(null);

  const doSomething = () => {
    fetch("http://localhost:8000/contacts")
      .then((res) => {
        if (!res.ok) throw new Error("Errore nel recupero dei contatti");
        return res.json();
      })
      .then((data) => setContacts(data))
      .catch((err) => setError(err.message));
  };

  useEffect(() => doSomething(), []);

  if (error) return <p>Errore: {error}</p>;

  return (
    <>
      <h1>Vite + React</h1>
      <p>Hello World!</p>
      <ContactList contacts={contacts} />
      <AddContactForm onContactSaved={() => doSomething()} />
    </>
  );
}

export default App;
