import requests
import sys
from html.entities import html5 as html5Entities

from html.parser import HTMLParser
from py_w3c.validators.html.validator import HTMLValidator


class Requirement():

    def __init__(self, unsatisfied_message):
        self.unsatisfied_message = unsatisfied_message
        self.satisfied_messages = []

    def add_success(self, msg):
        self.satisfied_messages.append('✅  ' + msg)

    def is_satisfied(self):
        return len(self.satisfied_messages) > 0

    def get_satisfied_message(self):
        satisfied_message = ''
        for msg in self.satisfied_messages:
            satisfied_message += (msg + '\n')
        return satisfied_message

    def get_unsatisfied_message(self):
        return '❌  ' + self.unsatisfied_message

    def get_report(self):
        if not self.is_satisfied():
            return self.get_unsatisfied_message()
        else:
            return self.get_satisfied_message()


class SetRequirement(Requirement):

    used_items = []

    def __init__(self, unsatisfied_message, required_items):
        super().__init__(unsatisfied_message)
        self.required_items = required_items

    def used_item(self, name):
        if name in self.required_items and name not in self.used_items:
            self.used_items.append(name)
            self.add_success('Used tag: ' + name)

    def is_satisfied(self):
        return len(self.required_items) == len(self.used_items)

    def get_unsatisfied_message(self):

        if self.is_satisfied():
            return ''

        message = self.unsatisfied_message + '\nNot Found: '
        unused_items = list(set(self.required_items) - set(self.used_items))
        message += ', '.join(unused_items)
        return message


class W3CValidityRequirement(Requirement):

    def __init__(self, html):
        super().__init__('Validation errors found')
        self.html = html
        self.validate()

    def validate(self):
        validator = HTMLValidator()
        validator.validate_fragment(self.html)
        self.errors = validator.errors
        self.warnings = validator.warnings
        self.is_valid = bool(len(self.errors))
        if self.is_valid:
            self.add_success('Valid HTML document found')

    def is_satisfied(self):
        return self.is_valid

    def get_unsatisfied_message(self):
        message = self.unsatisfied_message + '\n'

        if len(self.errors):
            message += '------ERRORS------\n'

        for error in self.errors:
            message += error['message'] + '\n'

        if len(self.warnings):
            message += '-----WARNINGS-----\n'

        for warning in self.warnings:
            message += warning['messages'] + '\n'

        return message


class HTMLMeSomethingParser(HTMLParser):

    required_tags = ['html', 'head', 'title', 'body', 'p', 'header', 'footer',
                     'main', 'article', 'img']

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tag_requirement = SetRequirement('Required HTML tags not found',
                                              self.required_tags)
        self.entity_requirement = Requirement('No valid HTML entities found')

    def feed(self, data):
        self.w3c_validity_requirement = W3CValidityRequirement(url)
        super().feed(data)
        self.report()

    def used_entity(self, name):
        if name in html5Entities:
            self.entity_requirement.add_success('Used entity: ' + name)

    def handle_entityref(self, name):
        self.used_entity(name)

    def handle_charref(self, name):
        self.used_entity(name)

    def handle_starttag(self, tag, attrs):
        self.tag_requirement.used_item(tag)

    def handle_startendtag(self, tag, attrs):
        self.tag_requirement.used_item(tag)

    def report(self):
        report_str = """******* HTML Me Something Grade Report *******

{validity_report}

{tag_report}

{entity_report}
"""
        print(report_str.format(
            validity_report=self.w3c_validity_requirement.get_report(),
            entity_report=self.entity_requirement.get_report(),
            tag_report=self.tag_requirement.get_report()))


if __name__ == '__main__':

    url = sys.argv[1]
    response = requests.get(url)
    html = response.text
    parser = HTMLMeSomethingParser()
    parser.feed(html)
