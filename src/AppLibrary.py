from stub_io import StubIO
from app import App
from repositories.citation_repository import CitationRepository
from database_connection import get_test_database_connection
from initialize_database import initialize_test_database
from services.citation_service import CitationServices


class AppLibrary:
    #pylint: disable=invalid-name
    def __init__(self):
        testrepo = CitationRepository(get_test_database_connection())
        self.test_services = CitationServices(testrepo)
        initialize_test_database()
        self._io = StubIO()
        self._app = App(self._io, self.test_services)
    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs
        for output in outputs:
            if value in output:
                return
        raise AssertionError(
            f"Output \"{value}\" is not in {str(outputs)}"
        )

    def run_application(self):
        self._app.run()
