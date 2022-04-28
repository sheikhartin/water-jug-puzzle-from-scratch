#!/usr/bin/env python

import sys
from pathlib import Path

from PyQt5.QtWidgets import (QApplication, QMainWindow, QSpinBox, QComboBox,
                             QPushButton, QTextBrowser)
from PyQt5.uic import loadUi

from core import WaterJugPuzzle


class MainWindowUI(QMainWindow):
    def __init__(self) -> None:
        super(MainWindowUI, self).__init__()
        loadUi(str(Path(f'{__file__}/../qtforms/main.ui').resolve()), self)

        self.jug_a_amount = self.findChild(QSpinBox, 'jugAAmountSpinBox')
        self.jug_a_amount.valueChanged.connect(self.update_puzzle)
        self.jug_a_capacity = self.findChild(QSpinBox, 'jugACapacitySpinBox')
        self.jug_a_capacity.valueChanged.connect(self.update_puzzle)

        self.jug_b_amount = self.findChild(QSpinBox, 'jugBAmountSpinBox')
        self.jug_b_amount.valueChanged.connect(self.update_puzzle)
        self.jug_b_capacity = self.findChild(QSpinBox, 'jugBCapacitySpinBox')
        self.jug_b_capacity.valueChanged.connect(self.update_puzzle)

        self.goal_amount = self.findChild(QSpinBox, 'goalAmountSpinBox')
        self.goal_amount.valueChanged.connect(self.update_puzzle)
        self.states_browser = self.findChild(QTextBrowser, 'statesTextBrowser')

        self.next_state = self.findChild(QComboBox, 'nextStateComboBox')
        self.next_state.currentIndexChanged.connect(self.apply_state)
        self.solve_button = self.findChild(QPushButton, 'autoSolvePushButton')
        self.solve_button.clicked.connect(self.solve_automatically)

        self.water_jug_puzzle = WaterJugPuzzle(
            f'{self.jug_a_amount.value()}/{self.jug_a_capacity.value()}',
            f'{self.jug_b_amount.value()}/{self.jug_b_capacity.value()}',
            self.goal_amount.value())

    def update_puzzle(self) -> None:
        """Updates the puzzle with the current values of the jugs."""
        self.jug_a_amount.setMaximum(self.jug_a_capacity.value())
        self.jug_b_amount.setMaximum(self.jug_b_capacity.value())
        self.goal_amount.setMaximum(min(self.jug_a_amount.value() + self.jug_b_amount.value(),
                                        max(self.jug_a_capacity.value(), self.jug_b_capacity.value())))

        self.water_jug_puzzle.update(
            f'{self.jug_a_amount.value()}/{self.jug_a_capacity.value()}',
            f'{self.jug_b_amount.value()}/{self.jug_b_capacity.value()}',
            self.goal_amount.value())

    def show_puzzle_states(self) -> None:
        """Shows the puzzle states in a text browser widget."""
        self.states_browser.clear()
        self.states_browser.setText('\n'.join(list(self.water_jug_puzzle.states())))

        if self.water_jug_puzzle.done():
            self.states_browser.append('\nPuzzle solved!')
        else:
            self.states_browser.append('\nNothing has happened yet...')

    def apply_state(self, index: int) -> None:
        """Applies the selected state to the puzzle."""
        if index == 1:  # Empty both jugs
            self.water_jug_puzzle.apply(0)
        elif index == 2:  # Empty A
            self.water_jug_puzzle.apply(1)
        elif index == 3:  # Empty B
            self.water_jug_puzzle.apply(2)
        elif index == 4:  # Pour B into A
            self.water_jug_puzzle.apply(6)
        elif index == 5:  # Pour A into B
            self.water_jug_puzzle.apply(7)

        self.show_puzzle_states()

    def solve_automatically(self) -> None:
        """Solves the puzzle automatically."""
        if not self.water_jug_puzzle.done():
            self.water_jug_puzzle.solve()
        self.show_puzzle_states()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindowUI()
    main_window.show()
    sys.exit(app.exec_())
