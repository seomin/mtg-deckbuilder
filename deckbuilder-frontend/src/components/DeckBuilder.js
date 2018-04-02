import React from 'react'
import CardSearch from "./CardSearch"
import DecksView from "./DecksView"
import "../styles/DeckBuilder.css"

export default function DeckBuilder(props) {
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
