<<<<<<< HEAD
import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
=======
import { createStore, combineReducers, compose, applyMiddleware } from 'redux';
>>>>>>> a08c5621d9201d3c335b6d39e6db44f30e97fbd9
import thunk from 'redux-thunk'
import { productListReducer } from './reducers/productReducers';


const initialState= {};
const reducer = combineReducers({
    productList: productListReducer,
})

const composeEnhancer = window._REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(reducer, initialState, compose(applyMiddleware(thunk)));
export default store;