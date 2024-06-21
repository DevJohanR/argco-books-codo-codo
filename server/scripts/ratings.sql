CREATE TABLE `Ratings` (
  `id` integer PRIMARY KEY,
  `score` float NOT NULL,
  `book_id` integer NOT NULL,
  `created_at` datetime NOT NULL,
  FOREIGN KEY (`book_id`) REFERENCES `Books` (`id`)
);