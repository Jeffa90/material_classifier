from setuptools import setup, find_packages

setup(
    name="material_classifier",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "joblib"
    ],
    include_package_data=True,
)
