# Reorganizes all files within directory and subdirectories of path passed as only argument.
# Reorganized into subdirectories according to year, month, and day of file creation.

from pathlib import Path
from time import sleep
import os
import time
import datetime
import shutil
import sys

months = {
        1:  'January',
        2:  'February',
        3:  'March',
        4:  'April',
        5:  'May',
        6:  'June',
        7:  'July',
        8:  'August',
        9:  'September',
        10: 'October',
        11: 'November',
        12: 'December',
}

def organize(source: Path):
    for item in source.iterdir():
        # if a directory
        if item.is_dir():
            organize(item)
            # Delete Directory
            os.rmdir(item)
        # if not a directory
        if item.is_file():
            stat = os.stat(item)
            file_timestamp = stat.st_birthtime
            file_datetime = datetime.datetime.fromtimestamp(file_timestamp)
            file_date = file_datetime.date()
            file_dest_year_path = Path(os.path.join(directory_to_organize, str(file_date.year)))
            file_dest_month_path = Path(os.path.join(file_dest_year_path, str(months.get(file_date.month))))
            file_dest_day_path = Path(os.path.join(file_dest_month_path, str(file_date.day)))
            if not file_dest_year_path.is_dir():
                # Make Year Directory
                os.makedirs(file_dest_year_path)
            if not file_dest_month_path.is_dir():
                # Make Month Directory
                os.makedirs(file_dest_month_path)
            if not file_dest_day_path.is_dir():
                # Make Day Directory
                os.makedirs(file_dest_day_path)
            shutil.move(src=item, dst=file_dest_day_path)


if __name__ == '__main__':
    directory_to_organize = sys.argv[1]
    organize(Path(directory_to_organize))
