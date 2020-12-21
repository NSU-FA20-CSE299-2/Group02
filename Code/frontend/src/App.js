import React from 'react';
import data from './data'
import {BrowserRouter, Route} from 'react-router-dom'
import './App.css';
import HomeScreen from './HomeScreen';
import ProductScreen from './ProductScreen';

function App() {
  return (
<BrowserRouter>
    <div className="grid-container">
      <header className="header">
        <div className="brand">
          <button onclick="openMenu()">
            &#9776;
          </button>
          <a href="index.html">Farsad's Store</a>
        </div>
        <div className="header-links">
          <a href="cart.html">Cart</a>
          <a href="signin.html">Sign in</a>
        </div>
      </header>
      <aside class="sidebar">
        <h3>Products Catagories</h3>
        <button class="sidebar-close-button" onclick="closeMenu()">X</button>
       <ul>
        <li>
          <a href="index.html">SSD</a>
        </li>
        <li>
          <a href="index.html">Ram</a>
        </li>
      </ul>

      </aside>


      <main className="main">
        <div className="content">
          <Route path="/products/:id" component={ProductScreen} />
          <Route path="/" exact={true} component={HomeScreen}/>
         
      </div>
    </main>
  </div> 
  
  </BrowserRouter>
  );
}

export default App;
