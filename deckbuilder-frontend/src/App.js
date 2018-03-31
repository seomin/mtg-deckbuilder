import React, { Component } from 'react';
import DeckBuilderApi from './DeckBuilderApi.js';
import "./App.css";

const CARD_BACK = process.env.REACT_APP_API_BASE_URL + "/static/card_back.jpg"
const api = new DeckBuilderApi(process.env.REACT_APP_API_BASE_URL)

class App extends Component {
  constructor(props) {
      super(props);
      this.state = {
        imgUrls: [CARD_BACK],
        search: ""
      };
  }

  render() {
    return (
      <div>
        <header>
          <h1>MTG Deckbuilder</h1>
        </header>

        <form onSubmit={this.searchCard} >
          <label>
            Search for card by name:
            <input type="text" value={this.state.search} onChange={this.updateSearch} />
          </label>
          <input type="submit" value="Search" />
        </form>

        {this.renderImages(this.state.imgUrls)}
      </div>
    );
  }

  renderImages = (imgUrls) => {
    const imgCount = imgUrls.length;
    return (
      <div>
        {imgUrls.map((imgUrl, index) => {
          return (
            <div key={index} className={index === imgCount - 1 ? "cardstack" : "cardstack crop"}>
              <img src={imgUrl} alt="card" />
            </div>
          );
        })}
      </div>
    );
  }

  updateSearch = (event) => {
    this.setState({search: event.target.value});
  }

  searchCard = (event) => {
    event.preventDefault();
    api.searchCard(this.state.search)
      .then(result => {
        return result.json();
      })
      .then(data => {
        if (data.length === 0) {
          this.setState({imgUrls: [CARD_BACK]});
          return;
        }
        const imgUrls = data.map(card => card["mciUrl"])
        this.setState({imgUrls: imgUrls});
      });

  }
}

export default App;
