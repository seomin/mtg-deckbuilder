export default class DeckBuilderApi {
  constructor(baseUrl) {
    this.baseUrl = baseUrl;
  }

  defaultHeaders() {
		return {
			'Accept': 'application/json',
			'Content-Type': 'application/json;charset=UTF-8'
		};
	}

  searchCard(search) {
    return fetch(this.baseUrl + "/cards?search=" + search, {
			method: 'GET',
			headers: this.defaultHeaders()
		});
  }
}
