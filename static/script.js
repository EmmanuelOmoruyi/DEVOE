const chatBox = document.getElementById("response");

// =========================
// CHAT MESSAGES
// =========================
function addMessage(sender, text) {

    const div = document.createElement("div");
    div.classList.add("message");

    if (sender === "user") {
        div.classList.add("user-message");
    } else {
        div.classList.add("bot-message");
    }

    div.innerText = text;

    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// =========================
// UPLOAD FILE
// =========================
async function uploadFile() {

    const fileInput = document.getElementById("fileInput");

    if (!fileInput.files.length) {
        alert("Select a file first");
        return;
    }

    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    try {

        addMessage("bot", "Processing file...");

        const res = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        addMessage("bot", `File processed. Chunks: ${data.chunks_created}`);

    } catch (err) {
        console.error(err);
        addMessage("bot", "Upload failed");
    }
}

// =========================
// SEND MESSAGE
// =========================
async function sendMessage() {

    const input = document.getElementById("question");
    const query = input.value.trim();

    if (!query) return;

    addMessage("user", query);
    input.value = "";

    try {

        const res = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query })
        });

        const data = await res.json();

        addMessage("bot", data.answer);

    } catch (err) {
        console.error(err);
        addMessage("bot", "Error contacting DEVOE");
    }
}

// =========================
// EVENTS
// =========================
document.getElementById("uploadBtn").addEventListener("click", uploadFile);
document.getElementById("sendBtn").addEventListener("click", sendMessage);

document.getElementById("question").addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});