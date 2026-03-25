#!/usr/bin/python3
"""Module that generates invitation files based on a template and a list of attendees."""
def generate_invitations(template, attendees):

    if not isinstance(template, str):
        raise TypeError("Template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        raise TypeError("Attendees must be a list of dictionaries")
        return

    if template.strip() == "":
        raise ValueError("Template is empty, no output files generated.")
        return

    if not attendees:
        raise ValueError("Attendees list is empty, no output files generated.")
        return

    fields = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, start=1):
        output = template

        for field in fields:
            value = attendee.get(field)

            if value is None:
                value = "N/A"

            output = output.replace("{" + field + "}", str(value))

        # Write to file
        filename = "output_{}.txt".format(i)
        try:
            with open(filename, "w") as f:
                f.write(output)
        except Exception as e:
            logging.error(f"Error writing file {filename}: {e}")
