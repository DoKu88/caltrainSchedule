from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

class ScheduleParser:
    def __init__(self):
        self.stations = []
        self.schedule = {}

    def parse_html(self, html_content):
        """Parse the HTML content and extract schedule information"""
        if not html_content:
            logger.error("No HTML content to parse")
            return None

        try:
            soup = BeautifulSoup(html_content, 'lxml')
            
            # This is a simplified example - you'll need to adjust the selectors
            # based on the actual HTML structure of the Caltrain website
            schedule_table = soup.find('table', {'class': 'schedule-table'})
            
            if not schedule_table:
                logger.warning("No schedule table found in HTML")
                return None

            schedule_data = []
            
            # Parse table rows
            for row in schedule_table.find_all('tr')[1:]:  # Skip header row
                cells = row.find_all('td')
                if cells:
                    station = cells[0].get_text(strip=True)
                    times = [cell.get_text(strip=True) for cell in cells[1:]]
                    schedule_data.append({
                        'station': station,
                        'times': times
                    })

            return schedule_data

        except Exception as e:
            logger.error(f"Error parsing schedule: {e}")
            return None 