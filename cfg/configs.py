
import os
from pathlib import Path


"""
=============
= P-A-T-H-S =
=============
"""

project_path = Path(__file__).parent.parent
csv_data_path = project_path / 'data' / 'Predict_Cardtype.csv'


"""
clean
"""

target_common_type = ["<class 'str'>", "<class 'bool'>"]