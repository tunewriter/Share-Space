## How to deploy
* Make a SSH connection to the server
* Optional: Get an SSL certificate (e.g. with [Let's Encrypt](https://letsencrypt.org/))
  * Move the certificate and key to the directory defined in the Dockerfile
* Clone the repository
* Create Docker image:
  * ``docker build -t synimg .``
* Run image in container:
  * ``docker run --name syncont -p 443:443 -e SUPABASE_URL=<url> -e SUPABASE_KEY=<key> -d synimg``
  * If you don't have an SSL certificate: Replace _443_ with _80_ in the command above and adapt the command in the Dockerfile