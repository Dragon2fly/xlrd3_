from xlrd import open_workbook

from .base import from_this_dir


def test_excel_comments():
    book = open_workbook(from_this_dir('test_comments_excel.xlsx'))
    sheet = book.sheet_by_index(0)

    note_map = sheet.cell_note_map
    assert len(note_map) == 1
    assert note_map[(0, 1)].text == 'hello'


def test_excel_comments_multiline():
    book = open_workbook(from_this_dir('test_comments_excel.xlsx'))
    sheet = book.sheet_by_index(1)

    note_map = sheet.cell_note_map
    assert note_map[(1, 2)].text == '1st line\n2nd line'


def test_excel_comments_two_t_elements():
    book = open_workbook(from_this_dir('test_comments_excel.xlsx'))
    sheet = book.sheet_by_index(2)

    note_map = sheet.cell_note_map
    assert note_map[(0, 0)].text == 'Author:\nTwo t elements'


def test_excel_comments_no_t_elements():
    book = open_workbook(from_this_dir('test_comments_excel.xlsx'))
    sheet = book.sheet_by_index(3)

    note_map = sheet.cell_note_map
    assert note_map[(0, 0)].text == ''


def test_gdocs_comments():
    book = open_workbook(from_this_dir('test_comments_gdocs.xlsx'))
    sheet = book.sheet_by_index(0)

    note_map = sheet.cell_note_map
    assert len(note_map) == 1
    assert note_map[(0, 1)].text == 'Just a test'


def test_excel_comments_with_multi_sheets():
    book = open_workbook(from_this_dir('test_comments_excel_sheet2.xlsx'))
    sheet = book.sheet_by_index(1)

    note_map = sheet.cell_note_map
    assert len(note_map) == 1
    assert note_map[(1, 1)].text == 'Note lives here'
    assert len(book.sheet_by_index(0).cell_note_map) == 0
