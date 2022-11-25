import {Navbar, Nav, Container} from "react-bootstrap"
import image from "../assets/hamburguesa-con-queso.png"


export function NavBar() {
	return (
		<Navbar style={{backgroundColor: "#1A0302"}} variant="dark">
			<div className="mx-auto">
				<Nav className="me-auto">
					<Nav.Link href="#menu">Menu</Nav.Link>
					<Nav.Link href="#places">Sucursales</Nav.Link>
					<Nav.Link href="#galery">Galeria</Nav.Link>
					<Nav.Link href="#reserve">Reservación</Nav.Link>
				</Nav>
			</div>
		</Navbar>
	)
}