import {combineReducers} from 'redux'
import {reducer as modalReducer} from 'react-redux-modal'

import {reducer as notifications} from 'react-notification-system-redux';
import codeState from './code'
import testState from './test'
import commonState from './common'

export default combineReducers({
    commonState,
    codeState,
    testState,
    notifications,
    modals: modalReducer
})