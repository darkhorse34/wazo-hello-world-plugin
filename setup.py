from setuptools import setup, find_packages

setup(
    name="hello-calld",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["Flask"],
    entry_points={
        # This is how wazo-calld discovers plugins (via stevedore)
        "wazo_calld.plugins": [
            "hello_calld = hello_calld.plugin:Plugin",
        ],
    },
)
