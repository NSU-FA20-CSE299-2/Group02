import React from 'react';
import data from './data';
import {BrowserRouter, Route, Link} from 'react-router-dom'
import './App.css';
import HomeScreen from './HomeScreen';
import ProductScreen from './ProductScreen';

function openMenu(){
  console.log('Open Menu');
}

function closeMenu(){
  console.log('Close Menu');
}

function App() {
  return (
<BrowserRouter>
    <div className="grid-container">
      <header className="header">
        <div className="brand">
          <button onClick={openMenu}>
            &#9776;
          </button>
          <Link to="/">Farsad's Store</Link>
          {/* <a href="index.html">Farsad's Store</a> */}
        </div>
        <div className="header-links">
          <a href="cart.html">Cart</a>
          <a href="signin.html">Sign in</a>
        </div>
      </header>
      <aside className="sidebar">
        <h3>Products Catagories</h3>
        <button className="sidebar-close-button" onClick={closeMenu}>X</button>
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
