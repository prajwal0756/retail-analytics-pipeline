from src.etl_pipeline import run_etl
from src.rfm_segmentation import calculate_rfm
from src.report_generation import generate_reports
import logging
import os

os.makedirs("logs", exist_ok=True)  

logging.basicConfig(
    filename="logs/scheduler.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def run_pipeline():

    print("Running ETL Pipeline")

    run_etl()

    print("Calculating RFM")

    calculate_rfm()

    print("Generating Reports")

    generate_reports()

    print("Pipeline completed successfully")


if __name__ == "__main__":

    run_pipeline()


