import React from 'react';
import { Link } from 'react-router-dom'
import data from './data';

function HomeScreen(props) {
  return <ul className="products">
    {
      data.products.map(product =>
        <li key={product._id}>
          <div className="product">
            <Link to={`/product/${product._id}`}>
              <img className="image" src={product.image} alt="SSD" />

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