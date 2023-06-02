import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './ArticleDetail.css';
import { Article } from '../models/index';

const ArticleDetail = () => {
  const { id } = useParams<{ id: string }>();
  const [article, setArticle] = useState<Article | null>(null);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_BASE_URL}/articles/${id}/`)
      .then(response => response.json())
      .then(data => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data.content, 'text/html');
        doc.querySelectorAll('img').forEach(img => {
          img.src = img.getAttribute('data-src')!;
        });
        data.content = doc.body.innerHTML;
        setArticle(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, [id]);
  
  return article ? (
    <main className="article-detail">
      <h2>{article.title}</h2>
      <p>By {article.author}</p>
      <p>{new Date(article.published_date).toLocaleString()}</p>
      <p>{article.summary}</p>
      <div className="content" dangerouslySetInnerHTML={{ __html: article.content }} />
    </main>
  ) : null;
};

export default ArticleDetail;
