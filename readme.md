# memeinsider-dl
A script to download [Meme Insider](https://memeinsider.co/) issues

# Installation
    git clone https://github.com/flomk/memeinsider-dl $HOME/.memeinsider-dl
    echo PATH="$HOME/.memeinsider-dl:${PATH}" >> ~/.zshrc
    source ~/.zshrc

# Usage

    memeinsider-dl -h

                                      _            _     __                    ____
       ____ ___  ___  ____ ___  ___  (_)___  _____(_)___/ /__  _____      ____/ / /
      / __ `__ \/ _ \/ __ `__ \/ _ \/ / __ \/ ___/ / __  / _ \/ ___/_____/ __  / /
     / / / / / /  __/ / / / / /  __/ / / / (__  ) / /_/ /  __/ /  /_____/ /_/ / /
    /_/ /_/ /_/\___/_/ /_/ /_/\___/_/_/ /_/____/_/\__,_/\___/_/         \__,_/_/


    usage: memeinsider-dl [-h] [-i URL | -u | -l]

    Usage: memeinsider-dl [URL]

    optional arguments:
    -h, --help           show this help message and exit
    -i URL, --issue URL  url of issue to download
    -u, --upload         upload to cloud storage
    -l, --latest         get the latest issue


# TODO
- [x] Add option to download the latest issue
- [ ] Add option to upload to google drive
- [ ] Add option to upload to Dropbox
- [ ] Make the code less ugly
