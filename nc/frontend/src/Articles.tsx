import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import './Articles.css';
import { Article } from './models/index';


const Articles = () => {
  const { categoryId } = useParams<{ categoryId: string }>();
  const [articles, setArticles] = useState<Article[]>([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_BASE_URL}/articles?category__id=${categoryId}`)
      .then(response => response.json())
      .then(data => setArticles(data.results))
      .catch(error => {
        console.error('Error:', error);
      });
  }, [categoryId]);  

  return (
    <main>
      <ul>
        {articles.map((article) => (
          <li key={article.id} className="article-item">
            <img src={article.thumbnail} alt={article.title} className="article-thumbnail" />
            <div>
              <div className="article-info">
                <Link to={`/article/${article.id}`}>
                  <h3 className="article-title">{article.title}</h3>
                </Link>
                <p className="article-date">{new Date(article.published_date).toLocaleDateString()}</p>
                <p className="article-site">{article.site}</p>  {/* Display the site */}
              </div>
              <p>{article.summary}</p>
            </div>
          </li>
        ))}
      </ul>
    </main>
  );
};

export default Articles;
