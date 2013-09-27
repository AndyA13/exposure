import exifread


def path_exif(path_name):
    f = open(path_name, 'rb')
    return file_exif(f)


def file_exif(f):

    # Return Exif tags
    tags = exifread.process_file(f)

    tags.pop('JPEGThumbnail')

    return tags