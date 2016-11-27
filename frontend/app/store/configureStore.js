import { createStore, applyMiddleware } from 'redux'
import rootReducer from '../reducers/index'
import thunk from 'redux-thunk'
import {redirect} from '../middlewares/redirect'



export default function configureStore(initialState) {
  return createStore(rootReducer, initialState, applyMiddleware(thunk, redirect));
}