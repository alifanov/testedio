import React, {
    Component,
    PropTypes,
} from 'react';

class TestWidget extends Component {
    constructor(props){
        super(props);
        this.state = {
            opened: false
        }
    }
    render() {
        return (
            <div className='col-md-12' >
                <div className='result__item_test'>
                    <div className='panel panel-success'>
                        <div className='panel-heading panel-heading_test'
                             onClick={() => {
                                 this.setState({
                                     opened: !this.state.opened
                                 })
                             }}
                        >
                            <h3 className='panel-title'>
                                Test: {this.props.title}</h3>
                        </div>
                        <div className={'panel-body ' + (this.state.opened ? '' : 'hidden')}
                        >
                            <pre>{this.props.content}</pre>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

TestWidget.propTypes = {};
TestWidget.defaultProps = {};

export default TestWidget;
