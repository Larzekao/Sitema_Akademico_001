const form = document.getElementById('loginForm');
const messageDiv = document.getElementById('message');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  try {
    const response = await fetch('/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (response.ok && data.success) {
      messageDiv.textContent = 'Login exitoso. Redirigiendo...';
      if (data.rol === 'Admin') {
        window.location.href = '/admin/';
      } else if (data.rol === 'Profesor') {
        window.location.href = '/profesor/';
      } else if (data.rol === 'Estudiante') {
        window.location.href = '/estudiante/';
      } else if (data.rol === 'Tutor') {
        window.location.href = '/tutor/';
      } else {
        window.location.href = '/';
      }
    } else {
      messageDiv.textContent = data.message || 'Error en el login';
    }
  } catch (err) {
    messageDiv.textContent = 'Error de red: ' + err.message;
  }
});
