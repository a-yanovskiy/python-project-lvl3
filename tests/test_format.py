import pytest
from page_loader.format import format_file_name, format_files_path, path_join

url_1 = 'https://habr.com/ru/post/143129/'
url_2 = 'https://ru.hexlet.io/blog/posts/how-to-find-your-first-job.png'
page_1 = 'habr-com-ru-post-143129.html'
page_2 = 'ru-hexlet-io-blog-posts-how-to-find-your-first-job.png'
files_path_name_1 = 'habr-com-ru-post-143129_files'
files_path_name_2 = 'ru-hexlet-io-blog-posts-how-to-find-your-first-job_files'
main_path = 'tests/fixtures'
full_path_1 = 'tests/fixtures/habr-com-ru-post-143129_files'
full_path_2 = 'tests/fixtures/ru-hexlet-io-blog-posts-how-to-find-your-first-job_files'


@pytest.mark.parametrize("url, result", [
    (url_1, page_1),
    (url_2, page_2),
])
def test_format_path(url, result):
    name = format_file_name(url)
    assert result == name


@pytest.mark.parametrize("page_name, files_path", [
    (page_1, files_path_name_1),
    (page_2, files_path_name_2),
])
def test_format_files_path(page_name, files_path):
    files_dir_path = format_files_path(page_name)
    assert files_dir_path == files_path


@pytest.mark.parametrize("path, files_path_name, result", [
    (main_path, files_path_name_1, full_path_1),
    (main_path, files_path_name_2, full_path_2),
])
def test_format_files_path(path, files_path_name, result):
    full_path = path_join(path, files_path_name)
    assert full_path == result
