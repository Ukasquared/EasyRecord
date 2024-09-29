import './styles.css'; 
import './general.css';
import logo from './images/logo.png';
import Img from './images/animatedpeople.png'
import fImg from './images/multitasking-illustration-design.png'
import fImgOne from './images/people-watching-breaking-news-phone.png';
import fImgTwo from './images/freelancers-man-woman-sit-table-with-laptops.png';
// toggle the menu button

let toggleBtn = function () {
    const overLay = document.querySelector(".overlay");
    const menuBar = document.querySelector(".menu-bar");
    if (overLay.classList.contains("overLay") 
        && menuBar.classList.contains("menuBar")) {
            overLay.classList.remove("overLay");
            menuBar.classList.remove("menuBar");
        } else {
            overLay.classList.add("overLay");
            menuBar.classList.add("menuBar");
        }
}

const menuEl= document.querySelector(".menu-btn");
menuEl.addEventListener('click', toggleBtn);

// add logo and style logo
const logoEl = document.querySelector('.logo-image');
const logoImg = document.createElement('img');
logoImg.src = logo;
logoImg.alt = 'logo';
logoImg.style.width = '120px'
logoEl.appendChild(logoImg);

// add the product image
const prodImg = document.querySelector('.animated-img');
const animatedImg = document.createElement('img');
animatedImg.src = Img;
animatedImg.style.width = '35rem';
prodImg.appendChild(animatedImg);


// add feature section image
const featImg = document.querySelector('.center-animation');
const animateImg = document.createElement('img');
animateImg.src = fImg;
featImg.classList.add('feat-img');
featImg.appendChild(animateImg);

// add feat img one
const featImgOne = document.querySelector('.des-feature-one');
const animateImgOne = document.createElement('img');
animateImgOne.src = fImgOne;
animateImgOne.style.width = '25rem'
featImgOne.appendChild(animateImgOne);

// add feature img two
const featImgTwo = document.querySelector('.des-feature-two');
const animateImgTwo = document.createElement('img');
animateImgTwo.src = fImgTwo;
animateImgTwo.style.width = '30rem'
featImgTwo.appendChild(animateImgTwo);