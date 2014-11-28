from setuptools import setup, find_packages

setup(
    name="tw2.jssor.slider",
    version="0.0",
    description="ToscaWidgets 2 wrapper for the jssor slider",
    author="Nils Philippsen",
    author_email="nils@tiptoe.de",
    #url=
    #download_url=
    install_requires=["tw2.core>=2.0", "tw2.jquery>=2.0"],
    packages=find_packages(),
    namespace_packages = ['tw2', 'tw2.jssor'],
    zip_safe=False,
    include_package_data=True,
    package_data = {
        'tw2.jssor.slider': [
            "static/*.txt",
            "static/js/jssor*.js",
            "static/img/[a-z][0-9][0-9].png",
            "static/img/close.png",
            "static/img/play.png",
            "static/img/loading.gif",
            "static/img/loading2.gif",
            "templates/*.py",
            "templates/*.html"
            ]
        },
    #test_suite="nose.collector"
    entry_points="""
        [tw2.widgets]
        widgets = tw2.jssor.slider
    """,
    keywords = ["tw2.widgets"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Environment :: Web Environment :: ToscaWidgets",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Widget Sets",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
