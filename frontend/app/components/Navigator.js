import React, {
    Component,
    PropTypes,
} from 'react';
import {Link} from 'react-router'
import {FaCheckSquare, FaCss3} from 'react-icons/fa';
import MdCode from 'react-icons/md/code';


class Navigator extends Component {
    render() {
        return (
            <div>
                <div className='row'>
                    <div className='col-md-4 text-center'>
                        <Link to='/code/' activeClassName='active' className='menu__item'>
                            <MdCode width='100' height='100' />
                        </Link>
                    </div>
                    <div className='col-md-4 text-center'>
                        <Link to='/test/' activeClassName='active' className='menu__item'>
                            <FaCheckSquare width='100' height='100' />
                        </Link>
                    </div>
                    <div className='col-md-4 text-center'>
                        <Link to='/widget/' activeClassName='active' className='menu__item'>
                            <FaCss3 width='100' height='100' />
                        </Link>
                    </div>
                </div>
            </div>
        );
    }
}

Navigator.propTypes = {};
Navigator.defaultProps = {};

export default Navigator;
