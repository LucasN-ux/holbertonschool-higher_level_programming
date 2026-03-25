#!/usr/bin/python3
"""Module that generates invitation files based on a template and a list of attendees."""
import os


def generate_invitations(template_content, attendees):
    if not template_content:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    if not isinstance(template_content, str):
        print("Invalid input type for template_content. Expected a string.")
        return

    if not isinstance(attendees, list):
        print("Invalid input type for attendees. Expected a list.")
        return
    try:
        for attendee in attendees:
            if not isinstance(attendee, dict):
                print("Invalid input type for attendee. Expected a dictionary.")
                return

            name = attendee.get("name", "N/A")
            event_title = attendee.get("event_title", "N/A")
            event_date = attendee.get("event_date", "N/A")
            event_location = attendee.get("event_location", "N/A")

            # Replace placeholders in the template
            invitation = template_content.replace("{name}", name or "N/A")
            invitation = invitation.replace("{event_title}", event_title or "N/A")
            invitation = invitation.replace("{event_date}", event_date or "N/A")
            invitation = invitation.replace("{event_location}", event_location or "N/A")

            output_filename = f"output_{attendees.index(attendee) + 1}.txt"
            if os.path.exists(output_filename):
                print(f"File {output_filename} already exists.")
            else:
                with open(output_filename, 'w') as output_file:
                    output_file.write(invitation)
    except Exception as e:
        print(f"Error writing to file {output_filename}: {e}")