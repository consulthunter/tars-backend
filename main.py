
import os
import uvicorn
from tars.services.configuration.configuration import Configuration
from tars.services.logger.logger import Logger
from datetime import datetime

# get the run time
runtime = datetime.now()

# Format the date and time
current_day = runtime.strftime("%Y-%m-%d")

def start_api():
    """start the api"""
    print("Starting FastAPI app...")
    uvicorn.run("tars.api.api:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    # create the config
    create_config_logger = Logger("logs", current_day, "create-config")
    Configuration.create_default_config(
        os.path.join("config", "default_config.json"),
        create_config_logger
    )

    # start the API
    start_api()