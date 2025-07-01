export default function ContactList({
  contacts,
}: {
  contacts: { name: string; email: string; id: string }[];
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
              <strong>{c.name}</strong> — {c.email}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
