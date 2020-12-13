import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (

    <div className="grid-container">
    <header className="header">
      <div className="brand">
        <a href="index.html">Farsad's Store</a>
      </div>
      <div className= "header-links">
        <a href ="cart.html">Cart</a>
        <a href="signin.html">Sign in</a>
      </div>
    </header>
    <main className="main">
      <div className="content">
         <ul className="products">
        <li>
         <div className="product"> 
           <img className="image" src="ssd.jpg">
           <div className="product-name">
           <a href="product.html"> SSD 256gb </a>
           </div>
           <div className= "brand"> WD</div>
           <div className="price">$30</div>
           <div className="rating">3.5 stars</div>
         </div>
        </li>
           <li>
            <div className="product"> 
              <img className="image" src="Sandisk.jpg">
               <div className="product-name">
                <a href="product.html"> SSD 120GB </a>
                </div>
                <div className= "brand"> Sandisk</div>
                <div className="price">$17</div>
                <div className="rating">2.2 stars</div>
            </div>
           </li>
              <li>
                <div className="product"> 
                  <img className="image" src="Transcend.jpg">
                  <div className="product-name">
                    <a href="product.html"> SSD 128gb </a>
                  </div>
                  <div className= "brand"> Transcend</div>
                  <div className="price">$20</div>
                  <div className="rating">3 stars</div>
                </div>
              </li>
                <li>
                 <div className="product"> 
                  <img className="image" src="HP.jpg">
                  <div className="product-name">
                    <a href="product.html"> SSD 128gb </a>
                  </div>
                  <div className= "brand"> HP</div>
                  <div className="price">$25</div>
                  <div className="rating">3.5 stars</div>
                 </div>
                </li>
                  <li>
                   <div className="product"> 
                    <img className="image" src="WD BLUE.png">
                     <div className="product-name">
                     <a href="product.html"> SSD 240gb </a>
                    </div>
                    <div className= "brand"> WD BLUE</div>
                    <div className="price">$28</div>
                    <div className="rating">2.5 stars</div>
                  </div>
                </li>
          </ul>
      </div>
    </main>
  </div> 
  );
}

export default App;
