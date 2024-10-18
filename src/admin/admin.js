import "./admin.css";


document.addEventListener("DOMContentLoaded", () => {
    const jwt_token = localStorage.getItem('jwt_token');

    
    async function loadAdmin() {
        if (!jwt_token) {
            window.location.href='login.html'
        }
    
        const response = await fetch('api//admin_dashboard', {
            method: "POST",
             headers: {
                 'Authorization': `Bearer ${jwt_token}`
             },
        });
        const admin_info = await response.json();

        // display user data
        document.querySelector('.uuid').innerHTML = admin_info.admin_info;
        document.querySelector('.fname').innerHTML = admin_info.firstname;
        document.querySelector('.lname').innerHTML = admin_info.lastname;
        document.querySelector('.email').innerHTML = admin_info.email;
        document.querySelector('.gender').innerHTML = admin_info.gender;

         // display total student and teacher
        document.querySelector('.student').innerHTML = admin_info.total_student;
        document.querySelector('.teacher').innerHTML = admin_info.total_teacher;

        // display image
        const imageDiv  =  document.querySelector('.admin-info');
        const image = document.createElement('img');
        image.src = admin_info.photo;
        image.style.display = 'block';
        imageDiv.appendChild(image);

        // display course
        const course = document.querySelector('.course-id-name');
        const courses = admin_info.courses_with_id;
        courses.forEach(element => {
            const div = createElement('div');
            element.forEach(element => {
                const para = createElement('p');
                para.textContent = element;
                div.appendChild(para);
            })
            course.appendChild(div);
            
        });
     }
     
     loadAdmin();
 });
