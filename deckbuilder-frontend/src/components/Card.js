import React, { Component } from 'react'
import { DragSource } from 'react-dnd'
import { ItemTypes } from "../constants/Constants"
import "../styles/Card.css"

const cardSource = {
  beginDrag(props) {
    const item = { cardId: props.card.id }
    return item
  },

  canDrag(props) {
    return props.card.name !== "No match found"
  }
}

function collect(connect, monitor) {
  return {
    connectDragSource: connect.dragSource(),
    connectDragPreview: connect.dragPreview(),
    isDragging: monitor.isDragging()
  }
}

function renderDraggingCard(props) {
  return (
    <div >
      <div className="card">
        <img src={props.card.url} alt={props.card.name} />
      </div>
    </div>
  )
}

function renderFullCard(props) {
  return (
    <div className="tooltip">
      <div className={"card" + (props.isFront ? "" : " crop")}>
        <img src={props.card.url} alt={props.card.name} />
      </div>
      <img src={props.card.url} alt="" className={"tooltiptext " + (props.isFront ? "tooltiptextuncropped" : " tooltiptextcropped")} />
    </div>
  )
}

class Card extends Component {

  componentDidUpdate() {
    const img = new Image()
    img.src = this.props.card.url
    // img.width = 150
    img.style = {width: "150px"}
    img.onload = () => this.props.connectDragPreview(img)
  }

  render() {
    return this.props.connectDragSource(
      this.props.isDragging ? renderDraggingCard(this.props) : renderFullCard(this.props)
    )
  }
}

export default DragSource(ItemTypes.CARD, cardSource, collect)(Card)
