<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ryanbender2/a-gamers-script">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">A-Gamers-Script</h3>

  <p align="center">
    A downloader for all of a gamer's essential installers!
    <br />
    <a href="https://github.com/ryanbender2/a-gamers-script"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ryanbender2/a-gamers-script/issues">Report Bug</a>
    ·
    <a href="https://github.com/ryanbender2/a-gamers-script/issues">Request Feature</a>
    <br />
    <a href="https://github.com/ryanbender2/a-gamers-script/raw/main/AGamersScript.exe">Download!</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
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
      <a href="#building-and-running">Building and Running</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#prepare-environment">Prepare Environment</a></li>
        <li><a href="#build-exe">Build exe</a></li>
        <li><a href="#run-in-terminal">Run in terminal</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![AGamersScript][product-screenshot]](https://github.com/ryanbender2/a-gamers-script)

Are you an gamer? Do you find yourself frequently building new PC's or getting new laptops? Does it get annoying having to constantly go out and download all of those installers for all your devices and games? Well this is the app for you! Built with gamer's in mind, this app does one thing, and one thing only, download all those pesky installers. 

Here are the current installers the AGamersScript will go and get:
* [AfterBurner](https://www.msi.com/Landing/afterburner/graphics-cards)
* [Battle.net](https://www.blizzard.com/en-us/)
* [Discord](https://discord.com/)
* [Epic Games](https://www.epicgames.com/store/en-US/)
* [Geforce Experience](https://www.nvidia.com/en-us/geforce/geforce-experience/)
* [Steam](https://store.steampowered.com/)

If you want to suggest an installer to be added, please add a [feature request](https://github.com/ryanbender2/a-gamers-script/issues)!

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [ChromeDriver](https://chromedriver.chromium.org/home)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Building and Running

If you're a pythonista and want to play around with the code for the project, here's some docs to get you started.

### Prerequisites

Python is the only prerequisite you need!

* [Python](https://www.python.org/)

### Prepare environment

1. Create the virtual environment
   ```sh
   dev_create_env.bat
   ```
2. Use the environment
   ```sh
   ./env/Scripts/activate
   ```

### Build exe

1. Ensure you have and are using the virtual environment as described above
2. Run the build script
   ```sh
   ./build.bat
   ```
   This script will build the executable and place it in a dist directory.

### Run in terminal

1. Ensure you have and are using the virtual environment as described above
2. Run the `main.py` file
   ```sh
   python ./src/main.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add initial project
- [ ] Add GUI

See the [open issues](https://github.com/ryanbender2/a-gamers-script/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ryan Bender - [@itsmeryan.hihello](https://www.instagram.com/itsmeryan.hihello/) - ryan.bender.general@gmail.com

Project Link: [https://github.com/ryanbender2/a-gamers-script](https://github.com/ryanbender2/a-gamers-script)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [SergeyPirogov's Python Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
* [Freepik - Flaticon](https://www.flaticon.com/free-icons/installation)
* [othneildrew's README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ryanbender2/a-gamers-script.svg?style=for-the-badge
[contributors-url]: https://github.com/ryanbender2/a-gamers-script/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ryanbender2/a-gamers-script.svg?style=for-the-badge
[forks-url]: https://github.com/ryanbender2/a-gamers-script/network/members
[stars-shield]: https://img.shields.io/github/stars/ryanbender2/a-gamers-script.svg?style=for-the-badge
[stars-url]: https://github.com/ryanbender2/a-gamers-script/stargazers
[issues-shield]: https://img.shields.io/github/issues/ryanbender2/a-gamers-script.svg?style=for-the-badge
[issues-url]: https://github.com/ryanbender2/a-gamers-script/issues
[license-shield]: https://img.shields.io/github/license/ryanbender2/a-gamers-script.svg?style=for-the-badge
[license-url]: https://github.com/ryanbender2/a-gamers-script/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ryan-bender-20a5a8154/
[product-screenshot]: images/screenshot.png