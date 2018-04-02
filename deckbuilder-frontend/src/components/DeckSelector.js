import React, { Component } from 'react'
import { connect } from 'react-redux'
import { fetchDecks, selectDeck } from '../state/actions'


class _DeckSelector extends Component {

  componentDidMount() {
    this.props.fetchDecks()
  }

  render() {
    return (
      <div>
        {this.props.decks.map((deck, idx) => {
          return (
            <div key={idx}>
              <a href="" onClick={this.selectDeck(deck.id)} >{deck.name} </a>
            </div>
          )
        })}
      </div>
    )
  }

  selectDeck = (deckId) => (event) => {
    event.preventDefault()
    this.props.selectDeck(deckId)
  }
}

const mapStateToProps = (state) => {
  return { decks: state.decks.userDecks }
}

const mapDispatchToProps = (dispatch) => {
  return {
    fetchDecks: () => {
      dispatch(fetchDecks())
    },
    selectDeck: (deckId) => {
      dispatch(selectDeck(deckId))
    }
  }
}

const DeckSelector = connect(
  mapStateToProps,
  mapDispatchToProps
)(_DeckSelector)

export default DeckSelector
