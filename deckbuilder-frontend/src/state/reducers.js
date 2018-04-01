import { combineReducers } from 'redux'
import {
  SEARCHING_CARD,
  FOUND_CARDS
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

const rootReducer = combineReducers({ searchedCards })

export default rootReducer
