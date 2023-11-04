# AB Tech Website
The website for the Carnegie Mellon Activities Board Technical Committee

## Issues
We all have them.

## Development
### Lazy
 - Push changes to `dev` and wait for GitHub to build and upload the built artifact (keeps for 90 days, re-run build to get it again)
 - Once changes are confimed OK, merge with `master` and it will build again and also push to `gh-pages`

Note: We do not host the production website with GitHub Pages, but it is a convenient place to keep the latest built version from `master`. It also provides emergency fallback hosting should it ever be needed.
### Simple (well, needs much more clarification)
 - Run the Docker container: ``docker run --rm -it --publish 4000:4000 -v `pwd`:/usr/src/app ghcr.io/abtech/abtech.org:dev bash``
 - `npm install --unsafe-perm` (will install Ruby and NodeJS dependencies, `--unsafe-perm` since you are probably `root` in the container)
 - `npm run-script serve` (for live development)
 - `npm run-script build-prod` (for built app placed in `_site`)
### Complicated
 - Use the Ruby version found in the Dockerfile or `.ruby-version` (for consistency). It is recommended to use rbenv and run `rbenv install`
 - Install the gems with `bundle install`.
 - Use the NodeJS version found in the Dockerfile (for consistency) and run `npm install`.
 - Continue with instructions from [Simple](#Simple) after the Docker and NPM install commands.

## Tips & Instructions
### Adding plugins
1. Add to `_config.yaml`
2. Add to `Gemfile`
3. Run `bundler update`

## Adding non-built files to root of repo
Files added to the root of the repo will automatically be built. Remove them by adding them to the `exclude` list in `_config.yaml`

## Adding JS libraries
Ensure JS libraries are browser-ready (no dependencies once built, usually found in a `dist` folder).

1. Install with `npm install --save <package>`
2. Add `node_modules/<package>` to the `include` list in `_config.yaml`

## Adding CSS/SCSS/SASS libraries

1. Install with `npm install --save <package>`
2. You should now be able to include them from within the `_sass` directory (example with how Bootstrap is included)

### Setup
Clone this repo into your workspace.
More info coming soon

### Running
It's a static website. Throw it on any web server (Apache, Nginx, etc.). Set the 404 page to `/404.html`.

## Contribute
Just send a pull request! Please contribute to the `dev` branch.

### Maintenance
Code hosted at www-01.abtech.org:/srv/abtech.org

To load changes from server, simply pull (from `gh-pages` once it is built):
```
git pull
```

## History
This website was refreshed by pnaseck in 2021 to use Jekyll. It was previously a Django site, which can be found in the `legacy-pre-2021` branch.
