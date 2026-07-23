from unittest.mock import patch
from fetch import fetch_recalls


def test_fetch_recalls_parses_results():
    """fetch_recalls returns the results list from the API response."""
    fake_response_data = {
        "Count": 1,
        "results": [
            {"NHTSACampaignNumber": "TEST123", "Make": "ACURA", "Model": "RDX"}
        ],
    }

    with patch("fetch.requests.get") as mock_get:
        mock_get.return_value.json.return_value = fake_response_data
        mock_get.return_value.raise_for_status.return_value = None

        result = fetch_recalls("acura", "rdx", 2012)

    assert len(result) == 1
    assert result[0]["NHTSACampaignNumber"] == "TEST123"
    