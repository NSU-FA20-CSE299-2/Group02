import React from 'react';
import data from './data';
function HomeScreen(props) {
  return <ul className="products">
    {
      data.products.map(product =>
        <li>
          <div className="product">
            <img className="image" src={product.image} alt="SSD" />
            <div className="product-name">
              <a href="product.html">{product.name}</a>
            </div>
            <div className="brand"> {product.brand}</div>
            <div className="price">${product.price}</div>
            <div className="rating">{product.rating}Stars {product.numeviews}</div>
          </div>
        </li>)
    }
  </ul>
}
export default HomeScreen;