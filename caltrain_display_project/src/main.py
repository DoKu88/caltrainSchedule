import time
import logging
from fetch_caltrain_data import CaltrainDataFetcher
from parse_schedule import ScheduleParser
from display_schedule import ScheduleDisplay

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    # Initialize components
    fetcher = CaltrainDataFetcher()
    parser = ScheduleParser()
    display = ScheduleDisplay()

    def update_schedule():
        """Fetch and update the displayed schedule"""
        try:
            # Fetch new schedule data
            html_content = fetcher.fetch_schedule()
            
            # Parse the schedule
            schedule_data = parser.parse_html(html_content)
            
            # Update the display
            display.display_schedule(schedule_data)
            
            # Schedule the next update in 5 minutes
            display.root.after(300000, update_schedule)
            
        except Exception as e:
            logger.error(f"Error updating schedule: {e}")
            # Retry after 1 minute if there's an error
            display.root.after(60000, update_schedule)

    # Start the initial update
    update_schedule()
    
    # Run the display
    display.run()

if __name__ == "__main__":
    main() 