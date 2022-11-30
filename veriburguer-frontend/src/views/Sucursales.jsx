import  Carrusel  from  '../components/CarrouselSucursales'
import { NavBar } from '../components/NavBar'
import  Footer  from  '../components/footer'
import  locations  from  '../components/locations'

function showSucursales(){
    return (
        <showSucursales>
            <NavBar></NavBar>
            <Carrusel></Carrusel>
            <locations></locations>
            <Footer></Footer>
        </showSucursales>
    )
}

export default showSucursales;