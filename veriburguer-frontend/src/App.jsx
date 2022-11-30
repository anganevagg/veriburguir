import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.css'
import { NavBar } from './components/NavBar'
import  Carrusel  from  './components/Carrousel'
import  Footer  from  './components/footer'

function App() {
  return (
    <div className="App">
			<NavBar></NavBar>
     <Carrusel></Carrusel>
     <Footer></Footer>
    </div>
  )
}

export default App
