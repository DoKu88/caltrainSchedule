import requests
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CaltrainDataFetcher:
    def __init__(self):
        self.base_url = "https://www.caltrain.com"
        # Note: You'll need to update these URLs based on actual Caltrain website structure
        self.schedule_urls = {
            'weekday': f"{self.base_url}/schedules",
            'weekend': f"{self.base_url}/schedules",
        }

    def get_schedule_url(self):
        """Determine which schedule URL to use based on current day"""
        current_day = datetime.now().weekday()
        return self.schedule_urls['weekday'] if current_day < 5 else self.schedule_urls['weekend']

    def fetch_schedule(self):
        """Fetch the HTML content of the schedule page"""
        try:
            url = self.get_schedule_url()
            logger.info(f"Fetching schedule from: {url}")
            
            response = requests.get(url)
            response.raise_for_status()
            
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching schedule: {e}")
            return None 