# client.py

import grpc
import pandas as pd
import os
import logging
import upload_pb2
import upload_pb2_grpc

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def upload_apk(stub, apkfile_name, apk_path):
    apkfile_size = os.path.getsize(apk_path)
    with open(apk_path, "rb") as apk_file:
        for chunk in iter(lambda: apk_file.read(8192), b""):
            request = upload_pb2.UploadRequest(
                apkfile_name=apkfile_name,
                apkfile_size=apkfile_size,
                apk_content=chunk,
            )
            response = stub.Upload(request)
            logging.info(f"Client: Uploaded chunk for '{apkfile_name}' - Response: {response.message}")

    # Upload "DONE" status for the corresponding row in paper_report_test.csv
    upload_done_status(apkfile_name)

def upload_done_status(apkfile_name):
    global df  # Make df global so it can be accessed in the function
    # Update the "upload_to_reverse" column in the CSV file
    df.loc[df['apkfile_name'] == apkfile_name, 'upload_to_reverse'] = 'DONE'
    df.to_csv("paper_report_test.csv", index=False)
    logging.info(f"Client: Uploaded 'DONE' status for '{apkfile_name}'")

def main():
    # Read CSV file
    global df  # Make df global so it can be accessed in the upload_apk function
    df = pd.read_csv("paper_report_test.csv")

    # Connect to the gRPC server
    channel = grpc.insecure_channel('192.168.107.143:50051')  # Replace with your server IP and port
    stub = upload_pb2_grpc.YourServiceStub(channel)

    for index, row in df.iterrows():
        apkfile_name = row["apkfile_name"]
        apk_path = f"/root/metaLeak-ml-apk-upload-client/{apkfile_name}"

        # Upload APK file
        logging.info(f"Client: Uploading '{apkfile_name}' to server...")
        upload_apk(stub, apkfile_name, apk_path)

if __name__ == "__main__":
    main()
