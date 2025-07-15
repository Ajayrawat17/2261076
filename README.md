# 🧠 AffordMed Custom URL Shortener

A simple, secure, and customizable URL shortener built with **Django REST Framework**, **MongoDB**, and **ReactJS**.  
Users can create short URLs with custom codes, set expiration time, and track click statistics.

---

## 🚀 Features

- ✅ Shorten any long URL
- 🔒 Secure with Bearer Token Authorization
- 🕐 Set custom expiry time (in minutes)
- 🔢 Custom shortcode (optional)
- 📊 Get stats: total clicks, IP address, timestamp, etc.
- 🌐 Frontend built with React
- ☁️ Backend using Django + MongoDB Atlas

---

## 🛠️ Tech Stack

| Frontend       | Backend         | Database     |
|----------------|------------------|--------------|
| ReactJS        | Django REST API  | MongoDB Atlas |

---

## 📁 Project Structure
/frontend
└── src
├── components/
│ ├── CreateURLForm.jsx
│ ├── ShowShortResult.jsx
│ └── CheckStats.jsx
├── App.jsx
├── api.js
└── index.js

/backend
├── core/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── middleware.py
├── backend/
│ └── settings.py
└── manage.py

yaml
Copy
Edit

---

## ⚙️ How to Run Locally

### Backend

```bash
cd backend
pip install -r requirements.txt
python manage.py runserver
Frontend
bash
Copy
Edit
cd frontend
npm install
npm start



Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJhamF5cmF3YXQxMTE0NkBnbWFpbC5jb20iLCJleHAiOjE3NTI1NTc4MTAsImlhdCI6MTc1MjU1NjkxMCwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6ImE3ZmUzNTdjLTljNmQtNGFlYS1hMjE2LWY1YjEzOWJlZmY2OCIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6ImFqYXkgcmF3YXQiLCJzdWIiOiI4OGI3NWNkMC0yNGZhLTQ2NWYtOTdmNC1lZjU1MGI3MjZkNjQifSwiZW1haWwiOiJhamF5cmF3YXQxMTE0NkBnbWFpbC5jb20iLCJuYW1lIjoiYWpheSByYXdhdCIsInJvbGxObyI6IjIyNjEwNzYiLCJhY2Nlc3NDb2RlIjoiUUFoRFVyIiwiY2xpZW50SUQiOiI4OGI3NWNkMC0yNGZhLTQ2NWYtOTdmNC1lZjU1MGI3MjZkNjQiLCJjbGllbnRTZWNyZXQiOiJiY0dxZUNkTkZrS0JXTUd0In0.FZIdl8LfPq6J7DScusF2ABFBG05Vm5ZqnP-HM9IFgW4


🌐 API Endpoints
Method	Endpoint	Description
POST	/shorturls/	Create short URL
GET	/shorturls/{shortcode}/	Get stats for a shortcode
GET	/shorturls/go/{shortcode}/	Redirect to original URL

📦 Deployment (Optional)
Backend: Render / Railway

Frontend: Netlify / Vercel

Database: MongoDB Atlas

🙋‍♂️ Author
Ajay Rawat
Email: ajayrawat11146@gmail.com
GitHub: Ajayrawat17

