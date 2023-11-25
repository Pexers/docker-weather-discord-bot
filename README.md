# Weather Forecast Bot ⛅🤖
A Python-based [**Discord**](https://discord.com/) bot running on Docker to provide weather forecast information.

> <img src="https://user-images.githubusercontent.com/47757441/213523762-dee27ec8-d0c8-42cb-baef-0176e33f02f9.png" width="480">

### Setting up the Docker environment
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/). Alternatively, you can install the [Docker Engine](https://docs.docker.com/engine/install/).
2. Proceed to build the Docker image.
    ```sh
    $ docker build -t weather-forecast-bot:latest ./
    ```
3. Start a new container for the newly built image. Set the following runtime arguments:
    - `discord_token`: a valid token provided by the [Discord Developer Portal](https://discord.com/developers/docs/intro).
    ```sh
    $ docker run weather-forecast-bot:latest --discord_token=DISCORD_TOKEN
    ⋮
    WeatherBot#0000 is now running!
    ```
> <img src="https://github.com/Pexers/docker-weather-forecast-bot/assets/47757441/1c290328-a2ae-4d56-959b-6c0108cf072e" width="480">

## Discord commands
(Work in progress)
|Command|Description|
|---|---|
|`!weather/country/COUNTRY_NAME`|Provides the current temperature in `COUNTRY_NAME`, in degrees Celsius.|
|`!help`|Provides information on built-in commands.|

## References
- [Weather Forecast API](https://open-meteo.com/en/docs#api-documentation)
- [discord.py API](https://discordpy.readthedocs.io/en/stable/api.html)
