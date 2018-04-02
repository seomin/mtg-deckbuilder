import { combineReducers } from 'redux'
import {
  SEARCHING_CARD,
  FOUND_CARDS,
  RECEIVED_DECKS,
  SELECTING_DECK,
  RECEIVED_DECK
} from './actions'

const CARD_BACK = process.env.REACT_APP_API_BASE_URL + "/static/card_back.jpg"
const NO_CARDS = [{ url: CARD_BACK, name: "No match found" }]

function searchedCards(state = {searching: false, cards: NO_CARDS}, action) {
  switch (action.type) {
    case SEARCHING_CARD:
      return { searching: true, cards: NO_CARDS }
    case FOUND_CARDS:
      return { searching: false, cards: action.cards }
    default:
      return state
  }
}

function decks(state = {userDecks: [], selectedDeck: null, fetching: false}, action) {
  switch (action.type) {
    case RECEIVED_DECKS:
      return Object.assign({}, state, { userDecks: action.decks })
    case RECEIVED_DECK:
      return Object.assign({}, state, { selectedDeck: action.deck })
    case SELECTING_DECK:
      return Object.assign( {}, state, { fetching: true })
    default:
      return state
  }
}

const rootReducer = combineReducers({
  searchedCards,
  decks
})

export default rootReducer
