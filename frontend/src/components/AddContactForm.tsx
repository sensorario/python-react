import { useState } from "react";

export default function AddContactForm({
  onContactSaved,
}: {
  onContactSaved: () => void;
}) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    const response = await fetch("http://localhost:8000/contacts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({ name, email, phone }),
    });

    if (response.ok) {
      onContactSaved();
      setName("");
      setEmail("");
      setPhone("");
    } else {
      console.error("Errore nell'aggiunta del contatto");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Aggiungi contatto</h2>
      <div>
        <input
          type="text"
          placeholder="Nome"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>
      <div>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>
      <div>
        <input
          type="phone"
          placeholder="phone"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          required
        />
      </div>
      <button type="submit">Aggiungi</button>
    </form>
  );
}
