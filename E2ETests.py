import pytest
from guiInterface import Ui_Dialog


@pytest.fixture
def app(qtbot):
    application = Ui_Dialog()
    qtbot.addWidget(application)
    return application


def test_empty_string(app):
    app.textEdit.setText("")
    app.pushButton.click()
    assert "" == app.label_2.toPlainText()

def test_correct_time(app):
    app.textEdit.setText("06:00")
    app.pushButton.click()
    assert "06:00" == app.label_2.toPlainText()

def test_correct_time_with_spaces(app):
    app.textEdit.setText(" 06:00  ")
    app.pushButton.click()
    assert "06:00" == app.label_2.toPlainText()






