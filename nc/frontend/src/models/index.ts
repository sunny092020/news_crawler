interface Category {
  id: number;
  name: string;
}

interface Article {
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

export type { Category, Article };
