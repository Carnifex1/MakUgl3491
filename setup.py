from setuptools import find_packages, setup

package_name = 'MakUgl'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='carnifex',
    maintainer_email='carnifex@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'even_number_publisher = MakUgl.even_number_publisher:main',
            'overflow_listener = MakUgl.overflow_listener:main',
        ],
    },
)
