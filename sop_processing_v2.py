#!/usr/bin/python3

# re is imported to use regex

import re

# class line() is created and defines position() and percent_identity()
# similar set-up to the regex used within the first and second script

class Line():
    def __init__(self, line):
        self.line = line


    def position(self):
        self.line = (self.line).strip()
        columns = re.split(r"\t", self.line)
        alignment_position_begin = (int(columns[9]) / 1000)
        return alignment_position_begin

    def percent_identity(self):
        self.line = (self.line).strip()
        columns = re.split(r"\t", self.line)
        percent_identity_columns = re.split("%", columns[7])
        percent_identity_value = float(percent_identity_columns[0])
        return percent_identity_value
