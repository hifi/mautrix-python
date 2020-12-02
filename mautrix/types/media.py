# Copyright (c) 2020 Tulir Asokan
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from .primitive import ContentURI
from .util import SerializableAttrs, field, dataclass


@dataclass
class MediaRepoConfig(SerializableAttrs['MediaRepoConfig']):
    """
    Matrix media repo config. See `GET /_matrix/media/r0/config`_.

    .. _GET /_matrix/media/r0/config:
        https://matrix.org/docs/spec/client_server/r0.5.0#get-matrix-media-r0-config
    """
    upload_size: int = field(json="m.upload_size")


@dataclass
class OpenGraphImage(SerializableAttrs['OpenGraphImage']):
    url: ContentURI = field(default=None, json="og:image")
    mimetype: str = field(default=None, json="og:image:type")
    height: int = field(default=None, json="og:image:width")
    width: int = field(default=None, json="og:image:height")
    size: int = field(default=None, json="matrix:image:size")


@dataclass
class OpenGraphVideo(SerializableAttrs['OpenGraphVideo']):
    url: ContentURI = field(default=None, json="og:video")
    mimetype: str = field(default=None, json="og:video:type")
    height: int = field(default=None, json="og:video:width")
    width: int = field(default=None, json="og:video:height")
    size: int = field(default=None, json="matrix:video:size")


@dataclass
class OpenGraphAudio(SerializableAttrs['OpenGraphAudio']):
    url: ContentURI = field(default=None, json="og:audio")
    mimetype: str = field(default=None, json="og:audio:type")


@dataclass
class MXOpenGraph(SerializableAttrs['MXOpenGraph']):
    """
    Matrix URL preview response. See `GET /_matrix/media/r0/preview_url`_.

    .. _GET /_matrix/media/r0/preview_url:
        https://matrix.org/docs/spec/client_server/r0.5.0#get-matrix-media-r0-preview-url
    """
    title: str = field(default=None, json="og:title")
    description: str = field(default=None, json="og:description")
    image: OpenGraphImage = field(default=None, flatten=True)
    video: OpenGraphVideo = field(default=None, flatten=True)
    audio: OpenGraphAudio = field(default=None, flatten=True)
