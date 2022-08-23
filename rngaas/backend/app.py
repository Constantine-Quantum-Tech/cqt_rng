from flask import Flask, request, after_this_request, send_file
from flask_cors import CORS
from cqt_rng import RNG
from cqt_rng.entropy_sources import BosonSampler
from cqt_rng.post_processors import CQTPP
from time import gmtime, strftime
import os
import numpy as np
from uuid import uuid4

app = Flask(__name__)
CORS(app)


@app.route("/generate", methods=["GET"])
def generate():
    try:
        length = int(request.args.to_dict()["length"])
        rng = RNG(BosonSampler(), CQTPP(dep_seq_len=10), save_sample=False)
        filename = str(uuid4())
        np.save("output/" + filename, rng.generate(length))

        with open(".log", "a") as f:
            time = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
            message = (
                "INFO "
                + request.remote_addr
                + " "
                + time
                + " Generated bistring of length:"
                + str(length)
                + "\n"
            )
            f.write(message)

            return {"filename": filename}

    except Exception as e:
        with open(".log", "a") as f:
            time = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
            message = (
                "ERROR (generate)"
                + request.remote_addr
                + " "
                + time
                + " "
                + str(e)
                + "\n"
            )
            f.write(message)
        return "bad request!", 400


@app.route("/download", methods=["GET"])
def download():
    try:
        file = request.args.to_dict()["file"]
        file_path = f"output/{file}.npy"
        file_handle = open(file_path, "rb")

        @after_this_request
        def remove_file(response):
            try:
                os.remove(file_path)
            except Exception as error:
                with open(".log", "a") as f:
                    time = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
                    message = (
                        "ERROR (download) "
                        + request.remote_addr
                        + " "
                        + time
                        + " error removing the file "
                        + file
                        + "\n"
                    )
                    f.write(message)
            return response

        with open(".log", "a") as f:
            time = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
            message = (
                "INFO " + request.remote_addr + " " + time + " Download " + file + "\n"
            )
            f.write(message)

        return send_file(file_handle, download_name="bitstring.npy"), 200

    except Exception as e:
        with open(".log", "a") as f:
            time = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
            message = (
                "ERROR (download)"
                + request.remote_addr
                + " "
                + time
                + " "
                + str(e)
                + "\n"
            )
            f.write(message)
        return "bad request!", 400
