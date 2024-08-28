import unittest
from airflow.models import DagBag


class TestDagOne(unittest.TestCase):

    def test_dag_loads_with_no_errors(self):
        dag_bag = DagBag(dag_folder='./',
                         include_examples=False)
        assert len(dag_bag.import_errors) == 0

    def test_contains_tasks(self):
        dag_bag = DagBag(dag_folder='./',
                         include_examples=False)
        dag_id = 'sample_dag'
        dag = dag_bag.get_dag(dag_id)
        assert dag is not None
        assert len(dag.tasks) == 1
