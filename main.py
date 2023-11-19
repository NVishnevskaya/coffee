import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from sql_functions import get_all_items


class ViewCoffeeItemWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('main.ui', self)
        self.fill_items_table()

    def fill_items_table(self) -> None:
        raw_data = get_all_items()
        self.items_table.setRowCount(len(raw_data))
        for index_row in range(0, len(raw_data)):
            for index_element in range(1, len(raw_data[0])):
                self.items_table.setItem(index_row, index_element - 1, QTableWidgetItem(
                    raw_data[index_row][index_element]))


class AddCoffeeItemWidget(QWidget):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViewCoffeeItemWidget()
    ex.show()
    sys.exit(app.exec_())

