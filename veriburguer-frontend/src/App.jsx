import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.css'
import { NavBar } from './components/NavBar'
import  Carrusel  from  './components/Carrousel'

function App() {
  return (
    <div className="App">
			<NavBar></NavBar>
     <Carrusel></Carrusel>
    </div>
  )
}

export default App
