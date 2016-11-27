import React from 'react'
import {render} from 'react-dom'
import configureStore from './store/configureStore'
import {Provider} from 'react-redux'
import routes from './routes'

import { Router } from 'react-router'
import {appHistory} from './history'

import NotificationsContainer from './components/Notifications'


const store = configureStore({});

render(
    <Provider store={store}>
        <div className='root-wrapper'>
            <Router history={appHistory}>
                {routes()}
            </Router>
            <NotificationsContainer />
        </div>
    </Provider>,
    document.getElementById('root')
);