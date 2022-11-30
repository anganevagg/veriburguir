import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import image1 from "../assets/location.png"
import  Carrusel  from  './components/CarrouselSucursales'
import { NavBar } from './components/NavBar'
import  Footer  from  './components/footer'

function locations() {
  return (
    <>
      <Card>
        <Card.Img variant="top" src={{image1}} />
        <Card.Body>
          <Card.Text>
            Nos ubicamos en esquina con carrilo
            Puerto 48, y con Abarrotes Mendoza
            Ven a visitarnos!!!!
          </Card.Text>
        </Card.Body>
      </Card>
      <Button variant="primary">Llamar</Button>{' '}
      
    </>
  );
}

export default locations;