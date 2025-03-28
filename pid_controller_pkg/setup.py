from setuptools import find_packages, setup

package_name = 'pid_controller_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/launch.py']),
        ('share/' + package_name + '/config', ['config/parameters.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='drinkalotofwater',
    maintainer_email='drinkalotofwater@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
	    'pid_controller_node = pid_controller_pkg.pid_controller_node:main',
        ],
    },
)
