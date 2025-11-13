import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import TeamView from './components/TeamView';
import CompassEditor from './components/CompassEditor';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/register">Register</Link></li>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/dashboard">Dashboard</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />

          <Route path="/dashboard" element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          } />
          <Route path="/team/:teamId" element={
            <ProtectedRoute>
              <TeamView />
            </ProtectedRoute>
          } />
          <Route path="/compass/:compassId" element={
            <ProtectedRoute>
              <CompassEditor />
            </ProtectedRoute>
          } />

          <Route path="/" element={<h1>Welcome to Archon V1</h1>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
