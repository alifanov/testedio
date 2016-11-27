export const initialState = {
    initial: true
};

export default function commonState(state = initialState, action) {
    switch (action.type) {
        case 'SET_INITIAL':
            return Object.assign({}, state, {
                initial: action.payload
            });
        default:
            return state;
    }
}