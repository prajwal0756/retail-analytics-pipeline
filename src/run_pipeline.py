from etl_pipeline import run_etl
from rfm_segmentation import calculate_rfm
from report_generation import generate_reports


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


import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO
)