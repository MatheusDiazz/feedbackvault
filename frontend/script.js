document.getElementById('feedbackForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const email = document.getElementById('email').value;
  const message = document.getElementById('message').value;

  const res = await fetch('https://tb7om8dkyh.execute-api.us-east-1.amazonaws.com/prod/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, message })
  });

  const text = await res.text();
  document.getElementById('response').innerText = text;
});
