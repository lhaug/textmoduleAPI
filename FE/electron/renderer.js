const baseURL = 'http://localhost:8000/textmodules';
const form = document.getElementById('create-form');
const tableBody = document.getElementById('modules-table-body');

async function fetchModules() {
  const res = await fetch(baseURL);
  const data = await res.json();
  tableBody.innerHTML = '';

  data.forEach(mod => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td><span class="title-text">${mod.title}</span><input class="title-input" style="display:none; width: 100%;" value="${mod.title}"></td>
      <td><span class="content-text">${mod.content}</span><textarea class="content-input" style="display:none; width: 100%;">${mod.content}</textarea></td>
      <td>${formatTimestamp(mod.created_at)}</td>
      <td>${formatTimestamp(mod.updated_at)}</td>
      <td>
        <button class="edit-btn">✏️</button>
        <button class="save-btn" style="display:none;">💾</button>
      </td>
      <td>
        <button onclick="deleteModule(${mod.id})">🗑️</button>
      </td>
    `;

    const editBtn = row.querySelector('.edit-btn');
    const saveBtn = row.querySelector('.save-btn');
    const titleText = row.querySelector('.title-text');
    const contentText = row.querySelector('.content-text');
    const titleInput = row.querySelector('.title-input');
    const contentInput = row.querySelector('.content-input');

    editBtn.addEventListener('click', () => {
      titleText.style.display = 'none';
      contentText.style.display = 'none';
      titleInput.style.display = 'block';
      contentInput.style.display = 'block';
      editBtn.style.display = 'none';
      saveBtn.style.display = 'inline';
    });

    saveBtn.addEventListener('click', async () => {
      const updatedTitle = titleInput.value.trim();
      const updatedContent = contentInput.value.trim();
      if (!updatedTitle || !updatedContent) return;

      await fetch(`${baseURL}/${mod.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: updatedTitle, content: updatedContent })
      });

      fetchModules();
    });

    tableBody.appendChild(row);
  });
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const title = document.getElementById('title').value;
  const content = document.getElementById('content').value;

  await fetch(baseURL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, content })
  });

  form.reset();
  fetchModules();
});

window.deleteModule = async (id) => {
  await fetch(`${baseURL}/${id}`, { method: 'DELETE' });
  fetchModules();
};

function formatTimestamp(utcString) {
  const date = new Date(utcString);
  return date.toLocaleString(undefined, {
    dateStyle: 'short',
    timeStyle: 'medium',
    hour12: false,
  });
}

fetchModules();
