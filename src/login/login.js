import './styles.css';

const form = document.querySelector('.form-1');
// login
async function sendData() {
    // const role = document.getElementById('myDropdown').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const log = document.querySelector('.display');
    try {
        const response = await fetch('api/login', {
            method: "POST",
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify({
                "email": email,
                "password": password,
            }),
        });
        if (!response.ok) {
            log.innerHTML = 'login failed';
            log.classList.add('log');
            throw new Error('login failed');
        }
        const access_token = await response.json();
        const role = access_token.role
        console.log(access_token);
        console.log(role)
        let path = "";
        if (role === 'admin' ) {
            path = '/admin.html';
        } else if (role === 'parent') {
            path = '/parent.html';
        } else if (role === 'teacher') {
            path =  '/teacher.html';
        }
        if (access_token.token) {
          localStorage.setItem('jwt-token', access_token.token);
          console.log(access_token.token)
          window.location.replace(path);
        } else {
            log.innerHTML = 'login failed';
            log.classList.add('log');
            throw new Error('login failed');
        }
    } catch (error) {
        console.log(error.message);
    }
}   


form.addEventListener('submit', (e) => {
    e.preventDefault();
    sendData();
})