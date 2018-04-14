import React, { Component } from 'react'
import CardSearch from "./CardSearch"
import DecksView from "./DecksView"
import "../styles/DeckBuilder.css"
import HTML5Backend from 'react-dnd-html5-backend';
import { DragDropContext } from 'react-dnd';

class DeckBuilder extends Component {

  render() {
    return (
      <div>
        <header className="header">
          <h1>MTG Deckbuilder</h1>
        </header>

        <div className="row">
          <CardSearch />
          <DecksView />
        </div>
      </div>
    )
  }
}

export default DragDropContext(HTML5Backend)(DeckBuilder)
