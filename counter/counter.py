import click
from counter.app_runner import run_get, run_view, run_get_from_db


@click.command()
@click.option('--get', '-g', help='get list of tags')
@click.option('--view', '-v', is_flag=True, help='get list of tag from db')
def main(get, view):
    if get is not None:
        run_get(get)
    elif view is not None:
        run_get_from_db(view)
    else:
        run_view()


if __name__ == "__main__":
    main()
