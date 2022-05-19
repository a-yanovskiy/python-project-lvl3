import os
import tempfile

from page_loader.scripts.page_loader import download


def test_download():
    web_page = 'https://ru.hexlet.io/courses'
    with tempfile.TemporaryDirectory() as tmpdir:
        total_path = download(web_page, tmpdir)
    assert os.path.join(tmpdir, 'ru-hexlet-io-courses.html') == total_path
