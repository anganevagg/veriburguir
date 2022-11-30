import { useEffect, useState } from "react"
import { Button, Card, Container, Form, Modal } from "react-bootstrap"
import { ItemCard } from "../components/ItemCard"

export function Orders() {
	const [orders, setOrders] = useState([])
	const [items, setItems] = useState([])
	const [loading, setLoading] = useState(true)
	useEffect(() => {
		fetch('http://localhost:8000/api/orders').
			then(res => res.json()).then(data => setOrders(data.data))
		fetch('http://localhost:8000/api/items')
			.then(res => res.json()).then(data => setItems(data.data))
		setLoading(false)
	}, [])
	console.log(orders)
	// console.log(items)
	const [openModal, setOpenModal] = useState(false)
	const handleOpen = () => setOpenModal(true)
	const handleClose = () => setOpenModal(false)
	return (
		<div className="mx-4">
			<Button className="my-4" onClick={handleOpen}>Crear Orden</Button>
			<div>
				{loading ? <p>Loading...</p> :
					orders.map(order =>
						<Card>
							<Card.Body>
								<h2>{order.id}</h2>
								<p>{order.total}</p>
							</Card.Body>
						</Card>
					)
				}
			</div>
			<Modal show={openModal} onHide={handleClose} size="lg">
				<Modal.Header closeButton={true}>Crear Orden</Modal.Header>
				<Modal.Body className="p-5">
					<div className="row">
						{loading ? <p>Loading...</p> :
							items.map(item => <>
								<div className="col-4 p-3">
									<ItemCard item={item}></ItemCard>
								</div>
							</>
							)
						}
					</div>
				</Modal.Body>
			</Modal>
		</div>
	)
}