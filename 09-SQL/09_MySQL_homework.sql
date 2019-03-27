use sakila;
select * from actor;
SELECT * FROM sakila.country;
select * from film;
select * from address;
select * from staff;
select * from payment;
select * from film_actor;
select * from inventory;
select * from customer;
select * from language;

-- 1a.
SELECT first_name, last_name FROM actor;

-- 1b.
SELECT CONCAT(first_name,' ',last_name) AS 'Actor Name' FROM actor;

-- 2a.
SELECT actor_id, first_name, last_name FROM actor WHERE first_name = "Joe";

-- 2b.
SELECT * FROM actor WHERE last_name LIKE "%GEN%";

-- 2c.

SELECT * FROM actor WHERE last_name LIKE "%LI%" ORDER BY ast_name, first_name;

-- 2d.
SELECT country_id, country FROM country WHERE country IN ("Afghanistan", "Bangladesh", "China");

-- 3a.
ALTER TABLE `sakila`.`actor` 
ADD COLUMN `description` BLOB NULL AFTER `last_update`;

-- 3b.
ALTER TABLE `sakila`.`actor` 
DROP COLUMN `description`;

-- 4a.
SELECT last_name, COUNT(*) FROM actor GROUP BY last_name;

-- 4b.
SELECT last_name,COUNT(*) FROM actor GROUP BY last_name HAVING COUNT(*) >= 2;

-- 4c.
SELECT * FROM actor WHERE first_name = "GROUCHO" AND last_name = "WILLIAMS";
UPDATE actor SET first_name = "HARPO" WHERE first_name = "GROUCHO" AND last_name = "WILLIAMS";
SELECT * FROM actor WHERE last_name = "WILLIAMS";

-- 4d.
SELECT * FROM actor WHERE first_name = "HARPO";
UPDATE actor SET first_name = "GROUCHO" WHERE first_name = "HARPO" AND last_name = "WILLIAMS";

-- 5a.
SHOW CREATE TABLE address;

-- 6a. 
SELECT s.first_name, s.last_name, a.address 
FROM staff AS s 
LEFT JOIN address AS a 
ON a.address_id = s.address_id;

-- 6b.
SELECT s.first_name, s.last_name, SUM(p.amount)
FROM staff AS s
LEFT JOIN payment AS p ON s.staff_id = p.staff_id
WHERE payment_date LIKE '2005-08%'
GROUP BY p.staff_id; 

-- 6c.
SELECT f.title, COUNT(fa.film_id) AS 'number of actors'
FROM film AS f
INNER JOIN film_actor AS fa 
ON fa.film_id = f.film_id
GROUP BY fa.film_id;

-- 6d.
SELECT (SELECT title FROM film WHERE title = "Hunchback Impossible")AS 'title', COUNT(i.film_id) AS 'number of copies'
FROM inventory AS i
LEFT JOIN film
ON i.film_id = film.film_id
WHERE i.film_id = (SELECT film_id FROM film WHERE title = "Hunchback Impossible" );

-- 6e.
SELECT c.first_name, c.last_name, SUM(p.amount) AS "Total Amount Paid"
FROM customer AS c
LEFT JOIN payment AS p
ON c.customer_id = p.customer_id
GROUP BY c.customer_id
ORDER BY c.last_name;

-- 7a.
SELECT title 
FROM film
WHERE (title LIKE "K%" OR title LIKE "Q%") AND language_id = (SELECT language_id FROM language WHERE name="English") ;

-- 7b.
SELECT actor.first_name, actor.last_name, actor.actor_id
FROM actor
WHERE actor_id IN (SELECT actor_id FROM film_actor WHERE film_id = (SELECT film_id FROM film WHERE title = "Alone Trip"));

-- 7c.
SELECT c.first_name, c.last_name, c.email
FROM customer AS c
JOIN address AS a ON c.address_id = a.address_id 
JOIN city AS cy ON cy.city_id = a.city_id
WHERE cy.city_id IN (SELECT city.city_id FROM city WHERE country_id = (SELECT country_id FROM country WHERE country = "Canada"));

-- 7d.
SELECT title
FROM film
WHERE film.film_id IN (SELECT film_id
FROM film_category
WHERE category_id=(SELECT category_id FROM category WHERE name = "Family"));

-- 7e.
SELECT f.title -- , count(r.inventory_id) as "Popular Movie"
FROM rental AS r
INNER JOIN inventory AS i
ON i.inventory_id = r.inventory_id
INNER JOIN film AS f
ON f.film_id = i.film_id
GROUP BY i.film_id
ORDER BY COUNT(r.inventory_id) DESC;

-- 7f.
SELECT s.store_id,SUM(amount)
FROM store AS s
INNER JOIN payment AS p
ON s.store_id = p.staff_id
GROUP BY staff_id;

-- 7g.

SELECT store_id, c.city, co.country
FROM address AS a 
JOIN store AS s
ON a.address_id = s.address_id 
JOIN city AS c
ON c.city_id = a.city_id
JOIN country AS co
ON c.country_id = co.country_id
WHERE a.address_id IN (SELECT address_id FROM store);

-- 7h.
SELECT film_id, SUM(amount)
FROM rental AS r
INNER JOIN inventory AS i
ON i.inventory_id = r.inventory_id
INNER JOIN payment AS p
ON p.rental_id = r.rental_id
GROUP BY film_id
ORDER BY SUM(amount) DESC 
LIMIT 5;

SELECT name
FROM category
WHERE category_id IN (SELECT category_id
FROM film_category 
WHERE film_id IN (879, 973, 1000, 369, 764));

-- 8a.
CREATE VIEW top_five_genres AS 
SELECT name
FROM category
WHERE category_id IN (SELECT category_id
FROM film_category 
WHERE film_id IN (879, 973, 1000, 369, 764));

SELECT * FROM top_five_genres;

-- 8b.
DROP VIEW top_five_genres;

























