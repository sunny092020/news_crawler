import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import './Articles.css';

interface Article {
  id: number;
  title: string;
  thumbnail: string;
  summary: string;
  published_date: string;
}

const Articles = () => {
  const { categoryId } = useParams<{ categoryId: string }>();
  const [articles, setArticles] = useState<Article[]>([]);

  useEffect(() => {
    fetch(`http://10.3.0.7:8000/api/v1/articles?category__id=${categoryId}`)
      .then(response => response.json())
      .then(data => setArticles(data.results));
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
