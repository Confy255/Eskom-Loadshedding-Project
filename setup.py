from setuptools import setup, find_packages

setup(
    name='ourmodule',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Analyse Predict Package',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/Confy255/group3predict',
    author='<Confidence Ledwaba, Evans Morema, Karabo Leso, Sandile Dladla, Sandile Mkhize>',
    author_email='<confidenceledwaba@gmail.com, karabopleso@gmail.com, kenmarema@gmail.com, sdladlad@gmail.com, mkizesandile@yahoo.com>'
)