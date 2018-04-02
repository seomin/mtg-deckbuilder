import DeckBuilderApi from '../api/DeckBuilderApi.js'

const API = new DeckBuilderApi(process.env.REACT_APP_API_BASE_URL)

export const SEARCHING_CARD = 'SEARCHING_CARD'
function searchingCard() {
  return { type: SEARCHING_CARD }
}

export const FOUND_CARDS = 'FOUND_CARDS'
function foundCards(cards) {
  return { type: FOUND_CARDS, cards }
}

export function searchCards(searchString) {
  return dispatch => {
    dispatch(searchingCard())

    API.searchCard(searchString)
      .then(result => {
        return result.json()
      })
      .then(json => {
        const cards = json.map(card => {
          return { url: card["mciUrl"], name: card["name"] }
        })
        dispatch(foundCards(cards))
      })
  }
}

export const RECEIVED_DECKS = 'RECEIVED_DECKS'
function receivedDecks(decks) {
  return { type: RECEIVED_DECKS, decks }
}

export function fetchDecks() {
  return dispatch => {
    API.fetchDecks()
      .then(result => {
        return result.json()
      })
      .then(decks => {
        dispatch(receivedDecks(decks))
      })
  }
}

export function createDeck(name) {
  return dispatch => {
    API.createDeck(name)
      .then(() => {
        dispatch(fetchDecks())
      })
  }
}
