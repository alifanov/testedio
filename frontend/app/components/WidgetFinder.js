import React, {
    Component,
    PropTypes,
} from 'react';

import Wrapper from './Wrapper'
import Navigator from './Navigator'

class WidgetFinder extends Component {
    render() {
        return (
            <Wrapper>
                <div>
                    <Navigator/>
                </div>
                <div>
                    <h1 className='text-center'>Widget finder</h1>
                    <div className='row'>
                        <div className='col-md-4 col-md-offset-4'>
                            <input type='text' placeholder='Example "red button with icon"' className="form-control"/>
                            <div className='element__wrapper'>
                                <button className='btn btn-primary btn-block'>Find</button>
                            </div>
                        </div>
                    </div>
                </div>
            </Wrapper>
        );
    }
}

WidgetFinder.propTypes = {};
WidgetFinder.defaultProps = {};

export default WidgetFinder;
