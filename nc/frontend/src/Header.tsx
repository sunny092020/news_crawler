import React, { useEffect, useState } from 'react';
import './Header.css';
import { Link } from 'react-router-dom';
import { Category } from './models/index';


const Header = () => {
  const [categories, setCategories] = useState<Category[]>([]);

  useEffect(() => {
    fetch('http://10.3.0.7:8000/api/v1/categories/')
      .then(response => response.json())
      .then(data => setCategories(data));
  }, []);

  return (
    <header className="header">
      <nav className="nav">
        <ul>
          {categories.map((category) => (
            <li key={category.id}>
              <Link to={`/category/${category.id}`}>{category.name}</Link>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
};

export default Header;
