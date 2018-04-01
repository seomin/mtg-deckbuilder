import React from 'react'
import CardSearch from "./CardSearch"

export default function DeckBuilder(props) {
  return (
    <div>
      <header>
        <h1>MTG Deckbuilder</h1>
      </header>

      <CardSearch />
    </div>
  )
}
