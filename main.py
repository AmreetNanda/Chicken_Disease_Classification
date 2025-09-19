from chicken_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

if __name__ == "__main__":
    try:
        print(">>> Stage 01: Data Ingestion started <<<")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        print(">>> Stage 01: Data Ingestion completed <<<")
    except Exception as e:
        raise e
