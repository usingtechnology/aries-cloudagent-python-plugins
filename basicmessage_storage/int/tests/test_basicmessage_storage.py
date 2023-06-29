"""Integration tests for Basic Message Storage."""

# pylint: disable=redefined-outer-name

import pytest
import requests
import time

from . import Agent, BOB, ALICE


@pytest.fixture(scope="session")
def bob():
    """bob agent fixture."""
    yield Agent(BOB)


@pytest.fixture(scope="session")
def alice():
    """resolver agent fixture."""
    yield Agent(ALICE)


@pytest.fixture(scope="session", autouse=True)
def established_connection(bob, alice):
    """Established connection filter."""
    invite = bob.create_invitation(auto_accept="true")["invitation"]
    resp = alice.receive_invite(invite, auto_accept="true")
    yield resp["connection_id"]



def test_storage(bob, alice, established_connection):
    # make sure connection is active...
    time.sleep(2)

    # alice send bob a message (alice will store their sent message)
    resp = alice.send_message(established_connection, "hello bob")
    assert True

    # make sure auto-respond messages have been exchanged
    time.sleep(2)

    # bob should have 1 received
    bob_messages = bob.retrieve_basicmessages()
    assert len(bob_messages["results"]) == 1

    # alice should have 1 sent and 1 received (auto-reponse)
    alice_messages = alice.retrieve_basicmessages()
    assert len(alice_messages["results"]) == 2
