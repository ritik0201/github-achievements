import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.components.data_ingestion import DataIngestion


def test_data_ingestion_creates_artifacts():
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    assert os.path.exists(train_path)
    assert os.path.exists(test_path)
    assert os.path.exists(os.path.join(PROJECT_ROOT, 'artifacts', 'data.csv'))
