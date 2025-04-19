import matplotlib.pyplot as plt
from fontTools.pens.basePen import BasePen
from fontTools.ttLib import TTFont

font = TTFont("fonts\\Borel-Regular.ttf", fontNumber=0)
# print('glyphID is: ' + str(font.getGlyphID("a")))

class MatplotlibPen(BasePen):
    def __init__(self, glyphSet):
        super().__init__(glyphSet)
        self.paths = []

    def _moveTo(self, p0):
        self.paths.append([p0])

    def _lineTo(self, p1):
        self.paths[-1].append(p1)

    def _curveToOne(self, p1, p2, p3):
        self.paths[-1].extend([p1, p2, p3])

    def _closePath(self):
        self.paths[-1].append(self.paths[-1][0])

text = "winsor"  # String of characters to plot
x_offset = 0  # Initial x-offset for positioning characters
spacing = 100  # Spacing between characters

scale = 1  # Scale factor for the plot
plt.figure(figsize=(10 * scale, 5 * scale))  # Set figure size

# Open a file to save the coordinates
with open("coordinates.txt", "w") as file:
    for char in text:
        glyph = font.getGlyphSet()[char]
        pen = MatplotlibPen(font.getGlyphSet())
        glyph.draw(pen)
        
        # Plot the glyph with the current x_offset
        for path in pen.paths:
            x, y = zip(*path)
            x = [point_x + x_offset for point_x in x]  # Apply x_offset to x-coordinates
            # Add a seperator between glyphs, hehe...
            file.write("==========================\n")
            for point_x, point_y in zip(x, y):
                # Save the coordinates to the file
                file.write(f"{point_x}, {point_y}\n")
            plt.plot(x, y, marker='o')
        
        # Update x_offset for the next character
        x_offset += glyph.width + spacing

plt.gcf().canvas.manager.set_window_title("Font Glyphs through Points")
plt.axis('equal')
plt.show()