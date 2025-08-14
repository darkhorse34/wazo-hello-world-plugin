from setuptools import setup, find_packages

setup(
    name="wazo-hello-calld",
    version="0.1.0",
    description="Minimal Hello World plugin for wazo-calld",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Flask>=2.0.0"],
    entry_points={
        # This is how wazo-calld discovers stack plugins
        "wazo_calld.plugins": [
            "hello_calld = hello_calld.plugin:Plugin",
        ],
    },
)
