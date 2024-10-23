import './teacher.css';


document.addEventListener("DOMContentLoaded", () => {
    const jwt_token = localStorage.getItem('jwt-token');
        // console.log(jwt_token)
        if (!jwt_token) {
            window.location.href='login.html';
        }

    async function teacherData() {
        try {
            const teacherInfo = await fetch('/teachers_dashboard', {
                method: "POST",
                headers: {
                    'Authorization': `Bearer ${jwt_token}`
                }
            })
            const response = await teacherInfo.json();
            const rowThree = document.querySelector('.row3');
            rowThree.innerHTML = '';
            const studentDiv = document.querySelector('.student-info');
            Object.entries(response).forEach(([key, value]) => {
                if (key === 'teacher') {
                    Object.entries(value).forEach(([elOne, elTwo]) => {
                        if (elOne === 'photo') {
                            const img = document.createElement('img');
                            img.src = `http://127.0.0.1:5500/api/images/${elTwo}`
                            document.querySelector('.img-container');
                        }
                        const pTag = document.createElement('p');
                        pTag.textContent = elTwo;
                        rowThree.append(pTag);
                    })
                }
                value.forEach((element) => {
                    const new_div = document.createElement('div');
                    new_div.setAttribute('id', 'student_info');
                    const pOne = document.createElement('p');
                    const pTwo = document.createElement('p');
                    pOne.textContent = element[0];
                    pTwo.textContent = element[1];
                    new_div.append(pOne,pTwo);
                    studentDiv.append(new_div);
                })
            })
        } catch (error) {
            console.log(error.message);
        }
    }

    teacherData();
        
})

async function searchStudent() {
    const studentName = document.getElementById('first-name').value;
    
    const response = await fetch('/search_for_student', {
        method: "POST",
        body: JSON.stringify({
            'name': studentName,
        })
    })
    const data = await response.json();
    // data returns just one student data
    const searchEl = document.querySelector('.display-search')
    Object.entries(data).forEach(([key, value]) => {
        const newEl = document.createElement('div');
        const pOne = document.createElement('p');
        const pTwo = document.createElement('p');
        pOne.textContent = key;
        pTwo.textContent = value;
        newEl.append(pOne, pTwo);
        searchEl.append(newEl);
    })
}

const searchBtn = document.querySelector('.fa-solid');
searchBtn.addEventListener('click', () => searchStudent);


 async function gradeStudent() {

    const notice = document.querySelector('.notification');

    try {
        const studentScore = document.getElementById('score').value
        const studentId = document.getElementById('student-id').value
        const CourseTitle = document.getElementById('title').value

        const response = await fetch('/grade_student', {
            method: "POST",
            body: JSON.stringify({
                'id': studentId,
                'score': studentScore,
                'title': CourseTitle,
            })
        })
        const data = await response.json();

        if (!response.ok) {
            notice.textContent = data.error;
        }else {
            notice.textContent = data.message;
        }
        notice.style.display = 'block';
    } catch (error) {
        console.log(error.message);
    }
}

const gradeForm = document.getElementById('grade');
gradeForm.addEventListener('submit', () => gradeStudent);