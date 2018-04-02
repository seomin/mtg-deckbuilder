import React from 'react'
import "../styles/CardStack.css"

export default function CardStack(props) {
  const imgCount = props.cards.length;
  return (
    <div>
      {props.cards.map((card, index) => {
        return (
          <div className="tooltip">
            <div key={index} className={"cardstack" + (index === imgCount - 1 ? "" : " crop")}>
              <img src={card.url} alt={card.name} />
            </div>
            <img src={card.url} alt="" className={"tooltiptext " + (index === imgCount - 1 ? "tooltiptextuncropped" : " tooltiptextcropped")} />
          </div>
        );
      })}
    </div>
  )
}
