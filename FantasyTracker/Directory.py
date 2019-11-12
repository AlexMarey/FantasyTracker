from pathlib import Path

class Directory():
    def __init__(self, week=0):
        if isinstance(week, int):
            self.week = week
        else:
            self.week = -1
        self.path = 'Rankings/'
        return

    def setWeek(self, week):
        self.week = week
    
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