import sys

from PyQt5 import uic, QtWidgets, QtCore, QtMultimedia
from PyQt5.QtCore import Qt
from funcs import get_names_from_dir


class SongPlayer:
    def __init__(self, note):
        media = QtCore.QUrl.fromLocalFile(note)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def play(self):
        self.player.stop()
        self.player.play()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.comboBox.currentIndexChanged.connect(self.set_key)
        self.keyboard_to_id = \
            {Qt.Key_Q: 0, Qt.Key_W: 1, Qt.Key_E: 2, Qt.Key_R: 3, Qt.Key_T: 4, Qt.Key_Y: 5, Qt.Key_U: 6, Qt.Key_I: 7,
             Qt.Key_O: 8, Qt.Key_P: 9, Qt.Key_BracketLeft: 10, Qt.Key_BracketRight: 11,
             49: 12, 50: 13, 51: 14, 52: 15, 53: 16, 54: 17, 55: 18, 56: 19, 57: 20, 58: 21}
        self.set_key()

    def set_key(self):
        key = self.comboBox.currentText()
        notes = get_names_from_dir('notes', lambda x: key in x)
        count = 0
        for i in self.buttonGroup.buttons():
            i.song_player = SongPlayer(fr'notes\{notes[count]}')
            i.clicked.connect(i.song_player.play)
            count += 1

    def keyPressEvent(self, event):
        if event.key() in self.keyboard_to_id:
            self.buttonGroup.buttons()[self.keyboard_to_id[event.key()]].song_player.play()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
