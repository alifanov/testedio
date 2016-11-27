import React, {
    Component,
    PropTypes,
} from 'react';

import Wrapper from './Wrapper'
import Navigator from './Navigator'
import {connect} from 'react-redux'
import * as findActions from '../actions/findActions'
import {bindActionCreators} from 'redux'

class TestFinder extends Component {
    render() {
        return (
            <Wrapper initial={this.props.initial}>
                <div>
                    <Navigator/>
                </div>
                <div>
                    <h1 className='text-center'>Test finder</h1>
                    <div className='row'>
                        <div className='col-md-8 col-md-offset-2'>
                            <textarea placeholder='Enter your test' className="form-control code__textarea"
                                      value={this.props.test}
                                      onChange={(event) => {
                                          this.props.fa.setTest(event.target.value)
                                      }}
                            />
                            <div className='element__wrapper'>
                                <button className='btn btn-primary btn-block'
                                        onClick={()=> {
                                            this.props.fa.findTest(this.props.test)
                                        }}
                                >Find
                                </button>
                            </div>
                        </div>
                    </div>
                    <div className='row'>
                        <div className='col-md-12'>
                            <div className='results'>
                                {this.props.found_test.map((result, i) => {
                                    return (
                                        <div className='result__item' key={i}>
                                            <div className='row'>
                                                <div className='col-md-6'>
                                                    <div className='result__item_test'>
                                                        <div className='panel panel-success'>
                                                            <div className='panel-heading'>
                                                                <h3 className='panel-title'>[{result.rank}] Test:</h3>
                                                            </div>
                                                            <div className='panel-body'>
                                                                <pre>{result.test}</pre>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div className='col-md-6'>
                                                    <div className='result__item_code'>
                                                        <div className='panel panel-primary'>
                                                            <div className='panel-heading'>
                                                                <h3 className='panel-title'>[{result.rank}] Code:</h3>
                                                            </div>
                                                            <div className='panel-body'>
                                                                <pre>{result.code}</pre>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <hr />
                                        </div>
                                    )
                                })}
                            </div>
                        </div>
                    </div>
                </div>
            </Wrapper>
        );
    }
}

TestFinder.propTypes = {};
TestFinder.defaultProps = {};

function mapStateToProps(state) {
    return {
        test: state.testState.test,
        found_test: state.testState.found_test,
        initial: state.commonState.initial
    }
}

function mapDispatchToProps(dispatch) {
    return {
        fa: bindActionCreators(findActions, dispatch)
    }
}
export default connect(mapStateToProps, mapDispatchToProps)(TestFinder)