import './parent.css';

//fetch the data from the database and display dynamically.
document.addEventListener('DOMContentLoaded', () => {
    const parentData = async () => {
        const jwt_token = localStorage.getItem('jwt-token');
        // console.log(jwt_token)
        if (!jwt_token) {
            window.location.href='login.html';
        }
        try {
            const parentInfo = await fetch('api/parent_dashboard', {
                method: "GET",
                headers: {
                    'Authorization': `Bearer ${jwt_token}`,
                }
            })

            if (parentInfo.status === 401) {
                // If token is expired or invalid, redirect to login page
                alert('Session expired. Redirecting to login...');
                localStorage.removeItem('access_token');  // Clear expired token
                window.location.href = '/login.html';  // Redirect to login page
              } 

            if (!parentInfo.ok) {
                alert('invalid request');
                return;
            }
            const response = await parentInfo.json();
            const parentRow = document.querySelector('.row3');
            parentRow.innerHTML = "";
            Object.entries(response).forEach(([key, values]) => {
                if (key === 'parent') {
                    values.forEach((element) => {
                        const elTwo = document.createElement('p');
                        elTwo.textContent = element;
                        parentRow.append(elTwo);
                    })
                } else if (key === 'student') {
                    const studentDiv = document.querySelector('.student-info');
                    Object.entries(values).forEach(([sub_key, sub_value]) => {
                        if (sub_key === 'course') {
                            // course is an array of dictionary;
                            const newDivOne = document.createElement('div');
                            newDivOne.setAttribute('class', 'course-list');
                            sub_value.forEach((element) => {
                                Object.entries(element).forEach(([key, value]) => {
                                    // const course = `<p>${key}</p><p>${value}</p>`
                                    const newDivTwo = document.createElement('div');
                                    const pOne = document.createElement('p');
                                    const pTwo = document.createElement('p');
                                    pOne.textContent = key;
                                    pTwo.textContent = value;
                                    newDivTwo.append(pOne,pTwo);
                                    newDivOne.append(newDivTwo)
                                })
                            })
                            studentDiv.append(newDivOne);
                        } else {
                            const elTwo = document.createElement('p');
                            elTwo.textContent = sub_value;
                            studentDiv.append(elTwo);
                        }
                    })
                } else {
                    const img = document.createElement('img');
                    img.src = `http://127.0.0.1:5500/api/images/${values}`;
                    img.style.width = '15rem';
                    document.querySelector('.img-container').innerHTML = "";
                    document.querySelector('.img-container').append(img);
                }
    
            })
    
        } catch (error) {
            console.log(error.message);
        }
        
    }

    parentData();
});

const logOut = document.getElementById('logout');

 logOut.onclick = async function () {
    try {
        const response = await fetch('api/logout', {
            method: "DELETE"
        });
        if (!response.ok){
            alert('failed to logout');
        }
        
        window.location.replace('/login.html');  // Redirect to login page

    } catch (error) {
        console.log(error.message);
    }
 }