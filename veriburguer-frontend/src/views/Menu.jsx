import  Carrusel  from  './components/CarrouselSucursales'
import { NavBar } from './components/NavBar'
import  Footer  from  './components/footer'
import  MenuCards  from  './components/cardsMenu'



function menu(){
    return(
        <div className="menu">
            <NavBar></NavBar>
            <Carrusel></Carrusel>
            <MenuCards></MenuCards>
            <Footer></Footer>
            
        </div>
        
    )
}


export default menu;