import React from 'react'
import "../styles/CardStack.css"

export default function CardStack(props) {
  const imgCount = props.cards.length;
  return (
    <div>
      {props.cards.map((card, index) => {
        return (
          <div key={index} className={index === imgCount - 1 ? "cardstack" : "cardstack crop"}>
            <img src={card.url} alt={card.name} />
          </div>
        );
      })}
    </div>
  )
}
