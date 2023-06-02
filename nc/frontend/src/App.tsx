import React from 'react';
import Header from './Header';
import Main from './Main';
import Footer from './Footer';
import { BrowserRouter as Router } from 'react-router-dom';

const App = () => (
  <Router>
    <div className="App">
      <Header />
      <Main />
      <Footer />
    </div>
  </Router>
);

export default App;
