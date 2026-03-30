import schedule
import time
import logging
from src.rfm_segmentation import calculate_rfm
from src.etl_pipeline import run_etl
from src.report_generation import generate_reports

logging.basicConfig(
    filename="logs/scheduler.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def job():
    logging.info("Pipeline started")
    print("Pipeline started...")

    try:
        
        logging.info("Starting ETL Pipeline")
        print("Running ETL Pipeline...")
        run_etl()
        logging.info("ETL Pipeline completed successfully")

        
        logging.info("Starting RFM calculation job")
        print("Running RFM update...")
        calculate_rfm()
        logging.info("RFM calculation completed successfully")

        
        logging.info("Pipeline completed successfully")
        print("Pipeline completed successfully!")

        logging.info("Generating reports")
        generate_reports()

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(f"Error: {e}")


schedule.every().day.at("02:00").do(job)
logging.info("Scheduler started")
print("Scheduler started...")
job()
while True:
    schedule.run_pending()
    time.sleep(60)