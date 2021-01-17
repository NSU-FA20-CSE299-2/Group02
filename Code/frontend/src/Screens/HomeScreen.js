import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'
import axios from 'axios';
import { useSelector } from 'react-redux';
import {listProducts} from '../actions/ProductActions';
function HomeScreen(props) {


const productList = useSelector(state => state.productList);
const { products, loading, error} = productList;
const dispatch = useDispatch();
useEffect(() => {
  dispatch(listProducts());
   
  return () => {
    //
  };
}, [])

  return loading ? <div>Loading...</div> :
 error ? <div>{error}</div>:
 
 <ul className="products">
    
    {
      products.map(product =>
        <li key={product._id}>
          <div className="product">
            <Link to={`/product/${product._id}`}>
              <img className="image" src={product.image} />

            </Link>
            <div className="product-name">
              <Link to={`/product/${product._id}`}>{product.name}</Link> </div>
            <div className="brand"> {product.brand}</div>
            <div className="price">${product.price}</div>
            <div className="rating">{product.rating}Stars {product.numeviews}</div>
          </div>
        </li>)
    }
  </ul>
}
export default HomeScreen;