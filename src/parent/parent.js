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
            const parentInfo = await fetch('/parent_dashboard', {
                method: "POST",
                headers: {
                    'Authorization': `Bearer ${jwt_token}`
                }
            })
            const response = await parentInfo.json();
            Object.entries(response).forEach(([key, values]) => {
                const elOne = document.querySelector('.row3');
                if (key === 'parent') {
                    Object.entries(values).forEach(([sub_key, sub_value]) => {
                        if (sub_key == 'photo') {
                            const img = document.createElement('img');
                            img.src = `http://127.0.0.1:5500/api/images/${sub_value}`
                            document.querySelector('.img-container');
                        }
                        const elTwo = document.createElement('p');
                        elTwo.textContent = sub_value;
                        elOne.append(elTwo);
                    })
                }
                if (key === 'student') {
                    const studentDiv = document.querySelector('student-info')
                    Object.entries(values).forEach(([sub_key, sub_value]) => {
                        const elTwo = document.createElement('p');
                        elTwo.textContent = sub_value;
                        studentDiv.append(elTwo);
                        if (sub_key === 'course') {
                            // course is an array of dictionary;
                            const new_div = document.createElement('div');
                            new_div.setAttribute('class', 'course-list');
                            sub_key.forEach((element) => {
                                Object.entries(element).forEach(([key, value]) => {
                                    // const course = `<p>${key}</p><p>${value}</p>`
                                    const pOne = document.createElement('p');
                                    const pTwo = document.createElement('p');
                                    pOne.textContent = key;
                                    pTwo.textContent = value;
                                    new_div.append(pOne,pTwo);
                                })
                            })
                            studentDiv.append(new_div);
                        }
                    })
                }
    
            })
    
        } catch (error) {
            console.log(error.message);
        }
        
    }

    parentData();
});