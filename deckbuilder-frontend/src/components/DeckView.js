import React from "react"
import { connect } from "react-redux"
import { DropTarget } from 'react-dnd'
import { ItemTypes } from "../constants/Constants"
import { addCardToDeck } from '../state/actions'
import "../styles/DeckView.css"

// DroptTarget
const deckTarget = {
  hover(props, monitor, component) {
  },

  drop(props, monitor, component) {
    const item = monitor.getItem()
    props.addCardToDeck(item.cardId, props.deck.id)
  }
};

function collect(connect, monitor) {
  return {
    connectDropTarget: connect.dropTarget(),
    isOver: monitor.isOver(),
  }
}

function DeckView(props) {
  if (props.deck === null) {
    return null
  }
  return props.connectDropTarget(
    <div>
      <h2>{props.deck.name}</h2>
      <div className="deckview" >
        {props.deck.cards.map(card => {
          return (<img src={card.mciUrl} key={card.id} />)
        })}
      </div>
    </div>
  )
}

const mapStateToProps = (state) => {
  return { deck: state.decks.selectedDeck, fetching: state.decks.fetching }
}

const mapDispatchToProps = (dispatch) => {
  return {
    addCardToDeck: (cardId, deckId) => {
      dispatch(addCardToDeck(cardId, deckId))
    }
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(DropTarget(ItemTypes.CARD, deckTarget, collect)(DeckView))
