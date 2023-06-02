import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Articles from './pages/Articles';
import ArticleDetail from './pages/ArticleDetail';

const Main = () => (
  <Switch>
    <Route path="/category/:categoryId">
      <Articles />
    </Route>
    <Route path="/article/:id">
      <ArticleDetail />
    </Route>
    <Route path="/">
      <p>Select a category to view articles.</p>
    </Route>
  </Switch>
);

export default Main;
