from datetime import date
import json


class Parser():
    POSITIONS = ['QB', 'RB', 'WR', 'FLEX', 'K', 'DEF']

    def _get_filename(self, position):
        current_year = date.today()
        current_year = current_year.year

        week = self._get_current_week()

        return f"FantasyPros_{str(current_year)}_Week_{str(week)}_{position}_Rankings.csv"

    def _get_current_nfl_year(self):
        current_date = date.today()
        current_month = current_date.month
        current_year = current_date.year

        if current_month == 'January':
            return current_year - 1

        return current_year

    def _get_current_week(self):
        nfl_year = self._get_current_nfl_year()
        filename = f'nfl_weeks_by_year/{nfl_year}.json'

        with open(filename) as f:
            data = json.load(f)

        current_date = date.today()
        year = current_date.year

        week_found = False
        week_number = 0
        while not week_found:
            week_number += 1

            week_data = data['week'][str(week_number)]
            beginning = date(
                year, week_data['beginningMonth'], week_data['firstDay'])
            end = date(
                year, week_data['endMonth'], week_data['lastDay'])
            if beginning <= current_date <= end:
                week_found = True
            elif week_number == 18:
                week_number = None
        return week_number

    def get_player_data(self):
        for pos in self.POSITIONS:
            filename = self._get_filename(pos)

        return
