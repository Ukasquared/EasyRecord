import './signup.css';

const form = document.querySelector('.form-signup');

async function sendFormData() {
    const formData = new FormData(form);
    console.log(formData)
    try {
        const response = await fetch('api/signup', {
            method: "POST",
            body: formData
        });
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
          }
      
        const res = await response.json();
        console.log(res.message)
        window.location.replace('/login.html');
        // alert("registered successfully with ID " + res.message);

    } catch (error) {
        console.log(error.message);
    }
}

form.addEventListener("submit", function(e) {
    // e = event object
    e.preventDefault();
    sendFormData();
    
})
