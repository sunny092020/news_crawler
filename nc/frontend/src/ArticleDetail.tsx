import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './ArticleDetail.css';

interface Category {
  id: number;
  name: string;
}

interface ArticleDetail {
  id: number;
  category: Category;
  title: string;
  url: string;
  author: string;
  published_date: string;
  content: string;
  site: string;
  thumbnail: string;
  summary: string;
}

const ArticleDetail = () => {
  const { id } = useParams<{ id: string }>();
  const [article, setArticle] = useState<ArticleDetail | null>(null);

  useEffect(() => {
    fetch(`http://10.3.0.7:8000/api/v1/articles/${id}/`)
      .then(response => response.json())
      .then(data => setArticle(data));
  }, [id]);

  if (!article) {
    return <div>Loading...</div>;
  }

  return (
    <main className="article-detail">
      <h2>{article.title}</h2>
      <p>By {article.author}</p>
      <p>{new Date(article.published_date).toLocaleDateString()}</p>
      <p>{article.summary}</p>
      <div className="content" dangerouslySetInnerHTML={{ __html: article.content }} />
    </main>
  );  
};

export default ArticleDetail;
