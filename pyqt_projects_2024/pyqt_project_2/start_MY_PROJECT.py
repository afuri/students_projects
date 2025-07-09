import sys
from PyQt5.QtWidgets import QApplication
from MY_PROJECT import Start

if __name__ == '__main__':
    app = QApplication(sys.argv)
    st = Start()
    st.show()
    sys.exit(app.exec())