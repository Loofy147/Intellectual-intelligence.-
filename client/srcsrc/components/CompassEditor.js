import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const CompassEditor = () => {
    const [title, setTitle] = useState('');
    const [data, setData] = useState({ q1: '', q2: '', q3: '', ac1: '', ac2: '', le1: '', le2: '', le3: '' });
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const { compassId } = useParams();

    useEffect(() => {
        const fetchCompass = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await axios.get(`/api/compasses/${compassId}`, {
                    headers: { Authorization: `Bearer ${token}` }
                });
                setTitle(response.data.title);
                setData(response.data.data);
            } catch (err) {
                setError('Failed to load the compass data.');
            }
        };
        fetchCompass();
    }, [compassId]);

    const handleDataChange = (e) => {
        setData({ ...data, [e.target.id]: e.target.value });
    };

    const handleSave = async () => {
        try {
            const token = localStorage.getItem('token');
            await axios.put(`/api/compasses/${compassId}`, { title, data }, {
                headers: { Authorization: `Bearer ${token}` }
            });
            setSuccess('Compass saved successfully!');
            setError('');
        } catch (err) {
            setError('Failed to save the compass.');
            setSuccess('');
        }
    };

    return (
        <div>
            <h2>Compass Editor</h2>
            <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} style={{fontSize: '1.5em', marginBottom: '20px'}} />
            <button onClick={handleSave} style={{marginLeft: '20px'}}>Save</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {success && <p style={{ color: 'green' }}>{success}</p>}

            <section>
                <h3>The Three Questions</h3>
                <textarea id="q1" value={data.q1} onChange={handleDataChange} placeholder="Market dislocation..."></textarea>
                <textarea id="q2" value={data.q2} onChange={handleDataChange} placeholder="Asymmetric advantage..."></textarea>
                <textarea id="q3" value={data.q3} onChange={handleDataChange} placeholder="GTM risk..."></textarea>
            </section>
            <section>
                <h3>The Adversarial Check</h3>
                <textarea id="ac1" value={data.ac1} onChange={handleDataChange} placeholder="Pre-mortem headline..."></textarea>
                <textarea id="ac2" value={data.ac2} onChange={handleDataChange} placeholder="Kill strategy..."></textarea>
            </section>
            <section>
                <h3>The Lean Experiment</h3>
                <textarea id="le1" value={data.le1} onChange={handleDataChange} placeholder="Riskiest assumption..."></textarea>
                <textarea id="le2" value={data.le2} onChange={handleDataChange} placeholder="Cheapest, fastest way..."></textarea>
                <textarea id="le3" value={data.le3} onChange={handleDataChange} placeholder="Quantifiable signal..."></textarea>
            </section>
        </div>
    );
};

export default CompassEditor;
