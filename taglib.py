from ctypes import *

_libraries = {}
_libraries['libtag_c.so'] = CDLL('libtag_c.so')
STRING = c_char_p


TagLib_ID3v2_UTF8 = 3
TagLib_ID3v2_UTF16BE = 2
TagLib_ID3v2_Latin1 = 0
TagLib_File_ASF = 9
TagLib_File_MP4 = 8
TagLib_File_TrueAudio = 7
TagLib_File_Speex = 6
TagLib_File_WavPack = 5
TagLib_File_OggFlac = 4
TagLib_File_MPC = 3
TagLib_File_FLAC = 2
TagLib_File_OggVorbis = 1
# BOOL = int # alias
TagLib_File_MPEG = 0
TagLib_ID3v2_UTF16 = 1
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
class TagLib_File(Structure):
    pass
TagLib_File._fields_ = [
    ('dummy', c_int),
]
class TagLib_Tag(Structure):
    pass
TagLib_Tag._fields_ = [
    ('dummy', c_int),
]
class TagLib_AudioProperties(Structure):
    pass
TagLib_AudioProperties._fields_ = [
    ('dummy', c_int),
]
taglib_set_strings_unicode = _libraries['libtag_c.so'].taglib_set_strings_unicode
taglib_set_strings_unicode.restype = None
taglib_set_strings_unicode.argtypes = [c_int]
taglib_set_string_management_enabled = _libraries['libtag_c.so'].taglib_set_string_management_enabled
taglib_set_string_management_enabled.restype = None
taglib_set_string_management_enabled.argtypes = [c_int]
taglib_free = _libraries['libtag_c.so'].taglib_free
taglib_free.restype = None
taglib_free.argtypes = [c_void_p]

# values for enumeration 'TagLib_File_Type'
TagLib_File_Type = c_int # enum
taglib_file_new = _libraries['libtag_c.so'].taglib_file_new
taglib_file_new.restype = POINTER(TagLib_File)
taglib_file_new.argtypes = [STRING]
taglib_file_new_type = _libraries['libtag_c.so'].taglib_file_new_type
taglib_file_new_type.restype = POINTER(TagLib_File)
taglib_file_new_type.argtypes = [STRING, TagLib_File_Type]
taglib_file_free = _libraries['libtag_c.so'].taglib_file_free
taglib_file_free.restype = None
taglib_file_free.argtypes = [POINTER(TagLib_File)]
taglib_file_is_valid = _libraries['libtag_c.so'].taglib_file_is_valid
taglib_file_is_valid.restype = c_int
taglib_file_is_valid.argtypes = [POINTER(TagLib_File)]
taglib_file_tag = _libraries['libtag_c.so'].taglib_file_tag
taglib_file_tag.restype = POINTER(TagLib_Tag)
taglib_file_tag.argtypes = [POINTER(TagLib_File)]
taglib_file_audioproperties = _libraries['libtag_c.so'].taglib_file_audioproperties
taglib_file_audioproperties.restype = POINTER(TagLib_AudioProperties)
taglib_file_audioproperties.argtypes = [POINTER(TagLib_File)]
taglib_file_save = _libraries['libtag_c.so'].taglib_file_save
taglib_file_save.restype = c_int
taglib_file_save.argtypes = [POINTER(TagLib_File)]
taglib_tag_title = _libraries['libtag_c.so'].taglib_tag_title
taglib_tag_title.restype = STRING
taglib_tag_title.argtypes = [POINTER(TagLib_Tag)]
taglib_tag_artist = _libraries['libtag_c.so'].taglib_tag_artist
taglib_tag_artist.restype = STRING
taglib_tag_artist.argtypes = [POINTER(TagLib_Tag)]
taglib_tag_album = _libraries['libtag_c.so'].taglib_tag_album
taglib_tag_album.restype = STRING
taglib_tag_album.argtypes = [POINTER(TagLib_Tag)]
taglib_tag_comment = _libraries['libtag_c.so'].taglib_tag_comment
taglib_tag_comment.restype = STRING
taglib_tag_comment.argtypes = [POINTER(TagLib_Tag)]
taglib_tag_genre = _libraries['libtag_c.so'].taglib_tag_genre
taglib_tag_genre.restype = STRING
taglib_tag_genre.argtypes = [POINTER(TagLib_Tag)]
taglib_tag_year = _libraries['libtag_c.so'].taglib_tag_year
taglib_tag_year.restype = c_uint
taglib_tag_year.argtypes = [POINTER(TagLib_Tag)]
taglib_tag_track = _libraries['libtag_c.so'].taglib_tag_track
taglib_tag_track.restype = c_uint
taglib_tag_track.argtypes = [POINTER(TagLib_Tag)]
taglib_tag_set_title = _libraries['libtag_c.so'].taglib_tag_set_title
taglib_tag_set_title.restype = None
taglib_tag_set_title.argtypes = [POINTER(TagLib_Tag), STRING]
taglib_tag_set_artist = _libraries['libtag_c.so'].taglib_tag_set_artist
taglib_tag_set_artist.restype = None
taglib_tag_set_artist.argtypes = [POINTER(TagLib_Tag), STRING]
taglib_tag_set_album = _libraries['libtag_c.so'].taglib_tag_set_album
taglib_tag_set_album.restype = None
taglib_tag_set_album.argtypes = [POINTER(TagLib_Tag), STRING]
taglib_tag_set_comment = _libraries['libtag_c.so'].taglib_tag_set_comment
taglib_tag_set_comment.restype = None
taglib_tag_set_comment.argtypes = [POINTER(TagLib_Tag), STRING]
taglib_tag_set_genre = _libraries['libtag_c.so'].taglib_tag_set_genre
taglib_tag_set_genre.restype = None
taglib_tag_set_genre.argtypes = [POINTER(TagLib_Tag), STRING]
taglib_tag_set_year = _libraries['libtag_c.so'].taglib_tag_set_year
taglib_tag_set_year.restype = None
taglib_tag_set_year.argtypes = [POINTER(TagLib_Tag), c_uint]
taglib_tag_set_track = _libraries['libtag_c.so'].taglib_tag_set_track
taglib_tag_set_track.restype = None
taglib_tag_set_track.argtypes = [POINTER(TagLib_Tag), c_uint]
taglib_tag_free_strings = _libraries['libtag_c.so'].taglib_tag_free_strings
taglib_tag_free_strings.restype = None
taglib_tag_free_strings.argtypes = []
taglib_audioproperties_length = _libraries['libtag_c.so'].taglib_audioproperties_length
taglib_audioproperties_length.restype = c_int
taglib_audioproperties_length.argtypes = [POINTER(TagLib_AudioProperties)]
taglib_audioproperties_bitrate = _libraries['libtag_c.so'].taglib_audioproperties_bitrate
taglib_audioproperties_bitrate.restype = c_int
taglib_audioproperties_bitrate.argtypes = [POINTER(TagLib_AudioProperties)]
taglib_audioproperties_samplerate = _libraries['libtag_c.so'].taglib_audioproperties_samplerate
taglib_audioproperties_samplerate.restype = c_int
taglib_audioproperties_samplerate.argtypes = [POINTER(TagLib_AudioProperties)]
taglib_audioproperties_channels = _libraries['libtag_c.so'].taglib_audioproperties_channels
taglib_audioproperties_channels.restype = c_int
taglib_audioproperties_channels.argtypes = [POINTER(TagLib_AudioProperties)]

# values for enumeration 'TagLib_ID3v2_Encoding'
TagLib_ID3v2_Encoding = c_int # enum
taglib_id3v2_set_default_text_encoding = _libraries['libtag_c.so'].taglib_id3v2_set_default_text_encoding
taglib_id3v2_set_default_text_encoding.restype = None
taglib_id3v2_set_default_text_encoding.argtypes = [TagLib_ID3v2_Encoding]
__all__ = ['taglib_tag_comment', 'TagLib_ID3v2_Encoding',
           'TagLib_File_FLAC', 'taglib_audioproperties_length',
           'TagLib_ID3v2_UTF8', 'taglib_file_free',
           'taglib_tag_track', 'taglib_audioproperties_bitrate',
           'taglib_tag_set_album', 'taglib_tag_year',
           'taglib_audioproperties_channels',
           'taglib_id3v2_set_default_text_encoding',
           '__STDC_CONSTANT_MACROS',
           'taglib_set_string_management_enabled', 'TagLib_Tag',
           'TagLib_File_WavPack', 'taglib_file_audioproperties',
           'TagLib_File_TrueAudio', 'taglib_tag_set_comment',
           'TagLib_ID3v2_Latin1', 'taglib_audioproperties_samplerate',
           'taglib_tag_set_title', 'taglib_tag_album',
           'TagLib_File_MP4', 'taglib_tag_genre', 'taglib_tag_title',
           'TagLib_File_ASF', 'taglib_tag_set_artist',
           'taglib_tag_free_strings', 'taglib_file_save',
           'TagLib_File_OggVorbis', 'taglib_free',
           'taglib_file_new_type', 'taglib_tag_set_year',
           'taglib_tag_artist', 'taglib_file_new',
           'TagLib_ID3v2_UTF16', 'TagLib_File', 'TagLib_File_MPC',
           'TagLib_AudioProperties', 'TagLib_File_Speex',
           'taglib_set_strings_unicode', 'taglib_file_tag',
           'taglib_tag_set_genre', 'TagLib_File_MPEG',
           'TagLib_File_Type', 'taglib_file_is_valid',
           'TagLib_File_OggFlac', 'taglib_tag_set_track',
           'TagLib_ID3v2_UTF16BE']
