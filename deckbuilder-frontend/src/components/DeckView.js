import React from "react"
import { connect } from "react-redux"

function _DeckView(props) {
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

const DeckView = connect(
  mapStateToProps,
  mapDispatchToProps
)(_DeckView)
export default DeckView
