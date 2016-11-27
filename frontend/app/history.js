import {createHashHistory} from 'history';
import { hashHistory } from 'history'
import {useRouterHistory} from 'react-router'


export const appHistory = useRouterHistory(createHashHistory)({queryKey: false});
