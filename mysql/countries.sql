SELECT countries.name, languages.language, languages.percentage FROM countries
	JOIN languages ON languages.country_id = countries.id
	WHERE languages.language = "Slovene"
	ORDER BY languages.percentage DESC;
    
SELECT countries.name, COUNT(cities.id) AS number_of_cities FROM countries
	JOIN cities ON countries.id = cities.country_id
    GROUP BY cities.country_id
    ORDER BY number_of_cities DESC;

SELECT cities.name, cities.population FROM cities
	WHERE country_id = (SELECT id FROM countries
			WHERE name = "Mexico")
            AND population > 5e5
    ORDER BY population DESC;
    
SELECT countries.name, languages.language, languages.percentage FROM languages
	JOIN countries ON countries.id = languages.country_id
    WHERE languages.percentage > 89
    ORDER BY languages.percentage DESC;
    
SELECT name, surface_area, population FROM countries
	WHERE surface_area < 501 AND population > 1e5;
    
SELECT name, government_form, capital, life_expectancy FROM countries
	WHERE government_form = "Constitutional Monarchy"
    AND capital > 200
    AND life_expectancy > 75;
    
SELECT countries.name, cities.name, cities.district, cities.population FROM cities
	JOIN countries ON countries.id = cities.country_id
    WHERE countries.name  = "Argentina"
    AND cities.district = "Buenos Aires"
    AND cities.population > 5e5;

SELECT region, COUNT(id) AS num_countries FROM countries
	GROUP BY region
    ORDER BY num_countries DESC;