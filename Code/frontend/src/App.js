import React from 'react';
import {BrowserRouter, Route, Link} from 'react-router-dom'
import './App.css';
import HomeScreen from './HomeScreen';
import ProductScreen from './ProductScreen';

function App() {

  const openMenu = () => {
  document.querySelector(".sidebar").classList.add("open");

}

const closeMenu = () => {
 document.querySelector(".sidebar").classList.remove("open")
}

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
        <button className="sidebar-close-button" onclick={closeMenu}>X</button>
       <ul>
        <li>
          <a href="index.html">Notebook</a>
        </li>
        <li>
          <a href="index.html">Desktop and Pc</a>
        </li>
        <li>
          <a href="index.html">Security System</a>
        </li>
        <li>
          <a href="index.html">Gaming</a>
        </li>
        <li>
          <a href="index.html">Network</a>
        </li>
        <li>
          <a href="index.html">Storage</a>
        </li>
        <li>
          <a href="index.html">Sound System</a>
        </li>
      </ul>

      </aside>


      <main className="main">
        <div className="content">
          <Route path="/products/:id" component={ProductScreen} />
          <Route path="/" exact={true} component={HomeScreen} />
         
      </div>
    </main>
  </div> 
  </BrowserRouter>
  );
  }
export default App;
