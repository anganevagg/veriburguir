import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.css'
import { NavBar } from './components/NavBar'
import { Landing } from './views/Landing'
import { Orders } from './views/Orders'

function App() {
	return (
		<div className="App">
			<NavBar></NavBar>
			<Landing></Landing>
		</div>
	)
}

export default App
