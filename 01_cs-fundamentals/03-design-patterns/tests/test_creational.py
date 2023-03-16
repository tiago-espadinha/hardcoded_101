import pytest
from patterns.creational.singleton.python.pattern import ConfigManager
from patterns.creational.factory.python.pattern import DocumentParserFactory
from patterns.creational.builder.python.pattern import HTTPRequestBuilder

def test_singleton_invariant():
    s1 = ConfigManager()
    s2 = ConfigManager()
    assert s1 is s2
    assert id(s1) == id(s2)

def test_factory_invariant():
    factory = DocumentParserFactory()
    pdf_parser = factory.get_parser("pdf")
    csv_parser = factory.get_parser("csv")
    assert pdf_parser.__class__.__name__ == "PDFParser"
    assert csv_parser.__class__.__name__ == "CSVParser"

def test_builder_invariant():
    builder = HTTPRequestBuilder()
    request = builder.set_url("https://api.example.com").set_method("GET").add_header("Auth", "Token").build()
    assert request.url == "https://api.example.com"
    assert request.method == "GET"
    assert "Auth" in request.headers
