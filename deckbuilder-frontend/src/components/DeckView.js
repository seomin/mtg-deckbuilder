import React from "react"
import { connect } from "react-redux"
import { DropTarget } from 'react-dnd'
import { Bar, BarChart, Tooltip, XAxis, YAxis } from "recharts"
import { ItemTypes } from "../constants/Constants"
import { addCardToDeck } from '../state/actions'
import "../styles/DeckView.css"

// DroptTarget
const deckTarget = {
  hover(props, monitor, component) {
  },

  drop(props, monitor, component) {
    const item = monitor.getItem()
    props.addCardToDeck(item.cardId, props.deck.id)
  }
};

function collect(connect, monitor) {
  return {
    connectDropTarget: connect.dropTarget(),
    isOver: monitor.isOver(),
  }
}

function createData(oldCmc) {
  var cmcList = []
  for (const [cmc, count] of Object.entries(oldCmc)) {
    cmcList.push({cmc: cmc, count: count})
  }
  return cmcList
}

function DeckView(props) {
  if (props.deck === null) {
    return null
  }
  return props.connectDropTarget(
    <div>
      <h2>{props.deck.name}</h2>

      <BarChart width={400} height={200} data={createData(props.deck.cmcDistribution)}>
        <XAxis dataKey="cmc" />
        <YAxis />
        <Bar type="monotone" dataKey="count" barSize={60} fill="#8884d8"/>
        <Tooltip />
      </BarChart>

      <div className="deckview" >
        {props.deck.cards.map((card, index) => {
          return (<img src={card.mciUrl} alt={card.name} key={index} />)
        })}
      </div>
    </div>
  )
}

const mapStateToProps = (state) => {
  return { deck: state.decks.selectedDeck, fetching: state.decks.fetching }
}

const mapDispatchToProps = (dispatch) => {
  return {
    addCardToDeck: (cardId, deckId) => {
      dispatch(addCardToDeck(cardId, deckId))
    }
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(DropTarget(ItemTypes.CARD, deckTarget, collect)(DeckView))
