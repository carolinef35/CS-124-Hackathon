import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [subject, setSubject] = useState('math');
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const subjects = ['math', 'science', 'history', 'english'];

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { sender: 'user', text: input }];
    setMessages(newMessages);
    setInput('');

    try {
      const response = await axios.post('http://localhost:8000/api/chat', {
        message: input,
        subject: subject,
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });

      const botReply = response.data.response;
      setMessages([...newMessages, { sender: 'bot', text: botReply }]);
    } catch (error) {
      console.error('Error:', error);
      console.error('Error Message: ', error.message)
      setMessages([...newMessages, { sender: 'bot', text: 'Failed to get a response' }]);
    }
  };

  const handleInputChange = (e) => setInput(e.target.value);

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') sendMessage();
  };

  const handleSubjectChange = (subject) => {
    setSubject(subject);
    setMessages([]);
  };

  return (
    <div className="App">
      <header className = "App-header">
        <img 
          src={`${process.env.PUBLIC_URL}/LearnLionNewLogo.png`}
          alt="LearnLion"
          className="learn-lion-logo"
        />
        <h1>Welcome to LearnLion</h1>
      </header>
      <div className="subject-buttons">
        {subjects.map((subj) => (
          <button
            key={subj}
            className={subject === subj ? 'active' : ''}
            onClick={() => handleSubjectChange(subj)}
          >
            {subj.charAt(0).toUpperCase() + subj.slice(1)}
          </button>
        ))}
      </div>

      <div className="chat-container">
        <div className="chat-box">
          {messages.map((msg, index) => (
            <div key={index} className={msg.sender === 'user' ? 'user-message' : 'bot-message'}>
              {msg.text}
            </div>
          ))}
        </div>
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          onKeyPress={handleKeyPress}
          placeholder="Ask me anything..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
