import unittest
import os
import sys

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from caltrain_display_project.src.fetch_caltrain_data import CaltrainDataFetcher
from caltrain_display_project.src.parse_schedule import ScheduleParser
from caltrain_display_project.src.display_schedule import ScheduleDisplay

class TestCaltrainDisplay(unittest.TestCase):
    def setUp(self):
        self.fetcher = CaltrainDataFetcher()
        self.parser = ScheduleParser()
        
    def test_fetch_schedule(self):
        """Test if we can fetch data from Caltrain website"""
        html_content = self.fetcher.fetch_schedule()
        self.assertIsNotNone(html_content)
        self.assertIsInstance(html_content, str)
        
    def test_parse_schedule(self):
        """Test parsing with a sample HTML content"""
        sample_html = """
        <table class="schedule-table">
            <tr><th>Station</th><th>Time 1</th><th>Time 2</th></tr>
            <tr><td>San Francisco</td><td>9:00 AM</td><td>10:00 AM</td></tr>
            <tr><td>Palo Alto</td><td>9:45 AM</td><td>10:45 AM</td></tr>
        </table>
        """
        schedule_data = self.parser.parse_html(sample_html)
        self.assertIsNotNone(schedule_data)
        self.assertEqual(len(schedule_data), 2)  # Two stations
        self.assertEqual(schedule_data[0]['station'], 'San Francisco')
        
    def test_display_creation(self):
        """Test if display can be created (will need manual verification)"""
        try:
            display = ScheduleDisplay()
            sample_data = [
                {'station': 'San Francisco', 'times': ['9:00 AM', '10:00 AM']},
                {'station': 'Palo Alto', 'times': ['9:45 AM', '10:45 AM']}
            ]
            display.display_schedule(sample_data)
            display.root.after(3000, display.root.quit)  # Close after 3 seconds
            display.run()
            self.assertTrue(True)  # If we get here, display worked
        except Exception as e:
            self.fail(f"Display creation failed: {e}")

if __name__ == '__main__':
    unittest.main() 