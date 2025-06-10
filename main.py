from ascii import AsciiArtConverter
image_path = 'tulip.jpeg'
square_size = 40
converter = AsciiArtConverter(image_path, square_size, "@@")
converter.convert_to_ascii()
