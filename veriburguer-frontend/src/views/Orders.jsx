import { useEffect, useState } from "react"
import { Button, Container, Modal } from "react-bootstrap"

export function Orders(){
	const [orders, setOrders] = useState([])
	const [burgers, setBurgers] = useState([])

	useEffect(()=>{
		fetch('http://localhost:8000/api/orders').
		then(res=>res.json()).then(data=>setOrders(data))
		console.log(orders)
	}, [])
	const [openModal, setOpenModal]= useState(false)
	const handleOpen = ()=>setOpenModal(true)
	const handleClose = ()=>setOpenModal(false)
	return (
		<div className="mx-4">
			<Button onClick={handleOpen}>Create Order</Button>
			<Modal show={openModal} onHide={handleClose} size="lg">
				<Modal.Header closeButton={true}></Modal.Header>
				<Modal.Body>
					
				</Modal.Body>
			</Modal>
		</div>
	)
}