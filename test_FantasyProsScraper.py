import pytest

from FantasyProsScraper import FantasyProsScraper


class TestFantasyProsScraper:
    def test_init_ShouldReturnFantasyProsScraperWithListOfPositions(self):
        fpsScraper = FantasyProsScraper()
        assert fpsScraper.positions == ["qb", "rb", "wr", "te", "k", "flex"]

    def test_makeUrl_ShouldRetrunUrlString(self):
        fpsScraper = FantasyProsScraper()
        purpose = 'purp'
        position = 'rb'
        expectedResult = 'https://www.fantasypros.com/nfl/{0}/{1}.php'.format(
            purpose, position)
        result = fpsScraper.makeUrl(purpose, position)
        assert result == expectedResult

    def test_makeUrl_ShouldReturnUrlWithScoring_WhenScoringIsNonStandard(self):
        fpsScraper = FantasyProsScraper()
        purpose = 'purp'
        position = 'rb'
        scoring = 'half-score'
        expectedResult = 'https://www.fantasypros.com/nfl/{0}/{1}-{2}.php'.format(
            purpose, scoring, position)
        result = fpsScraper.makeUrl(purpose, position, scoring)
        assert result == expectedResult

    def test_makeUrl_ShouldReturnStandardUrl_WhenScoringIsNonStandardAndPosIsQB(self):
        fpsScraper = FantasyProsScraper()
        purpose = 'purp'
        position = 'qb'
        scoring = 'half-score'
        expectedResult = 'https://www.fantasypros.com/nfl/{0}/{1}.php'.format(
            purpose, position)
        result = fpsScraper.makeUrl(purpose, position, scoring)
        assert result == expectedResult
