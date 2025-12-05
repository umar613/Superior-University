const chatbox = document.getElementById('chatbox');
const input = document.getElementById('input');
const send = document.getElementById('send');

function addMessage(sender, text) {
    const div = document.createElement('div');
    div.className = `message ${sender}`;
    chatbox.appendChild(div);

    // Typing effect for bot
    if (sender === 'bot') {
        let i = 0;
        const interval = setInterval(() => {
            div.textContent += text.charAt(i);
            i++;
            if (i >= text.length) clearInterval(interval);
            chatbox.scrollTop = chatbox.scrollHeight;
        }, 20);
    } else {
        div.textContent = text;
        chatbox.scrollTop = chatbox.scrollHeight;
    }
}

send.addEventListener('click', () => {
    const message = input.value.trim();
    if (!message) return;
    addMessage('user', message);
    input.value = '';

    fetch('/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => addMessage('bot', data.response));
});

input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') send.click();
});
