#!/usr/bin/env python3
"""Observer pattern example."""

from __future__ import annotations
from typing import Protocol


class Observer(Protocol):
    """Define the observer interface."""

    def update(self, topic: str, data: str) -> None:
        """Handle a notification."""
        ...


class NewsSubject:
    """Manage observers and publish news events."""

    def __init__(self) -> None:
        """Initialize the subscribers."""
        self._subs: dict[Observer, set[str] | None] = {}

    def subscribe(
        self,
        observer: Observer,
        topics: set[str] | None = None,
    ) -> None:
        """Subscribe an observer to selected topics."""
        if observer in self._subs:
            return
        self._subs[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        """Unsubscribe an observer."""
        self._subs.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        """Notify observers interested in the topic."""
        for observer, interests in list(self._subs.items()):
            if interests is not None and topic not in interests:
                continue
            observer.update(topic, data)


class LogObserver:
    """Log news events."""

    def update(self, topic: str, data: str) -> None:
        """Print a log notification."""
        print(f"log:{topic}={data}")


class EmailObserver:
    """Send email notifications."""

    def update(self, topic: str, data: str) -> None:
        """Print an email notification."""
        print(f"email:{topic}={data}")


class SmsObserver:
    """Send SMS notifications."""

    def update(self, topic: str, data: str) -> None:
        """Print an SMS notification."""
        print(f"sms:{topic}={data}")


def main() -> None:
    """Run the observer example."""
    subject = NewsSubject()

    log = LogObserver()
    email = EmailObserver()
    sms = SmsObserver()

    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email)
    subject.subscribe(sms, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
