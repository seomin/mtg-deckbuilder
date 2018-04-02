import React, { Component } from 'react'
import { connect } from 'react-redux'
import { createDeck } from '../state/actions'
import "../styles/CreateDeckView.css"


class _CreateDeckView extends Component {
  constructor(props) {
    super(props)
    this.state = {newDeckName: ""}
  }

  render() {
    return (
      <div className="createdeck" >
        <form onSubmit={this.createDeck}>
          <input type="text" placeholder="New Deck Name" value={this.state.newDeckName} onChange={this.updateNewDeckName} />
          <input type="submit" value="Create Deck" />
        </form>
      </div>
    )
  }

  updateNewDeckName = (event) => {
    this.setState({newDeckName: event.target.value})
  }

  createDeck = (event) => {
    event.preventDefault()
    this.props.createDeck(this.state.newDeckName)
  }
}

const mapStateToProps = (state) => {
  return {}
}

const mapDispatchToProps = (dispatch) => {
  return {
    createDeck: (name) => {
      dispatch(createDeck(name))
    }
  }
}

const CreateDeckView = connect(
  mapStateToProps,
  mapDispatchToProps
)(_CreateDeckView)

export default CreateDeckView
