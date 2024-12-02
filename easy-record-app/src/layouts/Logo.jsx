// import { ReactComponent as LogoDark } from "../assets/images/logos/materialpro.svg";
// import { logo } from "../assets/images/logos/materialpro.svg";
import { Link } from "react-router-dom";
// import "../assets/css/styles.css";

const Logo = () => {
  return (
    <Link to="/">
      {/* <img src={logo} className="main-logo" alt="logo" /> */}
      <span className="logo">easyrecord</span>
    </Link>
  );
};

export default Logo;
