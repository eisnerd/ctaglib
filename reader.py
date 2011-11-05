from taglib import *

from optparse import OptionParser
import sys
import os

def display (f):
 try:
  file = taglib_file_new(f);
  if bool(file) and taglib_file_is_valid(file):
   try:
    print
    print f
    print
	
    tag = taglib_file_tag(file)
    if bool(tag):
     print("   title: \"%s\"" % taglib_tag_title(tag))
     print("  artist: \"%s\"" % taglib_tag_artist(tag))
     print("   album: \"%s\"" % taglib_tag_album(tag))
     print("    year: \"%i\"" % taglib_tag_year(tag))
     print(" comment: \"%s\"" % taglib_tag_comment(tag))
     print("   track: \"%i\"" % taglib_tag_track(tag))
     print("   genre: \"%s\"" % taglib_tag_genre(tag))

    print(" pictures: \"%i\"" % taglib_file_picture_count(file))
    for picture in pictures(file):
      print("           %s %s %i" % (picture.typename, picture.mimetype, len(picture.base64data)))

    if bool(tag):
        print

    properties = taglib_file_audioproperties(file)
    if bool(properties):
     duration = taglib_audioproperties_length(properties)
     print("     bitrate: %i" % taglib_audioproperties_bitrate(properties))
     print(" sample rate: %i" % taglib_audioproperties_samplerate(properties))
     print("    channels: %i" % taglib_audioproperties_channels(properties))
     print("      length: %i:%02i\n" % (duration // 60, duration % 60))
	
   finally:
    taglib_tag_free_strings()
    taglib_file_free(file)
 except Exception, error:
  print >> sys.stderr, '%s: %s' % (f, error)

def visit (a, d, fs):
 for f in fs:
  display(os.path.join(d,f))

def walk (p):
 if os.path.isfile(p):
   display(p)
 else:
   os.path.walk (p, visit, {})

def main(args=None):
    optparse = OptionParser('%prog <dir | file ...>', version="1.7.0",
                            description='Display media metadata')
    args = optparse.parse_args(args)[1]
    if not args:
        optparse.print_help()
        return 1
    try:
        for path in args:
			walk (path)
    except KeyboardInterrupt:
        return 2
    return 0

if __name__ == '__main__':
    sys.exit(main())

def main():
	for path in sys.argv[1:]:
		print path

		if not (bool(file) and taglib_file_is_valid(file)):
			print 'Could not open ' + path
			break

		tag = taglib_file_tag(file)
		print file
		properties = taglib_file_audioproperties(file)
		if not tag is None:
			print("-- TAG --\n");
			print("title   - \"%s\"\n" % taglib_tag_title(tag))
			print("artist  - \"%s\"\n" % taglib_tag_artist(tag))
			print("album   - \"%s\"\n" % taglib_tag_album(tag))
			print("year    - \"%i\"\n" % taglib_tag_year(tag))
			print("comment - \"%s\"\n" % taglib_tag_comment(tag))
			print("track   - \"%i\"\n" % taglib_tag_track(tag))
			print("genre   - \"%s\"\n" % taglib_tag_genre(tag))

		taglib_tag_free_strings()
		taglib_file_free(file)

if __name__ == "__main__":
    main()