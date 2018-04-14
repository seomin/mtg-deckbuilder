import React from "react"
import { connect } from "react-redux"

function DeckView(props) {
  if (props.deck === null) {
    return null
  }
  return (
    <div>
      <h2>{props.deck.name}</h2>
      <div>
        Number of cards: {props.deck.cards.length}
      </div>
    </div>
  )
}

const mapStateToProps = (state) => {
  return { deck: state.decks.selectedDeck }
}

const mapDispatchToProps = (dispatch) => {
  return {}
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(DeckView)
