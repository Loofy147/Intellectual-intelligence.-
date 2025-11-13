import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Dashboard = () => {
    const [teams, setTeams] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchTeams = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await axios.get('/api/teams', {
                    headers: { Authorization: `Bearer ${token}` }
                });
                setTeams(response.data);
            } catch (err) {
                setError('Failed to fetch teams.');
            }
        };
        fetchTeams();
    }, []);

    return (
        <div>
            <h2>Dashboard</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <h3>Your Teams</h3>
            <ul>
                {teams.map(team => (
                    <li key={team.id}>
                        <Link to={`/team/${team.id}`}>{team.team_name}</Link>
                    </li>
                ))}
            </ul>
            {/* Link to create a new team will be added later */}
        </div>
    );
};

export default Dashboard;
