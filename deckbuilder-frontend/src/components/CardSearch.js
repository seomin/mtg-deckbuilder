import React, { Component } from 'react'
import { connect } from 'react-redux'
import { searchCards } from '../state/actions'
import CardStack from './CardStack'
import "../styles/CardSearch.css"

class _CardSearch extends Component {

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
          <label>
            Search for card by name:
            <input type="text" value={this.state.searchString} onChange={this.updateSearchString} />
          </label>
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

const CardSearch = connect(
  mapStateToProps,
  mapDispatchToProps
)(_CardSearch)

export default CardSearch
