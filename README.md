# HPE IT Solutions

A modern, responsive web application for HPE IT Solutions, showcasing enterprise IT services, infrastructure solutions, workforce management, and project portfolios.

## 🚀 Features

- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Interactive Maps**: Location-based contact information using Leaflet
- **Dynamic Animations**: Smooth transitions with Framer Motion
- **Contact Management**: Backend API for handling contact form submissions
- **Admin Dashboard**: Administrative interface for managing content
- **Project Showcase**: Portfolio of completed IT projects and solutions

## 🛠️ Tech Stack

### Frontend
- **React 18** - Modern JavaScript library for building user interfaces
- **Vite** - Fast build tool and development server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router** - Client-side routing
- **Framer Motion** - Animation library
- **Leaflet** - Interactive maps
- **Axios** - HTTP client for API calls

### Backend
- **Flask** - Lightweight Python web framework
- **MongoDB Atlas** - Cloud database for data storage
- **Flask-CORS** - Cross-origin resource sharing
- **Flasgger** - API documentation

## 📋 Prerequisites

- Node.js (v16 or higher)
- Python (v3.8 or higher)
- MongoDB Atlas account (for database)

## 🏃‍♂️ Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```bash
   python app.py
   ```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will run on `http://localhost:5173`

## 📁 Project Structure

```
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── index.html          # Backend template
├── frontend/
│   ├── public/             # Static assets
│   ├── src/
│   │   ├── components/     # Reusable React components
│   │   ├── pages/          # Page components
│   │   ├── context/        # React context providers
│   │   ├── data/           # Static data files
│   │   └── projects/       # Project data
│   ├── package.json        # Node dependencies
│   └── vite.config.js      # Vite configuration
└── README.md
```

## 🔧 Available Scripts

### Frontend
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Backend
- `python app.py` - Start Flask development server

## 🌐 API Endpoints

- `GET /api/contacts/all` - Retrieve all contact submissions
- `POST /api/contacts` - Submit new contact form
- `GET /` - Serve homepage

## 📧 Contact

For questions or support, please use the contact form on the website or reach out to the development team.

## 📄 License

This project is proprietary to HPE IT Solutions.
