# main func
def main():
    extension_to_media_type(input('file name: '))


# turns extensions to a media type
# jpg jpef gif png pdf zip txt only
# returns application/octet-stream if not in previous list
def extension_to_media_type(file_name):
    # removes empty space and makes a list with '.' as a sep
    file_name = file_name.strip()
    file_name = file_name.split('.')

    # gets extension type and name of the thingy
    extension = file_name[-1].lower()
    name = file_name[0]

    # sorts extension to its relevant media type
    match extension:
        case 'jpeg' | 'jpg':
            print(f'image/jpeg')
        case 'gif' | 'png':
            print(f'image/{extension}')
        case 'pdf' | 'zip':
            print(f'application/{extension}')
        case 'txt':
            print(f'text/{name}')
        case _:
            print('application/octet-stream')


main()
