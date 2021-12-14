import cv2
import dropbox
import time
import random
start_time = time.time()
def take_snapshot():
    number = random.randint(0,1000)
    # initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        # cv2.imwrite()method is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False
    return img_name
    print("Snapshot Taken")
    # releases the camera
    videoCaptureObject.release()
    # closes all the window that might be opened while this process
    cv2.destoryALlWindows()
def upload_file(img_name):
    access_token = "sl.A99Rus19fp5RXAc7rrECS7E_2CRxCjpKLS1A9EG7IpU9jFPMcB39tiPE9--dgDRLqNjTC5gKhNO7M3_nOdAdydNENHwP2b0dRmWOjD0zLedaYR9jkZw_TROrRESe6mU6INIrPP5CX_Rs"
    file = img_name
    file_from = file
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token) 
    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)
main()
    
    

        

