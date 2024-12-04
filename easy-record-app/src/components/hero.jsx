import Button from "./button.jsx";
import Navigation from "./nav.jsx"
import '../assets/css/styles.css'
import heroBg from '../assets/images/bg/hero-bg.png';
import heroImg from '../assets/images/bg/animatedpeople.png';

function Hero() {

    return (
        <div className="hero">
            <div className="img-container">
                <img src={heroBg} alt="" /> 
            </div>
            <div className="navigation">
                <Navigation />
            </div>
            <div className="container hero-note">
                <div className="row">
                    <div className="col-md-6 product-summary">
                    <h1>Manage Your School Work-flow <br/> with ease</h1>
                    <p>Easy record is free school management software<br/>that
                        replicates the daily activities of a school.
                    </p>
                    <Button text="Request for a trial &rarr;" />
                    </div>
                    <div className="col-6 hero-img">
                    <img src={heroImg} alt=""/>
                    </div>                       
                </div>
               
            </div>
        </div>
    )

}

export default Hero