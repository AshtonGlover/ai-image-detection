const fileInput = document.getElementById('fileInput');
const uploadedImage = document.getElementById('uploadedImage');
const submitBtn = document.getElementById('submitBtn');
let selectedFile = null;

fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        selectedFile = file

        const reader = new FileReader();
        reader.onload = function(e) {
            uploadedImage.src = e.target.result;
            uploadedImage.style.display = 'block';
            submitBtn.style.display = 'block';
        };

        reader.readAsDataURL(file);
    } else {
        file = null;
        uploadedImage.style.display = 'none'; 
    }
});

submitBtn.addEventListener('click', async function() {
    if (selectedFile) {
        const formData = new FormData();
        formData.append('image', selectedFile);

        await fetch('http://127.0.0.1:5000/api/upload_image', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });

        setResult()
    }
});

async function setResult() {
    await fetch('http://127.0.0.1:5000/api/get_decision')
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            const resultTag = document.getElementById("result");
            resultTag.style.display = 'block';
            resultTag.textContent = data.result ? "REAL" : "FAKE";
        })
        .catch(error => {
            console.error('Error:', error);
        });
}