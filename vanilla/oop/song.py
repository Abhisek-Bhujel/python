class Song:
    """Class to represent a song

    Attributes:
        title(str): The title of the song
        artist (Artist):An artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialise the 'title attribute
            artist (Artist): An Artist object representing the song's creator.
            duration (int, optional): Initial value of duration attribute. Defaults to 0.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist: (Artist): The artist responsible for album.If not specified
        artist will default to an artist with name "Various Artists".
        tracks (List[Song]): A list of songs on the album.

    Methods:
        addSong: Used to add a new song to the album's track list.

    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Add a song to a track list

        Args:
            song (Song): A song to be added
            position (int, optional): If specified, the song will be added to that position.
            Defaults to None i.e will be added to the end of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.

    Methods:
        add_album: Use to add new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list
        """
        self.albums.append(album)


def find_object(field, object_list):
    """Check object_list to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(
                line.strip("\n").split("\t")
            )
            year_field = int(year_field)
            print(
                "{}: {}: {}: {}".format(
                    artist_field, album_field, year_field, song_field
                )
            )

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # We have just read details for a new artist
                # retrieve the new_artist if there is one
                # otherwise create a new_artist object and add it to the artist_list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # We've just read a new_album for the current artist
                # retrieve the new_album if there is one
                # otherwise create a new_album object and add it to the artist collection
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


if __name__ == "__main__":
    artist = load_data()
    print("There are {} artist". format(len(artist)))
