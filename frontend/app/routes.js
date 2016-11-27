import React from 'react'
import {Route, IndexRoute} from 'react-router'
import CodeFinder from './components/CodeFinder'
import TestFinder from './components/TestFinder'
import WidgetFinder from './components/WidgetFinder'

export default function routes() {
    return (
        <div>
            <Route path='/' component={CodeFinder}>
                <IndexRoute component={CodeFinder}/>
            </Route>
            <Route path='/code/' component={CodeFinder}/>
            <Route path='/test/' component={TestFinder}/>
            <Route path='/widget/' component={WidgetFinder}/>
        </div>
    )
}