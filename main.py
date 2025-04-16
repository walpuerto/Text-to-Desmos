from fontTools.ttLib import TTFont
font = TTFont("cambria.ttc", fontNumber=0)
print('glyphID is: ' + str(font.getGlyphID("a")))
print(ord('a'))