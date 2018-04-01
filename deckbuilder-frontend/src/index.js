import React from 'react';
import ReactDOM from 'react-dom';
import thunkMiddleware from 'redux-thunk'
import { createStore, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'
import rootReducer from './state/reducers'
import './index.css';
import DeckBuilder from './components/DeckBuilder';


const store = createStore(
  rootReducer,
  applyMiddleware(thunkMiddleware)
)

ReactDOM.render(
  <Provider store={store}>
    <DeckBuilder />
  </Provider>,
  document.getElementById('root')
)
