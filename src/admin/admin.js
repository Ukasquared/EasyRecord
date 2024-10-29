import "./admin.css";


document.addEventListener("DOMContentLoaded", () => {
    const jwt_token = localStorage.getItem('jwt-token');
    console.log(jwt_token)

    
    async function loadAdmin() {
        if (!jwt_token) {
            window.location.href='login.html'
        }
        try {
            const response = await fetch('api/admin_dashboard', {
                method: "POST",
                 headers: {
                     'Authorization': `Bearer ${jwt_token}`
                 },
            });
            const admin_info = await response.json();
            console.log(admin_info)
    
            // display user data
            document.querySelector('.uuid').innerHTML = admin_info.id;
            document.querySelector('.fname').innerHTML = `${admin_info.firstname} ${admin_info.lastname}`;
            document.querySelector('.email').innerHTML = admin_info.email;
            document.querySelector('.gender').innerHTML = admin_info.gender;
    
             // display total student and teacher
            document.querySelector('.student').innerHTML = admin_info.total_student;
            document.querySelector('.teacher').innerHTML = admin_info.total_teacher;
    
            // display image
            const imageDiv  =  document.querySelector('.img-container');
            const image = document.createElement('img');
            imageDiv.innerHTML = '';
            image.src = `http://127.0.0.1:5500/api/images/${admin_info.photo}`;
            image.style.display = 'block';
            image.style.width = '15rem'
            imageDiv.appendChild(image);
    
            // // display course
            // const course = document.querySelector('.course-id-name');
            // const courses = admin_info.courses_with_id;
            // courses.forEach(element => {
            //     const div = createElement('div');
            //     element.forEach(element => {
            //         const para = createElement('p');
            //         para.textContent = element;
            //         div.appendChild(para);
            //     })
            //     course.appendChild(div);  
            // });
        } catch (error) {
            console.log(error.message)   
        }
        
     }
     
     loadAdmin();
     

    // sign up
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
                alert('registration failed');
                throw new Error(`Response status: ${response.status}`);
            }
            
            const res = await response.json();
            console.log(res.message)
            alert("registered successfully with ID " + res.message);

        } catch (error) {
            console.log(error.message);
        }
    }

    form.addEventListener("submit", function(e) {
        // e = event object
        e.preventDefault();
        sendFormData();
        form.reset()
    })

    // register a course
    const courseForm = document.getElementById('enroll-course');

    const courseData = async () => {
        const title = document.getElementById('title').value;
        const teacherID = document.getElementById('teacher_id').value;
        const adminID= document.getElementById('adminid').value;
        try {

            const response = await fetch('api/register_a_course', {
                method: "POST",
                headers: {
                    'Content-Type': "application/json",
                    'Authorization': `Bearer ${jwt_token}`
                },
                body: JSON.stringify({
                    'title': title,
                    'teacher_id': teacherID,
                    'admin_id': adminID,
                }),
            });
                
            if (!response.ok) {
                alert('course not yet registered');
                console.log('course not yet registered' + response.status);
            }
            const data = await response.json();
            console.log(data);
            alert('course created succesfully with ID' + data)
        } catch (error) {
            console.log(error.message);
        }
            
        }

    courseForm.addEventListener('submit', (e) => {
        e.preventDefault();
        courseData()
        courseForm.reset();
    })

    // register a student in a course
    const regStud = document.getElementById('enroll-student');

    async function regStudCourse() {
        const studentID = document.getElementById('studentid').value;
        const courseID = document.getElementById('course_id').value;
        // const teacherID = document.getElementById('teacherid').value;

        const response = await fetch('api/enroll_student_in_course', {
            method: "POST",
            headers: {
                'Content-Type': "application/json",
                'Authorization': `Bearer ${jwt_token}`
            },
            body: JSON.stringify({
                'student_id': studentID,
                'course_id': courseID,
            }),
        })

        if (response.status === 404) {
            const error = await response.json();
            console.log(error.error);
            return;
        }

        if (response.status === 401) {
            // If token is expired or invalid, redirect to login page
            alert('Session expired. Redirecting to login...');
            localStorage.removeItem('access_token');  // Clear expired token
            window.location.href = '/login.html';  // Redirect to login page
          } 

        if (!response.ok) {
            alert('unable to enroll student into a course');
            console.log('not successful');
            return;
        }

        const data = await response.json();
        console.log(data.message);
    }

    regStud.addEventListener('submit', (e) => {
        e.preventDefault();
        regStudCourse();
        regStud.reset();
    })
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