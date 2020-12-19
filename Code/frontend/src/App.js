import React from 'react';
import data from './data'
import './App.css';

function App() {
  return (

    <div className="grid-container">
      <header className="header">
        <div className="brand">
          <a href="index.html">Farsad's Store</a>
        </div>
        <div className="header-links">
          <a href="cart.html">Cart</a>
          <a href="signin.html">Sign in</a>
        </div>
      </header>
      <main className="main">
        <div className="content">
          <ul className="products">
            {
              data.products.map (product =>
              
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
      </div>
    </main>
  </div> 
  );
}

export default App;
