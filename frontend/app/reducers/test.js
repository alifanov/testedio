export const initialState = {
    found_test: [],
    test: ''
};

export default function testState(state = initialState, action) {
    switch (action.type) {
        case 'FIND_TEST':
            return Object.assign({}, state, {
                found_test: action.payload
            });
        case 'SET_TEST':
            return Object.assign({}, state, {
                test: action.payload
            });
        default:
            return state;
    }
}