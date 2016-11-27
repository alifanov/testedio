import {appHistory} from '../history'

export const redirect = store => next => action => { //eslint-disable-line no-unused-vars
  if (action.type === 'ROUTING') {
    appHistory.push(action.payload)
  }

  return next(action)
};