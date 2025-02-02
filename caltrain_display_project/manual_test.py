from src.fetch_caltrain_data import CaltrainDataFetcher
from src.parse_schedule import ScheduleParser
from src.display_schedule import ScheduleDisplay

def test_full_flow():
    # Initialize components
    fetcher = CaltrainDataFetcher()
    parser = ScheduleParser()
    display = ScheduleDisplay()

    # Fetch data
    print("Fetching schedule data...")
    html_content = fetcher.fetch_schedule()
    
    if html_content:
        print("Successfully fetched HTML content")
        
        # Parse data
        print("Parsing schedule data...")
        schedule_data = parser.parse_html(html_content)
        
        if schedule_data:
            print(f"Found {len(schedule_data)} schedule entries")
            
            # Display for 10 seconds
            print("Displaying schedule (will close after 10 seconds)...")
            display.display_schedule(schedule_data)
            display.root.after(10000, display.root.quit)
            display.run()
        else:
            print("Failed to parse schedule data")
    else:
        print("Failed to fetch schedule data")

if __name__ == "__main__":
    test_full_flow() 