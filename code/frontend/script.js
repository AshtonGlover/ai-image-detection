const fileInput = document.getElementById('fileInput');
const uploadedImage = document.getElementById('uploadedImage');
const submitBtn = document.getElementById('submitBtn');

fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            uploadedImage.src = e.target.result;
            uploadedImage.style.display = 'block';
            submitBtn.style.display = 'block';
        };

        reader.readAsDataURL(file);
    } else {
        uploadedImage.style.display = 'none'; 
    }
});

submitBtn.addEventListener('click', function() {
    if (uploadedImage) {
        const formData = new FormData();
        formData.append('image', uploadedImage);

        fetch('http://127.0.0.1:5000/api/upload_image', {
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

function setResult() {
    document.getElementById("result").textContent = "rah";
}