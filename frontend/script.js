// Predefined static responses
const responses = {
    "insat": "🛰️ INSAT (Indian National Satellite System) is used for telecommunications, broadcasting, meteorology, and search & rescue operations across India.",
    "risat": "🛰️ RISAT (Radar Imaging Satellite) provides radar-based Earth observation for agriculture, forestry, and disaster management.",
    "weather": "🌤️ You can access real-time weather data and forecasts at the MOSDAC portal: www.mosdac.gov.in/weather",
    "contact": "📧 You can contact us at support@mosdac.gov.in or visit www.mosdac.gov.in for more info.",
    "satellite": "🛰️ MODSAC supports several satellites including INSAT, RISAT, and more for weather and oceanographic data.",
    "help": "🤖 I’m here to help! You can ask me about satellites, weather data, or how to use the MOSDAC portal."
};

// Add welcome message on page load
window.onload = function() {
    addMessage("Bot", "👋 Hi! I’m your MODSAC Help Bot. How can I assist you today?");
};

// Function to send user message
function sendMessage() {
    const userInput = document.getElementById("user-input").value.trim();
    if (userInput === "") return;

    addMessage("You", userInput);
    const botResponse = getBotResponse(userInput.toLowerCase());
    setTimeout(() => addMessage("Bot", botResponse), 500);

    document.getElementById("user-input").value = "";
}

// Function to display message
function addMessage(sender, message) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.classList.add(sender === "Bot" ? "bot-message" : "user-message");
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to get bot response
function getBotResponse(userInput) {
    for (const key in responses) {
        if (userInput.includes(key)) {
            return responses[key];
        }
    }
    return "🤖 Sorry, I’m still learning. Can you try asking differently?";
}
