import setuptools

setuptools.setup(name='diagram_api_assignment',
                 version='0.0.4',
                 author = 'Patrick Morton',
                 author_email = 'jarhead8795@gmail.com',
                 description = 'Generate flowchart mermaid markdown from weather data.',
                 long_description='Generate flowchart mermaid markdown from weather data.',
                 package_dir={"": "src"},
                 packages=setuptools.find_packages(where="src"),
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent",
                ],
                python_requires='>=3.0'                         
)