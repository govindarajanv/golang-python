class RenderJPG:
    def render(self, filename):
        print("rendering JPG file:", filename)

class RenderSVG:
    def render(self, filename):
        print("Rendering SVG file:", filename)

class RenderPNG:
    def render(self, filename):
        print("Rendering PNG file:", filename)

class ImageViewer:
    def __init__(self):
        self.jpg_renderer = RenderJPG()
        self.svg_renderer = RenderSVG()
        self.png_renderer = RenderPNG()

    def render(self, filename):
        if filename.endswith(".jpg"):
            self.jpg_renderer.render(filename)
        elif filename.endswith(".svg"):
            self.svg_renderer.render(filename)
        elif filename.endswith(".png"):
            self.png_renderer.render(filename)
        else:
            print("Unsupported file format.")

# Client code
viewer = ImageViewer()
viewer.render("nature.jpg")
viewer.render("valley.png")
viewer.render("plantuml.svg")