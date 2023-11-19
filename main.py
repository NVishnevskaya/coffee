import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from sql_functions import get_all_items, insert_row

GROUND_TEXT = "Молотый"


class ViewCoffeeItemWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('main.ui', self)
        self.add_item_btn.clicked.connect(self.add_item)
        self.fill_items_table()

    def fill_items_table(self) -> None:
        raw_data = get_all_items()
        self.items_table.setRowCount(len(raw_data))
        for index_row in range(0, len(raw_data)):
            for index_element in range(1, len(raw_data[0])):
                self.items_table.setItem(index_row, index_element - 1, QTableWidgetItem(
                    str(raw_data[index_row][index_element])))
        self.items_table.resizeColumnsToContents()

    def add_item(self):
        dialog_ex = AddCoffeeItemWidget(self)
        dialog_ex.exec_()


class AddCoffeeItemWidget(QDialog):
    def __init__(self, parent=None):
        super(AddCoffeeItemWidget, self).__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.ok_btn.clicked.connect(self.insert_item)
        self.parent = parent

    def insert_item(self):
        sort_text = self.sort_edit.text().strip()
        degree_text = self.degree_edit.text().strip()
        is_ground_value = "TRUE" if self.type_edit.currentText().strip() == GROUND_TEXT else "FALSE"
        description_text = self.f_description_text.toPlainText().strip()
        current_price = int(self.price_edit.text().strip())
        current_capacity = int(self.capacity_edit.text().strip())
        insert_row(sort_text, degree_text, is_ground_value, description_text, current_price, current_capacity)
        self.parent.fill_items_table()


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = ViewCoffeeItemWidget()
    ex.show()
    sys.exit(app.exec_())
