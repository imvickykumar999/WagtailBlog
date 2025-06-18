const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files (css, js, images, etc.)
app.use(express.static(path.join(__dirname)));

// Routes
app.get('/', (req, res) => res.sendFile(path.join(__dirname, 'index.html')));
app.get('/about', (req, res) => res.sendFile(path.join(__dirname, 'about.html')));
app.get('/contact', (req, res) => res.sendFile(path.join(__dirname, 'contact.html')));
app.get('/post', (req, res) => res.sendFile(path.join(__dirname, 'post.html')));

// Start server
app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));
