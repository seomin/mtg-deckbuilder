import React from 'react'
import "../styles/DecksView.css"
import CreateDeckView from "./CreateDeckView"
import DeckSelector from "./DeckSelector"
import DeckView from "./DeckView"

export default function DecksView(props) {
  return (
    <div className="decksview">
      <CreateDeckView />
      <DeckSelector />
      <DeckView />
    </div>
  )
}
