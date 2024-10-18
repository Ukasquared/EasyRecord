import './styles.css';

const form = document.querySelector('.form-1');
// login
async function sendData() {
    const role = document.getElementById('myDropdown').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('api/login', {
            method: "POST",
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify({
                "email": email,
                "role": role,
                "password": password,
            }),
        });
        if (!response.ok) {
            const log = document.querySelector('.display');
            log.innerHTML = 'login failed';
            log.classList.add('log')
            throw new Error('login failed');
        }
        const access_token = await response.json();
        console.log(access_token)
        let path = "";
        if (role === 'admin' ) {
            path = '/admin.html';
        } else if (role === 'parent') {
            path = 'parent.html';
        } else if (role === 'teacher') {
            path =  'teacher.html';
        }
        if (access_token.token) {
          localStorage.setItem('jwt-token', access_token.token);
          window.location.href=path
        }
        else {
            

        }
    } catch (error) {
        console.log(error.message);
    }
}


form.addEventListener('submit', (e) => {
    e.preventDefault();
    sendData();
})