function sendMessage() {
    var userInput = document.getElementById("floatingInput").value.trim();
    if (userInput !== "") {
      var chatBox = document.getElementById("chat-box");
      var messageElement = document.createElement("div");
      messageElement.textContent = userInput;
      messageElement.classList.add("user-message");
      chatBox.appendChild(messageElement);
      chatBox.scrollTop = chatBox.scrollHeight;
      document.getElementById("floatingInput").value = "";
      // Simulate receiving a response after 1 second
      setTimeout(receiveMessage, 1000);
    }
  }
  
  function receiveMessage() {
    var chatBox = document.getElementById("chat-box");
    var messageElement = document.createElement("div");
    messageElement.textContent = "This is a response from the other user.";
    messageElement.classList.add("other-message");
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
  