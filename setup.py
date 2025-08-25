from setuptools import setup, find_packages

setup(
    name="description-from-memo",
    version="0.1.0",
    description="MkDocs plugin: use .memo file as description",
    packages=find_packages(),
    install_requires=["mkdocs"],
    entry_points={
        "mkdocs.plugins": [
            "description_from_memo = plugins.description_from_memo:Plugin"
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
