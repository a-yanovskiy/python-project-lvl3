import os
import tempfile
import pytest
import page_loader.link as download


html_1 = 'tests/fixtures/habr-com-ru-post-143129.html'
result_1 = []


@pytest.mark.parametrize("html, result", [
    (html_1, result_1),
    # (url_2, result_2),
])
def test_main_page(html, result):
    with tempfile.TemporaryDirectory() as tmpdir:

        total_path = download.format_file_name()
        path = os.path.join(tmpdir, result)
    assert total_path == path
