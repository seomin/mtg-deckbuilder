export default class DeckBuilderApi {
  constructor(baseUrl) {
    this.baseUrl = baseUrl
  }

  defaultHeaders() {
		return {
			'Accept': 'application/json',
			'Content-Type': 'application/json;charset=UTF-8'
		}
	}

  searchCard(search) {
    return fetch(this.baseUrl + "/cards?search=" + search, {
			method: 'GET',
			headers: this.defaultHeaders()
		})
  }

  fetchDecks() {
    return fetch(this.baseUrl + "/deck", {
			method: 'GET',
			headers: this.defaultHeaders()
		})
  }

  fetchDeck(deckId) {
    return fetch(this.baseUrl + "/deck/" + deckId, {
			method: 'GET',
			headers: this.defaultHeaders()
		})
  }

  createDeck(name) {
    const formData = new FormData()
    formData.append("name", name)
    return fetch(this.baseUrl + "/deck", {
			method: 'POST',
      body: formData
		})
  }

  addCardToDeck(cardId, deckId) {
    const formData = new FormData()
    formData.append("card_id", cardId)
    return fetch(this.baseUrl + "/deck/" + deckId + "/card", {
			method: 'POST',
      body: formData
		})
  }
}
