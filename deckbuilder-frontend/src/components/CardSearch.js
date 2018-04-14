import React, { Component } from 'react'
import { connect } from 'react-redux'
import { searchCards } from '../state/actions'
import CardStack from './CardStack'
import "../styles/CardSearch.css"

class CardSearch extends Component {

  constructor(props) {
      super(props)
      this.state = {
        searchString: ""
      }
  }

  render() {
    return (
      <div className="cardsearch">
        <form onSubmit={this.search} >
          <input type="text" placeholder="Search for card by name" value={this.state.searchString} onChange={this.updateSearchString} />
          <input type="submit" value="Search" />
        </form>

        <CardStack cards={this.props.cards}/>
      </div>
    )
  }

  updateSearchString = (event) => {
    this.setState({searchString: event.target.value})
  }

  search = (event) => {
    event.preventDefault()
    this.props.search(this.state.searchString)
  }
}

const mapStateToProps = (state) => {
  return { cards: state.searchedCards.cards }
}

const mapDispatchToProps = (dispatch) => {
  return {
    search: (searchString) => {
      dispatch(searchCards(searchString))
    }
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(CardSearch)
