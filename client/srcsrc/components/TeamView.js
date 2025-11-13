import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';

const TeamView = () => {
    const [compasses, setCompasses] = useState([]);
    const [error, setError] = useState('');
    const { teamId } = useParams();

    useEffect(() => {
        const fetchCompasses = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await axios.get(`/api/teams/${teamId}/compasses`, {
                    headers: { Authorization: `Bearer ${token}` }
                });
                setCompasses(response.data);
            } catch (err) {
                setError('Failed to fetch compasses for this team.');
            }
        };
        fetchCompasses();
    }, [teamId]);

    return (
        <div>
            <h2>Team Workspace</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <h3>Compasses</h3>
            <ul>
                {compasses.map(compass => (
                    <li key={compass.id}>
                        <Link to={`/compass/${compass.id}`}>{compass.title}</Link>
                        <small> (Last updated: {new Date(compass.updated_at).toLocaleString()})</small>
                    </li>
                ))}
            </ul>
            {/* Link to create a new compass will be added later */}
        </div>
    );
};

export default TeamView;
