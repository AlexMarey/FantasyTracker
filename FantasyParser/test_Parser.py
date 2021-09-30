import pytest
from FantasyParser.Parser import Parser
from datetime import date


class TestFantasyParser():
    @pytest.fixture
    def baseParser(self):
        return Parser()

    def test_GetFileName_ShouldReturnFileName_GivenWeekAndPosition(self, baseParser):
        week = 1
        position = "RB"
        currentYear = date.today()
        currentYear = currentYear.year

        expectedFileName = f"FantasyPros_{str(currentYear)}_Week_{str(week)}_{position}_Rankings.csv"

        result = baseParser.GetFileName(week, position)

        assert result == expectedFileName
