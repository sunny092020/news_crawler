// src/Header.tsx
import React, { useEffect, useState } from 'react';
import './Header.css';

interface Category {
  id: number;
  name: string;
}

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
              <a href={`/${category.name}`}>{category.name}</a>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
};

export default Header;
