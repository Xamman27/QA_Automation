from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture
def config_browser():
    browser.config.window_height = 1024
    browser.config.window_width = 768
    return browser


def test_google_positive(config_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_negative(config_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('agadfgvadfgertherth').press_enter()
    browser.element('.card-section').should(have.text('По запросу agadfgvadfgertherth ничего не найдено.'))
