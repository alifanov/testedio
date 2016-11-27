import cookie from 'react-cookie';
import ajax from 'superagent'

export function findCode(code) {
    return (dispatch) => {
        ajax.post('/api/find/code/')
            .withCredentials()
            .send({data: code})
            .set({'X-CSRFToken': cookie.load('csrftoken')})
            .end((err, res) => {
                dispatch({
                    type: 'FIND_CODE',
                    payload: res.body
                });
                dispatch({
                    type: 'SET_INITIAL',
                    payload: false
                })
            })
    }
}

export function findTest(test) {
    return (dispatch) => {
        ajax.post('/api/find/test/')
            .withCredentials()
            .send({data: test})
            .set({'X-CSRFToken': cookie.load('csrftoken')})
            .end((err, res) => {
                dispatch({
                    type: 'FIND_TEST',
                    payload: res.body
                });
                dispatch({
                    type: 'SET_INITIAL',
                    payload: false
                })
            })
    }
}

export function setCode(code) {
    return {
        type: 'SET_CODE',
        payload: code
    }
}

export function setTest(test) {
    return {
        type: 'SET_TEST',
        payload: test
    }
}