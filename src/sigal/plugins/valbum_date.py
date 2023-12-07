"""Plugin that adds media items to date-based virtual albums

Settings::

    date_valbum_level = "year" | "month" | "day"

"""

import logging

from sigal import signals

logger = logging.getLogger(__name__)


def do_media(media):
    date_level = media.settings['valbum_date_level']
    if date_level == "year":
        album_name = media.date.strftime('%Y')
    elif date_level == "month":
        album_name = media.date.strftime('%Y-%m')
    else:
        album_name = media.date.strftime('%Y-%m-%d')
    logger.debug("Add %r to date virtual album %s", media, album_name)
    media.add_valbum(album_name, 'date')

def do_album(album, settings=None):
    pass

def register(settings):
    if settings.get("valbum_date_level"):
        signals.media_initialized.connect(do_media)
        signals.album_initialized.connect(do_album)
    else:
        logger.warning("valbum_date_level not set")

