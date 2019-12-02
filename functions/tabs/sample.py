#!/usr/bin/python3

from gi.repository import Poppler, Gtk

def draw(widget, surface):
    page.render(surface)

document = Poppler.Document.new_from_file("file:///home/me/some.pdf", None)
page = document.get_page(0)

window = Gtk.Window(title="Hello World")
window.connect("delete-event", Gtk.main_quit)
window.connect("draw", draw)
window.set_app_paintable(True)

window.show_all()
Gtk.main()