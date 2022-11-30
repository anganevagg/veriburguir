import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import image1 from "../assets/menu1.jpg"
import image2 from "../assets/menu2.jpg"
import image3 from "../assets/menu3.jpg"
import image4 from "../assets/menu4.jpg"

function MenuCards() {
  return (
    <MenuCards>
        <Card style={{ width: '18rem' }}>
            <Card.Img variant="top" src={image1}/>
            <Card.Body>
                <Card.Title>MAMÁ OSA</Card.Title>
                <Card.Text>
                    Hamburguesa sencilla, todos se la comen
                </Card.Text>
                <Button variant="primary">Ver más</Button>
            </Card.Body>
        </Card>
        
        <Card style={{ width: '18rem' }}>
            <Card.Img variant="top" src={image2}/>
            <Card.Body>
                <Card.Title>T-1000</Card.Title>
                <Card.Text>
                    Especialidad de la casa
                    te pega sino la disfrutas
                    viene con rol de t-1000
                </Card.Text>
                <Button variant="primary">Ver más</Button>
            </Card.Body>
        </Card>
         
        <Card style={{ width: '18rem' }}>
            <Card.Img variant="top" src={image3}/>
            <Card.Body>
                <Card.Title>CRI-CRI</Card.Title>
                <Card.Text>
                    Ideal para comer en pareja
                    si traes a la novia de tu amigo te 
                    hacemos un descuento especial
                </Card.Text>
                <Button variant="primary">Ver más</Button>
            </Card.Body>
        </Card>
         
        <Card style={{ width: '18rem' }}>
            <Card.Img variant="top" src={image4}/>
            <Card.Body>
                <Card.Title>MANI MANITO</Card.Title>
                <Card.Text>
                    Viene sin papas, pero con un
                    buen ambiente combinado
                </Card.Text>
                <Button variant="primary">Ver más</Button>
            </Card.Body>
        </Card>
    </MenuCards>
    
    
  );
}

export default MenuCards;