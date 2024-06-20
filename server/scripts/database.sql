-- Script para crear la base de datos

-- Definición de la tabla Book
CREATE TABLE `Book` (
  `id` integer PRIMARY KEY,
  `isdb` varchar(13) UNIQUE NOT NULL,
  `title` varchar(255) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `synopsis` text NOT NULL,
  `publication_date` date NOT NULL,
  `author_id` integer NOT NULL,
  `category_id` integer NOT NULL
);

-- Definición de la tabla Category
CREATE TABLE `Category` (
  `id` integer PRIMARY KEY,
  `name` varchar(255) UNIQUE NOT NULL
);

-- Definición de la tabla Author
CREATE TABLE `Author` (
  `id` integer PRIMARY KEY,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL
);

-- Definición de clave externa en Book hacia Author
ALTER TABLE `Book` ADD FOREIGN KEY (`author_id`) REFERENCES `Author` (`id`);

-- Definición de clave externa en Book hacia Category
ALTER TABLE `Book` ADD FOREIGN KEY (`category_id`) REFERENCES `Category` (`id`);
