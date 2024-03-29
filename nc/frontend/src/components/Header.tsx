import React, { useEffect, useState } from 'react';
import './Header.css';
import { Link } from 'react-router-dom';
import { Category } from '../models/index';


const Header = () => {
  const [categories, setCategories] = useState<Category[]>([]);
  const [selectedCategoryId, setSelectedCategoryId] = useState<number | null>(null);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_BASE_URL}/categories/`)
      .then(response => response.json())
      .then(data => setCategories(data))
      .catch(error => {
        console.error('Error:', error);
      });
  }, []);  

  return (
    <header className="header">
      <nav className="nav">
        <ul>
          {categories.map((category) => (
            <li key={category.id}>
              <Link 
                to={`/category/${category.id}`}
                onClick={() => setSelectedCategoryId(category.id)}
                className={category.id === selectedCategoryId ? 'selected' : ''}
              >
                {category.name}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
};

export default Header;
