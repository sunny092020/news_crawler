import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './ArticleDetail.css';
import { Article } from './models/index';

const ArticleDetail = () => {
  const { id } = useParams<{ id: string }>();
  const [article, setArticle] = useState<Article | null>(null);

  useEffect(() => {
    fetch(`http://10.3.0.7:8000/api/v1/articles/${id}/`)
      .then(response => response.json())
      .then(data => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data.content, 'text/html');
        doc.querySelectorAll('img').forEach(img => {
          img.src = img.getAttribute('data-src')!;
        });
        data.content = doc.body.innerHTML;
        setArticle(data);
      });
  }, [id]);

  return article ? (
    <main className="article-detail">
      <h2>{article.title}</h2>
      <p>By {article.author}</p>
      <p>{new Date(article.published_date).toLocaleDateString()}</p>
      <p>{article.summary}</p>
      <div className="content" dangerouslySetInnerHTML={{ __html: article.content }} />
    </main>
  ) : null;
};

export default ArticleDetail;
