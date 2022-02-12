-- Imports the DB dump from hbtn_0d_tvshows to your server
SELECT tv_genres.name FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.id = tv_genres.id
WHERE tv_shows.title = 'Dexter';
