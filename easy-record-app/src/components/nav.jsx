import { useState } from "react"
import Logo from "../layouts/Logo"

import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';

function Navigation(args) {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);

  return (
    
    <div>
      <Navbar {...args} expand="md" >
        <NavbarBrand href="/"><Logo/></NavbarBrand>
        <NavbarToggler onClick={toggle}/>
        <Collapse isOpen={isOpen} className="nav-colapse" style={{flexGrow: "0"}} navbar>
          <Nav className="" navbar>
              <NavItem className="nav-padding">
                <NavLink href="/components/">About</NavLink>
              </NavItem>
              <NavItem className="nav-padding">
                <NavLink href="https://github.com/reactstrap/reactstrap">
                  Product
                </NavLink>
              </NavItem>
              <NavItem className="nav-padding">
                <NavLink href="https://github.com/reactstrap/reactstrap">
                  Contact
                </NavLink>
              </NavItem >
              <NavItem className="nav-padding">
                <NavLink href="https://github.com/reactstrap/reactstrap">
                  Register
                </NavLink>
              </NavItem>
              <NavItem className="nav-padding">
                <NavLink href="https://github.com/reactstrap/reactstrap">
                  Log In
                </NavLink>
              </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
}

export default Navigation;