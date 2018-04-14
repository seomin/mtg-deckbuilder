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
          return { id: card["id"], url: card["mciUrl"], name: card["name"] }
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

export const SELECTING_DECK = 'SELECTING_DECK'
function selectingDeck(deckId) {
  return { type: SELECTING_DECK, deckId }
}

export const RECEIVED_DECK = 'RECEIVED_DECK'
function receivedDeck(deck) {
  return { type: RECEIVED_DECK, deck }
}

export function selectDeck(deckId) {
  return dispatch => {
    dispatch(selectingDeck(deckId))

    API.fetchDeck(deckId)
      .then(result => {
        return result.json()
      })
      .then((data) => {
        dispatch(receivedDeck(data))
      })
  }
}
