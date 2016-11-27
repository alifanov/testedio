import React, {
    Component,
    PropTypes,
} from 'react';

import Wrapper from './Wrapper'
import Navigator from './Navigator'
import {connect} from 'react-redux'
import * as findActions from '../actions/findActions'
import {bindActionCreators} from 'redux'
import TestWidget from './primitive/TestWidget'

class CodeFinder extends Component {
    render() {
        return (
            <Wrapper initial={this.props.initial}>
                <div>
                    <Navigator/>
                </div>
                <div>
                    <h1 className='text-center'>Code finder</h1>
                    <div className='row'>
                        <div className='col-md-8 col-md-offset-2'>
                            <textarea placeholder='Enter your code' className="form-control code__textarea"
                                      value={this.props.code}
                                      onChange={(event) => {
                                          this.props.fa.setCode(event.target.value)
                                      }}
                            />
                            <div className='element__wrapper'>
                                <button className='btn btn-primary btn-block'
                                        onClick={()=> {
                                            this.props.fa.findCode(this.props.code)
                                        }}
                                >Find
                                </button>
                            </div>
                        </div>
                    </div>
                    <div className='row'>
                        <div className='col-md-12'>
                            <div className='results'>
                                {this.props.found_code.map((result, i) => {
                                    return (
                                        <div className='result__item' key={i}>
                                            <div className='row'>
                                                <div className='col-md-12'>
                                                    <div className='result__item_code'>
                                                        <div className='panel panel-primary'>
                                                            <div className='panel-heading'>
                                                                <h3 className='panel-title'>[{result.rank}] Code: ({result.depth}d {result.body_length}bl)</h3>
                                                            </div>
                                                            <div className='panel-body'>
                                                                <pre>{result.code}</pre>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                {result.tests.map((t, ii) => {
                                                    return (
                                                        <TestWidget key={ii} content={t.test} title={t.name}/>
                                                    )
                                                })}
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

CodeFinder.propTypes = {};
CodeFinder.defaultProps = {};

function mapStateToProps(state) {
    return {
        code: state.codeState.code,
        found_code: state.codeState.found_code,
        initial: state.commonState.initial
    }
}

function mapDispatchToProps(dispatch) {
    return {
        fa: bindActionCreators(findActions, dispatch)
    }
}
export default connect(mapStateToProps, mapDispatchToProps)(CodeFinder)