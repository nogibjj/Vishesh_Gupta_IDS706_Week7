from setuptools import setup, find_packages

setup(
    name="VisheshGuptaPipeline",
    version="0.1.0",
    description="ETLpipline",
    author="VisheshGupta",
    author_email="vg157@duke.edu",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        'console_scripts': [
            'etl_query=python_main:main',
        ],
    },
)
