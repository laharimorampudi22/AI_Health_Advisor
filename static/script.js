// Simple JS for chatbot and UI behavior (optional feature)
document.addEventListener("DOMContentLoaded", function() {
    const chatForm = document.getElementById("chatForm");
    const chatBox = document.getElementById("chatBox");
    
    if (chatForm) {
        chatForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const userMsg = document.getElementById("userInput").value;
            chatBox.innerHTML += `<p><b>You:</b> ${userMsg}</p>`;
            document.getElementById("userInput").value = "";

            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: `message=${encodeURIComponent(userMsg)}`
            });

            c

