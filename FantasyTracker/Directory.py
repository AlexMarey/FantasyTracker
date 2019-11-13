from pathlib import Path

class Directory():
    def __init__(self, week=0):
        if isinstance(week, int):
            self.week = week
        self.path = 'Rankings/'
        return

    def setWeek(self, week):
        if isinstance(week, int):
            if week > 0 and week < 18:
                self.week = week
            else: 
                raise ValueError("Week must be between 0 and 18")
        else:
            raise ValueError("setWeek only excepts integers.")

    def getFormattedWeek(self):
        return 'Week_{}'.format(self.week)

    def getFormattedPath(self):
        return '{}{}'.format(self.path, self.getFormattedWeek())

    def createRankingsDirectory(self):
        Path(self.path).mkdir(parents=True, exist_ok=True)
        
    def createWeeklyDirectory(self):
        Path(self.getFormattedPath()).mkdir(parents=True, exist_ok=True)

    # Creates weekly ranking directory if there needs to be one
    def createWeeklyRankingDirectories(self):
        self.createRankingsDirectory()
        self.createWeeklyDirectory()