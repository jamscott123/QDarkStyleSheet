from PySide import QtCore
import collections



def main():
    pass






class StylesheetWatcher(object):
    """
    A utility class for live-reloading Qt stylesheets.
 
    When watched, all changes made to a .css file automatically
    propagate to any running apps with live stylesheets.
    """
 
    def __init__(self):
        self._widget_sheet_map = collections.defaultdict(list)  # One-to-many map of stylesheets to their widgets
        self._watcher = None
 
    def watch(self, widget, stylesheet_path):
        """
        Establishes a live link between a widget and a stylesheet.
        When modified, the stylesheet will be reapplied to the widget.
 
        Args:
            widget: (QtGui.QWidget) A widget to apply style to.
            stylesheet_path: (str) Absolute file path on disk to a .css stylesheet.
 
        Returns: (None)
        """
        self._widget_sheet_map[stylesheet_path].append(widget)
 
        self._watcher = QtCore.QFileSystemWatcher()
        self._watcher.addPath(stylesheet_path)
 
        self._watcher.fileChanged.connect(self.update)
 
        self.update()
 
    def update(self):
        """
        Callback to reload and reapply a stylesheet when changed by the file system watcher.
 
        Returns: (None)
        """
        for stylesheet_path, widgets in self._widget_sheet_map.iteritems():
            with open(stylesheet_path, "r") as fid:
                raw_stylesheet = fid.read()
 
            for widget in widgets:
                widget.setStyleSheet(raw_stylesheet)