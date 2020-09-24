import click
from counter.app_runner import run_get, run_view


@click.command()
@click.option('--get', '-g', help='get list of tags')
def main(get):
    if get is not None:
        run_get(get)
    else:
        run_view()


if __name__ == "__main__":
    main()
