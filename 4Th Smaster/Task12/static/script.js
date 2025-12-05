const chatBody = document.getElementById('chat-body');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

function appendMessage(text, className) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${className}`;
    msgDiv.textContent = text;
    chatBody.appendChild(msgDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
}

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;
    appendMessage(message, 'user-msg');
    userInput.value = '';

    const response = await fetch('/get_reply', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message})
    });
    const data = await response.json();
    appendMessage(data.reply, 'bot-msg');
}

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', function(e){
    if(e.key === "Enter") sendMessage();
});
