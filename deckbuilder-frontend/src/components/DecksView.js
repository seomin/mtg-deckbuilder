import React from 'react'
import "../styles/DecksView.css"
import CreateDeckView from "./CreateDeckView"
import DeckView from "./DeckView"

export default function DecksView(props) {
  return (
    <div className="decksview">
      <CreateDeckView />
      <DeckView />
    </div>
  )
}
