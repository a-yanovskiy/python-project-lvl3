from page_loader.path import format_file_name, format_folder_name


url = 'https://ru.hexlet.io/courses'

filepath = 'tests/fixtures/habr-com-ru-post-143129.html'
files_dir_name = 'habr-com-ru-post-143129_files'


def test_file_name():
    assert format_file_name(url, '.html') == 'ru-hexlet-io-courses.html'


def test_folder_name():
    assert format_folder_name(filepath) == files_dir_name
