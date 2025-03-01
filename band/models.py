from django.db import models


class Song(models.Model):
    """
    Represents a song in the database with a title, album, and release date.

    Attributes:
        title (CharField): The title of the song.
        album (CharField): The album to which the song belongs.
        release_date (DateField): The release date of the song.

    Methods:
        __str__(): Returns a string representation of the song's title.
    """
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        """
        Returns the string representation of the song (its title).

        Returns:
            str: The title of the song.
        """
        return self.title
