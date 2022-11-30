import { useEffect, useState } from "react"
import { Button, Card, Container, Form, Modal } from "react-bootstrap"
import { ItemCard } from "../components/ItemCard"

import Swal from "sweetalert2"

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
	const [openModal, setOpenModal] = useState(false)
	const handleOpen = () => setOpenModal(true)
	const handleClose = () => setOpenModal(false)
	const [order, setOrder] = useState({})
	const handleOrdenar = () => {
		Swal.fire({
			icon: 'success',
			title: 'Ordenado',
			showConfirmButton: true,
		}).then(()=>handleClose())
	}
	return (
		<div className="mx-4">
			<Button className="my-4" onClick={handleOpen}>Crear Orden</Button>
			<div>
				<h2 className="text-white">Historial de ordenes</h2>
				<div className="row justify-content-center">
					{loading ? <p>Loading...</p> :
						orders.map(order =>
							<Card key={order.id} className="col-5 m-3">
								<Card.Body>
									<h2>Orden #{order.id}</h2>
									<p>Total: ${order.total}</p>
									{order.items.map(item => <>
										<p key={item.id}>{item.name} -{">"} ${item.price}</p>
									</>)}
									<div className="d-flex justify-content-end">
										<Button variant="primary" className="m-2">Editar</Button>
										<Button variant="danger" className="m-2">Borrar</Button>
									</div>
								</Card.Body>
							</Card>
						)
					}
				</div>
			</div>
			<Modal show={openModal} onHide={handleClose} size="lg">
				<Modal.Header closeButton={true}>Crear Orden</Modal.Header>
				<Modal.Body className="p-5">
					<div className="row">
						{loading ? <p>Loading...</p> :
							items.map(item => <>
								<div key={item.id} className="col-4 p-3">
									<ItemCard item={item} order={order} setOrder={setOrder}></ItemCard>
								</div>
							</>
							)
						}
						<div className="d-flex justify-content-end">
							<Button variant="success" onClick={handleOrdenar}>Ordenar</Button>
						</div>
					</div>
				</Modal.Body>
			</Modal>
		</div>
	)
}