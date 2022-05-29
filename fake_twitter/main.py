import os
import json
import time
import random
from utils import generate_fake_tweet

from socketserver import ForkingTCPServer, StreamRequestHandler


class MyHandler(StreamRequestHandler):

    def handle(self):
        while True:
            fake_tweet = generate_fake_tweet()
            self.wfile.write(json.dumps(fake_tweet).encode())
            self.wfile.write("\n".encode())
            time.sleep(random.randint(0, 5))


if __name__ == "__main__":
    with ForkingTCPServer(("0.0.0.0", int(os.environ.get("FAKE_TWITTER_PORT", 7000))), MyHandler) as server:
        server.serve_forever()