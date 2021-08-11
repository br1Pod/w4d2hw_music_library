import pdb
from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

pdb.set_trace()

artist1 = Artist("The Cure")
artist_repository.save(artist1)
artist2 = Artist("The Smiths")
artist_repository.save(artist2)
artist3 = Artist("The Fall")
artist_repository.save(artist3)
artist4 = Artist("Sonic Youth")
artist_repository.save(artist4)
artist5 = Artist("The Pharcyde")
artist_repository.save(artist5)

album1 = Album("The Head On The Door", "Goth", "The Cure")
album_repository.save(album1)
album2 = Album("Strangeways Here We Come", "Indie", "The Smiths")
album_repository.save(album2)
album3 = Album("Goo", "New Wave", "Sonic Youth")
album_repository.save(album3)
album4 = Album("Labcabincalifornia", "Hip Hop", "The Pharcyde")
album_repository.save(album4)
album5 = Album("Disintegration", "Goth", "The Cure")
album_repository.save(album5)
album6 = Album("The Wonderful And Frightening World Of The Fall", "Alternative", "The Fall")
album_repository.save(album6)
album7 = Album("Daydream Nation", "New Wave", "Sonic Youth")
album_repository.save(album7)


artist_repository.select()
album_repository.select()


for album in album_repository.select_all():
    print(album.__dict__)




