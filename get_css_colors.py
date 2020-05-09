import requests
from bs4 import BeautifulSoup


def get_html_page_with_css_colors(requestor=requests) -> str:
    """
    >>> from unittest import mock
    >>> requestor = mock.Mock()
    >>> requestor.get.return_value.text = "HTML"
    >>> get_html_page_with_css_colors(requestor)
    'HTML'
    """
    return requestor.get("http://www.w3schools.com/cssref/css_colors.asp").text


def get_color_mapping():
    html = get_html_page_with_css_colors()
    soup = BeautifulSoup(html)
    rows = soup.findAll("div", {"class": "w3-col l4 m6 w3-center colorbox"})
    for row in rows:
        colorName = row.find("span", {"class": "colornamespan"}).text
        colorValue = row.find("span", {"class": "colorhexspan"}).text
        yield colorName, colorValue


def create_xml(mapping):
    yield "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
    yield "<resources>"
    for colorName, colorValue in mapping:
        yield "    <color name=\"{}\">{}</color>".format(colorName, colorValue)
    yield "</resources>"


def main(color_getter=get_color_mapping, xml_creator=create_xml):
    """
    >>> from unittest import mock
    >>> fake_get_color_mapping = mock.Mock()
    >>> mapping = [("name", "#DEADBEAF")]
    >>> fake_get_color_mapping.return_value = mapping
    >>> fake_create_xml = mock.Mock()
    >>> fake_create_xml.return_value = ["line1", "line2"]
    >>> main(fake_get_color_mapping, fake_create_xml)
    'line1\\nline2'
    >>> fake_create_xml.assert_called_once_with(mapping)
    """
    return "\n".join(
        xml_creator(
            color_getter()
        )
    )


if __name__ == "__main__":
    print(main())
