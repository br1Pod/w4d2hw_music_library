from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    pass


def select(id):
    pass


def delete(id):
    pass

def select_all():
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        release = Album(row['title'], row['genre'], row['artist'])
        albums.append(release)
    return albums

def update(album):
    pass
