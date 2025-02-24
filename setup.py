from setuptools import setup, find_packages

setup(
    name="rnn_smiles",
    version="0.1.0",
    description="Project to create a RNN from scratch using just math that outputs SMILES valid structures",
    author="Alejandro Flores",
    packages=find_packages(where="src"),  # This ensures it finds the modules inside "src"
    package_dir={"": "src"},  # This sets "src" as the root package directory
    install_requires=[
        "rdkit",
        "numpy", 
        "pandas",
        "matplotlib",
        "tqdm", 
        "pyarrow",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "mypy",
            "pytest-cov",
        ],
    },
    python_requires=">=3.9",
)