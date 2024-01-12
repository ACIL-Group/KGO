"""
    test_cvi.py

# Description
Runs each experiment within pytest to verify script functionality during CI.

# Authors
- Sasha Petrenko <sap625@mst.edu>
"""

# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------


class TestExperiments:
    """
    Pytest class containing experiment unit tests.
    """

    def test_graph_ontology(self):
        """
        Tests the main function of `main_dystonia_graph_and_ontology_method.py`.
        """
        from src.main_dystonia_graph_and_ontology_method import main
        main()
