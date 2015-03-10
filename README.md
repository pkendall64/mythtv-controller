# mythtv-controller

## Prerequisites

* npm
* bower `npm install -g bower)`
* vulcanize `npm install -g vulcanize`

## To get the project running

Run the following commands, assuming you have bower installed globally

```bash
git clone https://github.com/pkendall64/mythtv-controller
cd mythtv-controller
bower update
```

Now you can edit the file `app/mythconfig.json` enter the names/ip addresses of your backend and frontend systems.

start the server

```
python serve.py
```

Now open a browser to `http://localhost:8080/src/index.html`

Select the middle (recordings) button, then select the frontend to control from the menu chevron on the right.
Now you should get a list of recordings and be able to select one and play it on the selected frontend.

## Build to a single page

```
vulcanize -p . -s -o index.html src/index.html
```

Once you've built the application to a single you can copy `index.html` and the `src/mythconfig.json` to your deployment server.
