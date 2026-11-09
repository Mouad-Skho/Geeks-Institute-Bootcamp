const catalogItems = [
  {
    id: 1,
    title: "The Great Gatsby",
    category: "Classic Fiction",
    image: "https://covers.openlibrary.org/b/isbn/9780743273565-L.jpg",
    metric: "1925 · F. Scott Fitzgerald",
    shortDescription: "A story of wealth, love, ambition, and the American Dream.",
    fullDetails: "Published in 1925, this classic novel follows Jay Gatsby and his pursuit of Daisy Buchanan in the world of 1920s New York."
  },
  {
    id: 2,
    title: "1984",
    category: "Science Fiction",
    image: "https://covers.openlibrary.org/b/isbn/9780451524935-L.jpg",
    metric: "1949 · George Orwell",
    shortDescription: "A dystopian novel about surveillance and totalitarianism.",
    fullDetails: "Published in 1949, George Orwell's novel explores a society controlled by the Party and its leader, Big Brother."
  },
  {
    id: 3,
    title: "To Kill a Mockingbird",
    category: "Classic Fiction",
    image: "https://covers.openlibrary.org/b/isbn/9780061120084-L.jpg",
    metric: "1960 · Harper Lee",
    shortDescription: "A novel exploring justice, morality, and prejudice.",
    fullDetails: "Set in the American South during the 1930s, the story follows Scout Finch as she observes her father's defense of Tom Robinson."
  },
  {
    id: 4,
    title: "The Hobbit",
    category: "Fantasy",
    image: "https://covers.openlibrary.org/b/isbn/9780547928227-L.jpg",
    metric: "1937 · J.R.R. Tolkien",
    shortDescription: "A hobbit embarks on an unexpected adventure.",
    fullDetails: "Published in 1937, this fantasy novel follows Bilbo Baggins on a journey with a group of dwarves to reclaim their treasure from the dragon Smaug."
  },
  {
    id: 5,
    title: "Harry Potter and the Philosopher's Stone",
    category: "Fantasy",
    image: "https://covers.openlibrary.org/b/isbn/9780747532699-L.jpg",
    metric: "1997 · J.K. Rowling",
    shortDescription: "A young wizard discovers a magical world.",
    fullDetails: "The first Harry Potter novel introduces Harry, who discovers his magical heritage and begins studying at Hogwarts School of Witchcraft and Wizardry."
  },
  {
    id: 6,
    title: "The Alchemist",
    category: "Adventure",
    image: "https://covers.openlibrary.org/b/isbn/9780061122415-L.jpg",
    metric: "1988 · Paulo Coelho",
    shortDescription: "A shepherd travels in search of a hidden treasure.",
    fullDetails: "This philosophical novel follows Santiago, a young Andalusian shepherd who journeys toward the Egyptian pyramids while discovering lessons about purpose and personal dreams."
  },
  {
    id: 7,
    title: "Pride and Prejudice",
    category: "Romance",
    image: "https://covers.openlibrary.org/b/isbn/9780141439518-L.jpg",
    metric: "1813 · Jane Austen",
    shortDescription: "A classic story of relationships, class, and first impressions.",
    fullDetails: "Jane Austen's novel follows Elizabeth Bennet as she navigates family expectations, social conventions, and her changing relationship with Mr. Darcy."
  },
  {
    id: 8,
    title: "The Little Prince",
    category: "Philosophy",
    image: "https://covers.openlibrary.org/b/isbn/9780156012195-L.jpg",
    metric: "1943 · Antoine de Saint-Exupéry",
    shortDescription: "A poetic tale about friendship, love, and life.",
    fullDetails: "This novella tells the story of a young prince who travels between planets and encounters characters who offer insights into human nature and relationships."
  },
  {
    id: 9,
    title: "Atomic Habits",
    category: "Self-Development",
    image: "https://covers.openlibrary.org/b/isbn/9780735211292-L.jpg",
    metric: "2018 · James Clear",
    shortDescription: "A practical guide to building better habits.",
    fullDetails: "James Clear explains how small, consistent behavioral changes can compound over time and presents strategies for creating good habits and changing unwanted ones."
  },
  {
    id: 10,
    title: "The Book Thief",
    category: "Historical Fiction",
    image: "https://covers.openlibrary.org/b/isbn/9780375842207-L.jpg",
    metric: "2005 · Markus Zusak",
    shortDescription: "A young girl discovers the power of books during wartime.",
    fullDetails: "Set in Nazi Germany during World War II, the novel follows Liesel Meminger, a young girl who finds comfort in books and forms meaningful relationships amid hardship."
  }
  ,
  {
    id: 11,
    title: "Sapiens: A Brief History of Humankind",
    category: "Non-Fiction",
    image: "https://covers.openlibrary.org/b/isbn/9780062316097-L.jpg",
    metric: "2011 · Yuval Noah Harari",
    shortDescription: "A exploration of the history and impact of human species.",
    fullDetails: "Yuval Noah Harari traces the evolution of humankind from the Stone Age to the modern era, examining how biology and history have shaped our societies and lives."
  }
  ,
  {
    id: 12,
    title: "The Name of the Wind",
    category: "Fantasy",
    image: "https://covers.openlibrary.org/b/isbn/9780756404079-L.jpg",
    metric: "2007 · Patrick Rothfuss",
    shortDescription: "The legendary magician Kvothe tells the story of his life.",
    fullDetails: "This first book in the Kingkiller Chronicle chronicles the life of Kvothe, a magically gifted young man who grows to be the most notorious wizard his world has ever seen."
  },
  {
    id: 13,
    title: "Educated",
    category: "Memoir",
    image: "https://covers.openlibrary.org/b/isbn/9780399590504-L.jpg",
    metric: "2018 · Tara Westover",
    shortDescription: "A young woman leaves her survivalist family to pursue education.",
    fullDetails: "Tara Westover recounts her journey from growing up in a harsh, isolated mountain family to earning a PhD from Cambridge University, exploring the transformative power of education."
  },
  {
    id: 14,
    title: "Dune",
    category: "Science Fiction",
    image: "https://covers.openlibrary.org/b/isbn/9780441013593-L.jpg",
    metric: "1965 · Frank Herbert",
    shortDescription: "An epic saga of politics, religion, and desert planets.",
    fullDetails: "Set on the desert planet Arrakis, this seminal sci-fi novel follows Paul Atreides as his family takes control of the planet, the only source of the most valuable substance in the universe."
  },
  {
    id: 15,
    title: "Wuthering Heights",
    category: "Classic Fiction",
    image: "https://covers.openlibrary.org/b/isbn/9780141439556-L.jpg",
    metric: "1847 · Emily Brontë",
    shortDescription: "A passionate and tragic story of obsession and revenge on the Yorkshire moors.",
    fullDetails: "Emily Brontë's only novel tells the story of Heathcliff, an orphan who rises from poverty to become wealthy, then seeks revenge on those who wronged him, destroying lives in the process."
  }
  ,
  {
    id: 16,
    title: "Midaq Alley (Zuqaq al-Midaq)",
    category: "Classic Arabic Fiction",
    image: "https://m.media-amazon.com/images/I/81t1ue-KGzL._SL1500_.jpg",
    metric: "1947 · Naguib Mahfouz",
    shortDescription: "A Nobel Prize-winning novel about life in a crowded Cairo neighborhood.",
    fullDetails: "Naguib Mahfouz's iconic work explores the lives of residents in a historic Cairo alleyway, weaving together stories of love, struggle, and social change in mid-20th century Egypt."
  },
  {
    id: 17,
    title: "The Thief and the Dogs",
    category: "Literary Fiction",
    image: "https://a.ltrbxd.com/resized/film-poster/1/8/2/3/0/2/182302-the-thief-and-the-dogs-0-230-0-345-crop.jpg?v=62c3e1f40b",
    metric: "1961 · Naguib Mahfouz",
    shortDescription: "A psychological novel about a man released from prison seeking revenge.",
    fullDetails: "This powerful novel follows Said Mahran, who after being imprisoned for robbery, struggles to reconcile with his changed world and the people who betrayed him."
  },
  {
    id: 18,
    title: "Frankenstein in Baghdad",
    category: "Contemporary Fiction",
    image: "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1490645416i/30780005.jpg",
    metric: "2013 · Ahmed Saadawi",
    shortDescription: "A dark fantasy novel set during the Iraq War that reimagines the Frankenstein story.",
    fullDetails: "In war-torn Baghdad, a street vendor collects body parts of bomb victims and sews them together, unintentionally creating a monster that haunts the city in this award-winning blend of horror and social commentary."
  }

];