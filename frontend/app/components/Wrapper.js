import React, {
    Component,
    PropTypes,
} from 'react';

class Wrapper extends Component {
    render() {
        return (
            <div className={'container ' + (this.props.initial ? 'initial' : '')}>{this.props.children}</div>
        );
    }
}

Wrapper.propTypes = {};
Wrapper.defaultProps = {};

export default Wrapper;
