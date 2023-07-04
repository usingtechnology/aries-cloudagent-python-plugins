### developer notes

- Open devcontainer in VS Code
- Python 3.9 and all dependencies will be loaded
- Poetry will be loaded and configured
- Docker and Docker Compose will be available

IMPORTANT: docker-in-docker can be a little flaky, so if you encounter a messages such as: "Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?" you should probably reboot VS Code.

# plugin documentation
TODO: development team should describe what the plugin does, any limitations (ex only in multitenant mode), any known issues interacting with other plugins, etc. Full documentation including a plugin_config sample should be provided.

- v1_0: uses a middleware wrapper around the existing basicmessage `connections/{id}/send-message` api, and will persist
  the sent message. messages between all agents/connections can be fetched via `GET /basicmessages` with optional query params for `connection_id` and `state`.

## build and run

A [Dockerfile](./docker/Dockerfile) is provided to run integration tests. This image is not intended for production as it copies the plugin source and loads its dependencies (including ACA-Py) along with a simplistic ACA-Py configuration file: [default.yml](./docker/default.yml).

### run and debug
In the devcontainer, we can run an ACA-Py instance with our plugin source loaded and set breakpoints for debug (see `launch.json`). 

To run your ACA-Py code in debug mode, go to the `Run and Debug` view, select "Run/Debug Plugin" and click `Start Debugging (F5)`. Using [default.yml](./docker/default.yml), your agent swagger is available at http://localhost:3001/api/doc.

### run integration tests
All plugins should have a suite of integration tests. We use `docker compose` to set up the environment, and make use of the [Dockerfile](./docker/Dockerfile) to produce our ACA-Py/Plugin image. To simplify, we have a [Dockerfile](./int/Dockerfile.test.runner) for running those [tests](./int/tests/).

#### Tests
The integration tests will start 2 agents - bob and alice - and a juggernaut container that will execute the tests. Test results will be found in the juggernaut container output. The juggernaut container should close itself down, the logs can be reviewed in the `Docker` view, open `Containers`, open `int`, right-click the `int-tests` container and select `View Logs`

```sh
# open a terminal in vs code
cd int
docker compose build
docker compose up
```
