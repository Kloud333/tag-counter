import click
from counter.app import run_get, run_view, show_all_aliases, remove_alias, add_alias, run_gui


@click.command()
@click.option('--get', '-g', help='get list of tags')
@click.option('--view', '-v', help='get data from db')
@click.option('--aliases', is_flag=True, help='show aliases')
@click.option('--removealias', '-r', help='remove alias')
@click.option('--addalias', '-a', nargs=2, help='add alias')
def main(get, view, aliases, removealias, addalias):
    if get is not None:
        run_get(get)
    elif view is not None:
        run_view(view)
    elif aliases:
        show_all_aliases()
    elif removealias is not None:
        remove_alias(removealias)
    elif addalias:
        add_alias(addalias)
    else:
        run_gui()


if __name__ == "__main__":
    main()
