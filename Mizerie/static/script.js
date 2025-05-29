async function loadItems() {
  const res = await fetch('/items');
  const items = await res.json();

  const table = document.getElementById('itemsTable');
  table.innerHTML = '';
  items.forEach(item => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${item.id}</td>
      <td>${item.title}</td>
      <td>${item.author}</td>
      <td>
        <button onclick="editItem(${item.id})">Edit</button>
        <button onclick="deleteItem(${item.id})">Delete</button>
      </td>
    `;
    table.appendChild(row);
  });
}

async function addItem() {
  const title = prompt("Enter title:");
  const author = prompt("Enter author:");
  if (!title || !author) return;
  await fetch('/items', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, author })
  });
  loadItems();
}

async function editItem(id) {
  const title = prompt("New title:");
  const author = prompt("New author:");
  if (!title || !author) return;
  await fetch(`/items/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, author })
  });
  loadItems();
}

async function deleteItem(id) {
  if (!confirm("Are you sure?")) return;
  await fetch(`/items/${id}`, { method: 'DELETE' });
  loadItems();
}

document.addEventListener('DOMContentLoaded', loadItems);