from unittest.mock import patch, MagicMock
from weather import get_temperature, is_sunny, get_weather_data
from mock import mock_data

def test_get_temperature():

    with patch('weather.get_weather_data', return_value=mock_data):
        result = get_temperature("Lyon")

    assert result == 18

def test_is_sunny():
    mock_data = {'condition': 'sunny'}
    with patch('weather.get_weather_data', return_value=mock_data):
        assert is_sunny("Paris") is True

def test_is_sunny_false():
    with patch('weather.get_weather_data') as mock_func:
        mock_func.return_value = {'condition': 'cloudy'}
        assert is_sunny("Paris") is False



def test_get_weather_data():
    mock_response = MagicMock()
    mock_response.json.return_value = {"temperature": 25, "condition": "sunny"}

    with patch("weather.requests.get", return_value=mock_response) as mock_get:
        result = get_weather_data("Paris")

        
        mock_get.assert_called_with("http://api.weather.com/v1/weather?city=Paris")

        
        assert result == {"temperature": 25, "condition": "sunny"}
