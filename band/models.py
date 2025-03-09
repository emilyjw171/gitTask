from django.db import models


class Song(models.Model):
    """
    Represents a song in the database.

    :ivar title: The title of the song.
    :ivar album: The album to which the song belongs.
    :ivar release_date: The release date of the song.
    """

    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        """
        Returns the string representation of the song (its title).

        :return: The title of the song.
        :rtype: str
        """
        return self.title
