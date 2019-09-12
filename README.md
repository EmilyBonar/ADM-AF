# Aerosol Deposition Machine

This project controls a system designed to deposite aerosolized particles in specified patterns. The system consists of one or more feeders to aerosolize the powder(s), mass flow controllers to manage the speed of gas flow, pressure gauges to ensure the system is under vacuum, and a 3-axis stage.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Before using the program MGI Library, MGI Panel Manager, and OpenG Toolkit must be installed using VI Package Manager, which comes installed alongside LabVIEW. 

### Installing

To use this code in a development environment, download it here and open ADM.lvproj in LabVIEW 2018 or later. The program is started by running the VI named Splash Screen in the top level of the project explorer. Your hardware ports can be specified in the Physical Channels cluster in the Debug tab and they will be saved in a configuration file for later use.   

## Deployment

Open the project in the LabVIEW development environment and under Build Specifications, right click Aerosol Deposition Machine and select Build. An executable will be generated at:

```
<Project Folder>\builds\Aerosol Deposition Machine
```

## Built With

* [Actor Framework](https://labviewwiki.org/wiki/Actor_Framework) - The framework used
* [MGI Library](https://www.mooregoodideas.com/products/library/index.html) - Helpful tools
* [MGI Panel Manager](https://www.mooregoodideas.com/products/panel-manager/index.html) - Used to insert subpanels into front panel
* [OpenG Toolkit](https://sourceforge.net/projects/opengtoolkit/) - Helpful tools

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Source Control

We use [SourceTree](https://www.sourcetreeapp.com/) and [vicompare](https://github.com/smithed/vicompare) for version control.

## Authors

* **Michael Bonar** - *Initial work* - [PurpleBooth](https://github.com/michaelbonar)

See also the list of [contributors](https://github.com/michaelbonar/ADM-AF/graphs/contributors) who participated in this project.