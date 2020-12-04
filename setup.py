from setuptools import setup, find_packages

setup(
    name='air_ticket',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ticket=cli.scripts.create_ticket:get_ticket
        read_ticket=cli.scripts.create_ticket:get_ticket_json
    ''',
)
