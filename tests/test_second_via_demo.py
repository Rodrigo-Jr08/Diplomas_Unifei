import pytest

pytest.importorskip("xsdata")

from pathlib import Path

from examples.gerar_segunda_via_demo import main


def test_second_via_demo_generates_valid_xsd_xml(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    # The example reads the schemas from its installed project tree, not tmp_path.
    main()
    assert Path("output/segunda_via_demo.xml").exists()
