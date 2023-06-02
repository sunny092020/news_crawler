import React from 'react';
import Header from './components/Header';
import Main from './Main';
import Footer from './components/Footer';
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
