from counter.console import Console
from counter.gui import Gui
from counter.services.aliases.aliases import Aliases

aliases = Aliases()


def show_all_aliases():
    aliases.show_aliases()


def remove_alias(alias):
    aliases.remove_alias(alias)


def add_alias(alias):
    aliases.add_alias(alias[0], alias[1])


def run_get(domain_name: str):
    Console(domain_name).console_view()


def run_view(domain_name: str):
    Console(domain_name).console_view_db()


def run_gui():
    Gui().gui_view()
