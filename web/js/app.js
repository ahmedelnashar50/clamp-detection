async function uploadAndAnalyze() {
    const fileInput = document.getElementById('videoInput');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const loader = document.getElementById('loader');
    const inputVid = document.getElementById('inputVid');
    const outputVid = document.getElementById('outputVid');

    if (!fileInput.files[0]) return alert("Please select a video file!");

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    inputVid.src = URL.createObjectURL(fileInput.files[0]);

    analyzeBtn.disabled = true;
    loader.classList.remove('hidden');

    try {
        const response = await fetch('http://127.0.0.1:8000/analyze', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        
        if (data.status === 'success') {
            outputVid.src = data.video_url + "?t=" + new Date().getTime();
            outputVid.load();
            outputVid.play();
        } else {
            alert("Error: " + data.message);
        }
    } catch (err) {
        console.error(err);
        alert("Failed to connect to server.");
    } finally {
        analyzeBtn.disabled = false;
        loader.classList.add('hidden');
    }
}