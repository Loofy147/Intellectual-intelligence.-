document.addEventListener('DOMContentLoaded', () => {
    const saveBtn = document.getElementById('save-btn');
    const loadBtn = document.getElementById('load-btn');

    const textareas = {
        q1: document.getElementById('q1'),
        q2: document.getElementById('q2'),
        q3: document.getElementById('q3'),
        ac1: document.getElementById('ac1'),
        ac2: document.getElementById('ac2'),
        le1: document.getElementById('le1'),
        le2: document.getElementById('le2'),
        le3: document.getElementById('le3'),
    };

    saveBtn.addEventListener('click', () => {
        const data = {};
        for (const id in textareas) {
            data[id] = textareas[id].value;
        }

        const jsonData = JSON.stringify(data, null, 2);
        const blob = new Blob([jsonData], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'pragmatic-compass.json';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });

    loadBtn.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (!file) {
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const data = JSON.parse(e.target.result);
                for (const id in data) {
                    if (textareas[id]) {
                        textareas[id].value = data[id];
                    }
                }
            } catch (error) {
                alert('Error reading or parsing the JSON file.');
                console.error(error);
            }
        };
        reader.readAsText(file);
    });
});
