import { Button } from "./button.jsx";
import { Nav } from "./nav.jsx"
import '../assets/css/styles.css'

function Hero() {

    return (
        <div className="hero-bg">
            <div>
                <Nav />
            </div>
            <div>
                <div className="hero-note">
                    <p>Lorem ipsum dolor sit amet 
                        consectetur adipisicing elit. 
                        Voluptates voluptatibus corrupti 
                        ducimus nihil nemo earum.</p>
                    <Button text="Readmore" />
                </div>
                <div className="hero-img">
                </div>
            </div>
        </div>
    )

}