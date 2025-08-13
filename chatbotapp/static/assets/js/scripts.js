document.addEventListener('DOMContentLoaded', (event) => {
    const socket = io();

    socket.on('connect', () => {
        console.log('WebSocket connected');
    });

    document.getElementById('send-btn').addEventListener('click', function() {
        const message = document.getElementById('message').value;
        if (message.trim() !== '') {
            console.log('Sending message:', message);
            socket.send(message);
            document.getElementById('message').value = '';
        }
    });

    socket.on('message', function(msg) {
        console.log('Received message:', msg);
        const chatBox = document.getElementById('chat-box');
        const messageElement = document.createElement('div');
        messageElement.className = 'message';
        messageElement.textContent = msg;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    });
});