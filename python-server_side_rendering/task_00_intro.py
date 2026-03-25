#!/usr/bin/python3
import logging

logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):

    if not isinstance(template, str):
        logging.error("Template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Attendees must be a list of dictionaries")
        return

    if template.strip() == "":
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("Attendees list is empty, no output files generated.")
        return
        