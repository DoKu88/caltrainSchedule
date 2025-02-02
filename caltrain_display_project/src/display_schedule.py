import tkinter as tk
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class ScheduleDisplay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Caltrain Schedule")
        self.setup_window()

    def setup_window(self):
        """Configure the main window"""
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        
        # Press Escape to exit
        self.root.bind('<Escape>', lambda e: self.root.quit())

    def display_schedule(self, schedule_data):
        """Display the schedule data in a formatted way"""
        if not schedule_data:
            self._show_error_message()
            return

        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Add header
        current_time = datetime.now().strftime("%I:%M %p")
        header = tk.Label(
            self.root,
            text=f"Caltrain Schedule (Updated: {current_time})",
            font=('Helvetica', 24, 'bold'),
            fg='white',
            bg='black'
        )
        header.pack(pady=20)

        # Create frame for schedule
        schedule_frame = tk.Frame(self.root, bg='black')
        schedule_frame.pack(padx=50, pady=20, fill='both', expand=True)

        # Add column headers
        tk.Label(
            schedule_frame,
            text="Station",
            font=('Helvetica', 20, 'bold'),
            fg='white',
            bg='black'
        ).grid(row=0, column=0, padx=10, pady=5, sticky='w')

        tk.Label(
            schedule_frame,
            text="Next Departures",
            font=('Helvetica', 20, 'bold'),
            fg='white',
            bg='black'
        ).grid(row=0, column=1, padx=10, pady=5, sticky='w')

        # Add schedule data
        for i, entry in enumerate(schedule_data, 1):
            station = entry['station']
            times = ' | '.join(entry['times'][:5])  # Show only next 5 departures

            tk.Label(
                schedule_frame,
                text=station,
                font=('Helvetica', 16),
                fg='white',
                bg='black'
            ).grid(row=i, column=0, padx=10, pady=5, sticky='w')

            tk.Label(
                schedule_frame,
                text=times,
                font=('Helvetica', 16),
                fg='white',
                bg='black'
            ).grid(row=i, column=1, padx=10, pady=5, sticky='w')

    def _show_error_message(self):
        """Display error message when no schedule data is available"""
        error_label = tk.Label(
            self.root,
            text="Unable to load schedule data.\nPlease check your internet connection.",
            font=('Helvetica', 20),
            fg='red',
            bg='black'
        )
        error_label.pack(expand=True)

    def run(self):
        """Start the display loop"""
        self.root.mainloop() 