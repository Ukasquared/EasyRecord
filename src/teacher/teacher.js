import './teacher.css';

document.addEventListener("DOMContentLoaded", () => {
    const jwt_token = localStorage.getItem('jwt-token');
        console.log(jwt_token)
        if (!jwt_token) {
            window.location.href='login.html';
        }

    async function teacherData() {
        try {
            const teacherInfo = await fetch('api/teachers_dashboard', {
                method: "GET",
                headers: {
                    'Authorization': `Bearer ${jwt_token}`,
                    'Content-Type': "application/json"
                }
            })
            if (teacherInfo.status === 401) {
                // If token is expired or invalid, redirect to login page
                alert('Session expired. Redirecting to login...');
                localStorage.removeItem('access_token');  // Clear expired token
                window.location.href = '/login.html';  // Redirect to login page
              } 

            const response = await teacherInfo.json();
            console.log(response);
            const rowThree = document.querySelector('.row3');
            rowThree.innerHTML = '';
            const studentDiv = document.querySelector('.student-info');
            Object.entries(response).forEach(([key, value]) => {
                if (key === 'teacher') {
                    Object.entries(value).forEach(([elOne, elTwo]) => {
                        if (elOne === 'photo') {
                            const img = document.createElement('img');
                            img.src = `http://127.0.0.1:5500/api/images/${elTwo}`
                            img.style.width = '20rem'
                            const imgContainer = document.querySelector('.img-container');
                            imgContainer.innerHTML = ''
                            imgContainer.append(img);
                        }else {
                            const pTag = document.createElement('p');
                            pTag.textContent = elTwo;
                            rowThree.append(pTag);
                        }
                        
                    })
                } else {
                    value.forEach((element) => {
                        const new_div = document.createElement('div');
                        new_div.setAttribute('id', 'student_info');
                        const divTag = document.createElement('div');
                        const pOne = document.createElement('span');
                        const pTwo = document.createElement('span');
                        pOne.textContent = element[0];
                        pTwo.textContent = element[1];
                        divTag.textContent = `Names of Students offering ${response.teacher.course}`
                        new_div.append(pOne, pTwo);
                        studentDiv.append(divTag, new_div);
                })
                }
            })
        } catch (error) {
            console.log(error.message);
        }
    }

    teacherData();
    
    async function searchStudent() {

        try {
            const studentName = document.getElementById('first-name').value;
            const response = await fetch('api/search_for_student', {
                method: "POST",
                headers: {
                    'Authorization': `Bearer ${jwt_token}`,
                    'Content-Type': "application/json"
                },
                body: JSON.stringify({
                    'name': studentName,
                })
            })

            if (!response.ok) {
                console.log(response.message);
            }
            const data = await response.json();
            // data returns just one student data
            const searchEl = document.getElementById('display-search');
            const newDiv = document.createElement('div')
            newDiv.setAttribute('class', 'search-el')
            searchEl.appendChild(newDiv);
            Object.entries(data).forEach(([key, value]) => {
                const newEl = document.createElement('div');
                // newEl.setAttribute('class', 'search-el')
                const pOne = document.createElement('p');
                const pTwo = document.createElement('p');
                pOne.textContent = key;
                pTwo.textContent = value;
                newEl.append(pOne, pTwo);
                newDiv.append(newEl);
            })
  
        } catch (error) {
            
        }
    }
    
    const searchBtn = document.getElementById('search-form');
    searchBtn.addEventListener('submit', (e) => {
        e.preventDefault();
        searchStudent();
        searchBtn.reset()
    });
    
    
    async function gradeStudent() {
        // const notice = document.createElement('div');
 
        try {
            const studentScore = document.getElementById('score').value
            const studentId = document.getElementById('student-id').value
            const CourseTitle = document.getElementById('title').value
    
            const response = await fetch('api/grade_student', {
                method: "POST",
                headers: {
                    'Authorization': `Bearer ${jwt_token}`,
                    'Content-Type': "application/json"
                },
                body: JSON.stringify({
                    'id': studentId,
                    'score': studentScore,
                    'title': CourseTitle,
                })
            })
            if (!response.ok) {
                // notice.textContent = data.error;
                alert('grading not successful')
            }
    
            const data = await response.json();
                // notice.textContent = data.message;
            alert(data.message);
            notice.classList.add('notification');

        } catch (error) {
            console.log(error.message);
        }
    }
    
    const gradeForm = document.getElementById('grade');
    gradeForm.addEventListener('submit', (e) => {
        e.preventDefault();
        gradeStudent();
        gradeForm.reset();
    })
})

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

 document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
        const searchBtn = document.getElementById('display-search');
        if (searchBtn.hasChildNodes()) {
            const searchEl = document.querySelector('.search-el');
            searchEl.remove();
        }
    }
 })