export default function ContactList({
  contacts,
  deleteContact,
}: {
  contacts: { name: string; email: string; id: string }[];
  deleteContact: (id: string) => void;
}) {
  return (
    <div>
      <h2>Rubrica</h2>
      {contacts.length === 0 ? (
        <p>Nessun contatto presente.</p>
      ) : (
        <ul>
          {contacts.map((c: { name: string; email: string; id: string }) => (
            <li key={c.id}>
              <strong>{c.name}</strong> — {c.email}{" "}
              <button onClick={() => deleteContact(c.id)}>DELETE</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
