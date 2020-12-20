import React from 'react';
import data from './data'
import {BrowserRouter, Route} from 'react-router-dom'
import './App.css';
import HomeScreen from './Screens/HomeScreen';
import ProductScreen from './Screens/ProductScreen';

function App() {
  return (
<BrowserRouter>
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
          <Route path="/products/:id" component={ProductScreen} />
          <Route path="/" exact={true} component={HomeScreen}/>
         
      </div>
    </main>
  </div> 
  </BrowserRouter>
  );
}

export default App;
