import setuptools

setuptools.setup(name='diagram_api',
                 version='0.0.1',
                 author = 'Patrick Morton',
                 author_email = 'jarhead8795@gmail.com',
                 description = 'Generate flowchart mermaid markdown from weather data.',
                 packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent",
                ],
                python_requires='>=3.0'                         
)