import  { Carrusel }  from  '../components/CarrouselSucursales'
import { NavBar } from '../components/NavBar'
import  Footer  from  '../components/footer'
import  MenuCards  from  '../components/cardsMenu'

export function Menu(){
    return(
        <div className="menu">
            <Carrusel></Carrusel>
            <MenuCards></MenuCards>
            <Footer></Footer>
        </div>
        
    )
}
