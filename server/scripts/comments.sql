CREATE TABLE `Comments` (
  `id` integer PRIMARY KEY,
  `content` text NOT NULL,
  `book_id` integer NOT NULL,
  `created_at` datetime NOT NULL,
  FOREIGN KEY (`book_id`) REFERENCES `Books` (`id`)
);
