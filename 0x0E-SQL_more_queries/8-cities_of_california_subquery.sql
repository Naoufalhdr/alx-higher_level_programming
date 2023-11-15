-- Lists all the cities of California in the database 'hbtn_0d_usa'
SELECT id, name
FROM states, cities
WHERE states.id = cities.id
ORDER BY id;
