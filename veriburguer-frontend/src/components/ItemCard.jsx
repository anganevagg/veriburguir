import { useState } from "react"
import { Button, Card, Form } from "react-bootstrap"

export function ItemCard (props){
	const { item } = props
	const [ num, setNum ] = useState(0)
	const handleAdd = ()=>{
		setNum(num+1)
	}
	const handleSubstract = ()=>{
		if(num>0)
			setNum(num-1)
	}
	return <Card className="">
		<Card.Body>
			<h5>{item.name}</h5>
			<p>${item.price}</p>
			<div className="px-3">
				<div className="d-flex flex-row mx-auto text-center">
					<Button onClick={handleSubstract}>-</Button>
					<Form.Control className="text-center" value={num} min={0}></Form.Control>
					<Button onClick={handleAdd}>+</Button>
				</div>
			</div>
		</Card.Body>
	</Card>
}