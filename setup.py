from setuptools import setup, find_packages

setup(
    name='StockStreamSim',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'websockets',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'stock-stream-sim=stock_stream_sim.main:main',
        ],
    },
)
