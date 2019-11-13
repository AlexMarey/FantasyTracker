from pathlib import Path

class Directory():
    def __init__(self, week=0):
        if isinstance(week, int):
            self.week = week
        self.path = 'Rankings/'
        return

    def setWeek(self, week):
        if isinstance(week, int):
            if week < 0 or week > 17:
                self.week = -1
            else: 
                self.week = 9
        else:
            raise ValueError("setWeek only excepts integers.")

    
    def formatWeek(self):
        return 'Week_{}'.format(self.week)

    def formatPath(self):
        return '{}{}/'.format(self.path, self.formatWeek())

    def createRankingsDirectory(self):
        Path(self.path).mkdir(parents=True, exist_ok=True)
        
    def createWeeklyDirectory(self):
        Path(self.formatPath()).mkdir(parents=True, exist_ok=True)

    # Creates weekly ranking directory if there needs to be one
    def createWeeklyRankingDirectories(self):
        self.createRankingsDirectory()
        self.createWeeklyDirectory()