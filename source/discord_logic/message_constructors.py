"""Functions responsible for building bot responses.

These functions will almost always be run in asynchronous context, so make sure there are
no time-consuming operations in them, or that they are asynchronous as well.
"""
from server_time import TimesOfDay


def _get_time_based_greeting(time: TimesOfDay) -> str:
    """Return proper greeting based on the time of day given.

    Each greeting should be isolated and contain no following commas or periods.
    """
    match time.name:
        case "MORNING":
            return "Witam w ten przepiękny poranek"
        case "AFTERNOON":
            return "Dzień dobry"
        case "EVENING":
            return "Dobry wieczór"
        case "NIGHT":
            return "*zieeew* No cześć"
    return "Cześć"


def create_hello_response_based_on_time(user: str | None = None, time: TimesOfDay | None = None) -> str:
    """Return a greeting to the user depending on server's local time."""
    response = _get_time_based_greeting(time) if time else "Cześć"
    if user:
        response += f", {user}"

    sentence_ending = "!"
    if time and time.name == "NIGHT":
        sentence_ending = "."
    response += sentence_ending

    return response
