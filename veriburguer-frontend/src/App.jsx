import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.css'
import { NavBar } from './components/NavBar'
import { Landing } from './views/Landing'
import { Orders } from './views/Orders'
import  { Carrusel }  from  './components/Carrousel'
import  Footer  from  './components/footer'
import { Menu } from "./views/Menu"

function App() {
	return (
		<div className="App">
			<NavBar></NavBar>
			<Menu></Menu>
		</div>
	)
}

export default App
