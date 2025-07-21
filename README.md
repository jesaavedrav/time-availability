# Time Availability Heatmap

## Problem Statement
Coordinating the best time for a group of players to play together can be challenging, especially when everyone has different schedules and possibly different time zones. This script helps solve that problem by allowing each player to create their own worksheet in a shared Google Sheet, marking their available time slots. The script then automatically analyzes all worksheets and generates heatmaps to visualize the most popular time slots and the best times to play (with at least 3 players available).

**How it works:**
- Each player creates a worksheet (tab) in the shared Google Sheet, using their name as the worksheet name.
- Each player marks their availability with an 'X' in the corresponding time slots and days.
- The script aggregates all the data and produces visual heatmaps to easily identify the best times for everyone to play together.

## Google Sheet Structure
Your Google Sheet must have the following structure in **each worksheet**:

|        | A                  | B      | C        | D         | E      | F      | G      | H      |
|--------|--------------------|--------|----------|-----------|--------|--------|--------|--------|
| **1**  | (empty)            | LUNES  | MARTES   | MIÉRCOLES | JUEVES | VIERNES| SÁBADO | DOMINGO|
| **2**  | 00:00:00 - 01:00:00|        |          |           |        |        |        |        |
| **3**  | 01:00:00 - 02:00:00|        |          |           |        |        |        |        |
| ...    | ...                | ...    | ...      | ...       | ...    | ...    | ...    | ...    |
| **25** | 23:00:00 - 00:00:00|        |          |           |        |        |        |        |

- **Column A**: Time slots (one-hour intervals, 24 rows from 00:00 to 00:00)
- **Columns B-H**: Days of the week (in Spanish: LUNES, MARTES, MIÉRCOLES, JUEVES, VIERNES, SÁBADO, DOMINGO)
- **Mark an 'X'** in the cell if you are available at that time and day.
- Each worksheet should represent a different participant (use their name as the worksheet name).

## How to Use

1. **Clone or download this repository.**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Google Cloud Setup:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a project and enable both the **Google Sheets API** and **Google Drive API**.
   - Create a Service Account credential and download the JSON file.
   - Share your Google Sheet with the service account email (found in the JSON file).

4. **Configure the script:**
   - Set the path to your credentials JSON and the name of your Google Sheet at the top of `calculate_heatmap.py`.

5. **Run the script:**
   ```bash
   python calculate_heatmap.py
   ```

6. **Output:**
   - The script will generate heatmaps showing the most popular time slots and the best time to play (at least 3 participants available).
   - Images will be saved as `heatmap.png` and `best_time_to_play.png`.

## Notes
- All worksheet tabs must have the same structure.
- The script is written in Spanish but the README and output images are in English.
- For any issues, please open an issue or contact the maintainer. 

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this code for any purpose, including commercial and non-commercial use, provided that the original copyright and license notice are included.

See the LICENSE file for more details. 

