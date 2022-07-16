<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Lopinosaurus/FloppyRecorder">
    <img src="logo.png" alt="Logo" width="160" height=160">
  </a>

  <h3 align="center">FloppyRecorder Discord Bot</h3>

  <p align="center">
    A Discord bot to centralize all of your logs in different servers into one and unique channel !
    <br />
    <br />
    <a href="https://github.com/Lopinosaurus/FloppyRecorder/issues">Report Bug</a>
    ·
    <a href="https://github.com/Lopinosaurus/FloppyRecorder/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

FloppyRecorder is a Discord Bot allowing you to centralize your multiple server logs on a unique channel. Thanks to this, you will be able to manage all of your communities in a better and easier way, as the bot record a lot of server and member actions.




### Built With

Here are the tools I used to build FloppyRecorder.

* [Python3](https://www.python.org/download/releases/3.0/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [Discord.py](https://discordpy.readthedocs.io/en/stable/)



## Getting Started

First, clone this repository by running into your Shell or Git Bash : 

```
git clone git@github.com:Lopinosaurus/FloppyRecorder.git
```
You can now install the requirements for python by running : 
```
python3 -m pip install -r requirements.txt
```
in your terminal.   

You can now setup your bot by modifying the `.env` file : 
The `TOKEN` field should be filled with your bot's token.
The `LOG` field should be filled with the channel ID of your log channel (where the bot is supposed to write the logs).
The `ADMIN` field should be filled with the ID of the administrator role on the log server (where the log channel is located).

Now you should be able to start the bot by running in your shell : 
```
python3 main.py
```
or
```
py -3 main.py
```
on Windows systems.


<!-- CONTRIBUTING -->
## Contributing

Contributing to this project would be greatly appreciated. To help FloppyRecorder to get better, follow this steps : 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.




<!-- CONTACT -->
## Contact

Discord : Lopinosaurus#0404


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
                                
Credits to : 

* [Choose an Open Source License](https://choosealicense.com)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
