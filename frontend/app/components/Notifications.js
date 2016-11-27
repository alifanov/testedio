import React, {
    Component,
    PropTypes,
} from 'react';
import {connect} from 'react-redux';
import Notifications from 'react-notification-system-redux';


class NotificationsContainer extends Component {
    render() {
        const style = {
            NotificationItem: {
                DefaultStyle: {
                    margin: '10px 5px 2px 1px'
                },
                success: {
                    borderTop: '2px solid #1abc9c',
                    background: 'white'
                }
            },
            Title: {
                success: {
                    color: '#1abc9c',
                    fontSize: '16px',
                    fontWeight: 'normal',
                    fontFamily: 'ProximaNova-Regular'
                }
            },
            Dismiss: {
                success: {
                    color: '#fff',
                    backgroundColor: '#1abc9c'
                }
            }
        };
        const {notifications} = this.props;
        return (
            <div>
                <Notifications notifications={notifications} style={style}/>
            </div>
        );
    }
}

Notifications.propTypes = {};
Notifications.defaultProps = {};

export default connect(
    state => ({notifications: state.notifications})
)(NotificationsContainer);
