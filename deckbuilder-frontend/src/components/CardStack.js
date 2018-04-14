import React from 'react'
import Card from "./Card"

export default function CardStack(props) {
  const imgCount = props.cards.length;
  return (
    <div>
      {props.cards.map((card, index) => {
        return (
          <Card card={card} isFront={index === imgCount - 1} key={index} />
        );
      })}
    </div>
  )
}
