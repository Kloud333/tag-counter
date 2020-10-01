from counter.console import console_view
from counter.gui import gui_view
from counter.services.aliases.aliases import Aliases

aliases = Aliases()


def show_all_aliases():
    aliases.show_aliases()


def remove_alias(alias):
    aliases.remove_alias(alias)


def add_alias(alias):
    aliases.add_alias(alias[0], alias[1])


def run_get(domain_name: str):
    console_view(domain_name)


def run_view():
    gui_view()
