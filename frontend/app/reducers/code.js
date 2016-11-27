export const initialState = {
    found_code: [],
    code: ''
};

export default function codeState(state = initialState, action) {
    switch (action.type) {
        case 'FIND_CODE':
            return Object.assign({}, state, {
                found_code: action.payload
            });
        case 'SET_CODE':
            return Object.assign({}, state, {
                code: action.payload
            });
        default:
            return state;
    }
}